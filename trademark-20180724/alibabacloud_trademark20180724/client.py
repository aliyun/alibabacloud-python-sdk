# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_trademark20180724 import models as trademark_20180724_models
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
        self._endpoint = self.get_endpoint('trademark', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_trade_produce_list_with_options(
        self,
        request: trademark_20180724_models.QueryTradeProduceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeProduceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeProduceListResponse(),
            self.do_rpcrequest('QueryTradeProduceList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trade_produce_list_with_options_async(
        self,
        request: trademark_20180724_models.QueryTradeProduceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeProduceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeProduceListResponse(),
            await self.do_rpcrequest_async('QueryTradeProduceList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_produce_list(
        self,
        request: trademark_20180724_models.QueryTradeProduceListRequest,
    ) -> trademark_20180724_models.QueryTradeProduceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trade_produce_list_with_options(request, runtime)

    async def query_trade_produce_list_async(
        self,
        request: trademark_20180724_models.QueryTradeProduceListRequest,
    ) -> trademark_20180724_models.QueryTradeProduceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trade_produce_list_with_options_async(request, runtime)

    def query_trademark_monitor_results_with_options(
        self,
        request: trademark_20180724_models.QueryTrademarkMonitorResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTrademarkMonitorResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkMonitorResultsResponse(),
            self.do_rpcrequest('QueryTrademarkMonitorResults', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trademark_monitor_results_with_options_async(
        self,
        request: trademark_20180724_models.QueryTrademarkMonitorResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTrademarkMonitorResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkMonitorResultsResponse(),
            await self.do_rpcrequest_async('QueryTrademarkMonitorResults', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trademark_monitor_results(
        self,
        request: trademark_20180724_models.QueryTrademarkMonitorResultsRequest,
    ) -> trademark_20180724_models.QueryTrademarkMonitorResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_monitor_results_with_options(request, runtime)

    async def query_trademark_monitor_results_async(
        self,
        request: trademark_20180724_models.QueryTrademarkMonitorResultsRequest,
    ) -> trademark_20180724_models.QueryTrademarkMonitorResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trademark_monitor_results_with_options_async(request, runtime)

    def cancel_trade_order_with_options(
        self,
        request: trademark_20180724_models.CancelTradeOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CancelTradeOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CancelTradeOrderResponse(),
            self.do_rpcrequest('CancelTradeOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_trade_order_with_options_async(
        self,
        request: trademark_20180724_models.CancelTradeOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CancelTradeOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CancelTradeOrderResponse(),
            await self.do_rpcrequest_async('CancelTradeOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_trade_order(
        self,
        request: trademark_20180724_models.CancelTradeOrderRequest,
    ) -> trademark_20180724_models.CancelTradeOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_trade_order_with_options(request, runtime)

    async def cancel_trade_order_async(
        self,
        request: trademark_20180724_models.CancelTradeOrderRequest,
    ) -> trademark_20180724_models.CancelTradeOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_trade_order_with_options_async(request, runtime)

    def delete_tm_monitor_rule_with_options(
        self,
        request: trademark_20180724_models.DeleteTmMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.DeleteTmMonitorRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteTmMonitorRuleResponse(),
            self.do_rpcrequest('DeleteTmMonitorRule', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_tm_monitor_rule_with_options_async(
        self,
        request: trademark_20180724_models.DeleteTmMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.DeleteTmMonitorRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteTmMonitorRuleResponse(),
            await self.do_rpcrequest_async('DeleteTmMonitorRule', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_tm_monitor_rule(
        self,
        request: trademark_20180724_models.DeleteTmMonitorRuleRequest,
    ) -> trademark_20180724_models.DeleteTmMonitorRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tm_monitor_rule_with_options(request, runtime)

    async def delete_tm_monitor_rule_async(
        self,
        request: trademark_20180724_models.DeleteTmMonitorRuleRequest,
    ) -> trademark_20180724_models.DeleteTmMonitorRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tm_monitor_rule_with_options_async(request, runtime)

    def upload_notary_data_with_options(
        self,
        request: trademark_20180724_models.UploadNotaryDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UploadNotaryDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UploadNotaryDataResponse(),
            self.do_rpcrequest('UploadNotaryData', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_notary_data_with_options_async(
        self,
        request: trademark_20180724_models.UploadNotaryDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UploadNotaryDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UploadNotaryDataResponse(),
            await self.do_rpcrequest_async('UploadNotaryData', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_notary_data(
        self,
        request: trademark_20180724_models.UploadNotaryDataRequest,
    ) -> trademark_20180724_models.UploadNotaryDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_notary_data_with_options(request, runtime)

    async def upload_notary_data_async(
        self,
        request: trademark_20180724_models.UploadNotaryDataRequest,
    ) -> trademark_20180724_models.UploadNotaryDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_notary_data_with_options_async(request, runtime)

    def copy_applicant_with_options(
        self,
        request: trademark_20180724_models.CopyApplicantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CopyApplicantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CopyApplicantResponse(),
            self.do_rpcrequest('CopyApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_applicant_with_options_async(
        self,
        request: trademark_20180724_models.CopyApplicantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CopyApplicantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CopyApplicantResponse(),
            await self.do_rpcrequest_async('CopyApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_applicant(
        self,
        request: trademark_20180724_models.CopyApplicantRequest,
    ) -> trademark_20180724_models.CopyApplicantResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_applicant_with_options(request, runtime)

    async def copy_applicant_async(
        self,
        request: trademark_20180724_models.CopyApplicantRequest,
    ) -> trademark_20180724_models.CopyApplicantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_applicant_with_options_async(request, runtime)

    def partner_update_trademark_name_with_options(
        self,
        request: trademark_20180724_models.PartnerUpdateTrademarkNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.PartnerUpdateTrademarkNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.PartnerUpdateTrademarkNameResponse(),
            self.do_rpcrequest('PartnerUpdateTrademarkName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def partner_update_trademark_name_with_options_async(
        self,
        request: trademark_20180724_models.PartnerUpdateTrademarkNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.PartnerUpdateTrademarkNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.PartnerUpdateTrademarkNameResponse(),
            await self.do_rpcrequest_async('PartnerUpdateTrademarkName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def partner_update_trademark_name(
        self,
        request: trademark_20180724_models.PartnerUpdateTrademarkNameRequest,
    ) -> trademark_20180724_models.PartnerUpdateTrademarkNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.partner_update_trademark_name_with_options(request, runtime)

    async def partner_update_trademark_name_async(
        self,
        request: trademark_20180724_models.PartnerUpdateTrademarkNameRequest,
    ) -> trademark_20180724_models.PartnerUpdateTrademarkNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.partner_update_trademark_name_with_options_async(request, runtime)

    def query_intention_detail_with_options(
        self,
        request: trademark_20180724_models.QueryIntentionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryIntentionDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionDetailResponse(),
            self.do_rpcrequest('QueryIntentionDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_intention_detail_with_options_async(
        self,
        request: trademark_20180724_models.QueryIntentionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryIntentionDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionDetailResponse(),
            await self.do_rpcrequest_async('QueryIntentionDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_intention_detail(
        self,
        request: trademark_20180724_models.QueryIntentionDetailRequest,
    ) -> trademark_20180724_models.QueryIntentionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_intention_detail_with_options(request, runtime)

    async def query_intention_detail_async(
        self,
        request: trademark_20180724_models.QueryIntentionDetailRequest,
    ) -> trademark_20180724_models.QueryIntentionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_intention_detail_with_options_async(request, runtime)

    def query_intention_price_with_options(
        self,
        request: trademark_20180724_models.QueryIntentionPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryIntentionPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionPriceResponse(),
            self.do_rpcrequest('QueryIntentionPrice', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_intention_price_with_options_async(
        self,
        request: trademark_20180724_models.QueryIntentionPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryIntentionPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionPriceResponse(),
            await self.do_rpcrequest_async('QueryIntentionPrice', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_intention_price(
        self,
        request: trademark_20180724_models.QueryIntentionPriceRequest,
    ) -> trademark_20180724_models.QueryIntentionPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_intention_price_with_options(request, runtime)

    async def query_intention_price_async(
        self,
        request: trademark_20180724_models.QueryIntentionPriceRequest,
    ) -> trademark_20180724_models.QueryIntentionPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_intention_price_with_options_async(request, runtime)

    def query_official_file_custom_list_with_options(
        self,
        request: trademark_20180724_models.QueryOfficialFileCustomListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryOfficialFileCustomListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryOfficialFileCustomListResponse(),
            self.do_rpcrequest('QueryOfficialFileCustomList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_official_file_custom_list_with_options_async(
        self,
        request: trademark_20180724_models.QueryOfficialFileCustomListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryOfficialFileCustomListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryOfficialFileCustomListResponse(),
            await self.do_rpcrequest_async('QueryOfficialFileCustomList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_official_file_custom_list(
        self,
        request: trademark_20180724_models.QueryOfficialFileCustomListRequest,
    ) -> trademark_20180724_models.QueryOfficialFileCustomListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_official_file_custom_list_with_options(request, runtime)

    async def query_official_file_custom_list_async(
        self,
        request: trademark_20180724_models.QueryOfficialFileCustomListRequest,
    ) -> trademark_20180724_models.QueryOfficialFileCustomListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_official_file_custom_list_with_options_async(request, runtime)

    def check_trademark_icon_with_options(
        self,
        request: trademark_20180724_models.CheckTrademarkIconRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CheckTrademarkIconResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckTrademarkIconResponse(),
            self.do_rpcrequest('CheckTrademarkIcon', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_trademark_icon_with_options_async(
        self,
        request: trademark_20180724_models.CheckTrademarkIconRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CheckTrademarkIconResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckTrademarkIconResponse(),
            await self.do_rpcrequest_async('CheckTrademarkIcon', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_trademark_icon(
        self,
        request: trademark_20180724_models.CheckTrademarkIconRequest,
    ) -> trademark_20180724_models.CheckTrademarkIconResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_trademark_icon_with_options(request, runtime)

    async def check_trademark_icon_async(
        self,
        request: trademark_20180724_models.CheckTrademarkIconRequest,
    ) -> trademark_20180724_models.CheckTrademarkIconResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_trademark_icon_with_options_async(request, runtime)

    def query_supplement_detail_with_options(
        self,
        request: trademark_20180724_models.QuerySupplementDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QuerySupplementDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QuerySupplementDetailResponse(),
            self.do_rpcrequest('QuerySupplementDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_supplement_detail_with_options_async(
        self,
        request: trademark_20180724_models.QuerySupplementDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QuerySupplementDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QuerySupplementDetailResponse(),
            await self.do_rpcrequest_async('QuerySupplementDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_supplement_detail(
        self,
        request: trademark_20180724_models.QuerySupplementDetailRequest,
    ) -> trademark_20180724_models.QuerySupplementDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_supplement_detail_with_options(request, runtime)

    async def query_supplement_detail_async(
        self,
        request: trademark_20180724_models.QuerySupplementDetailRequest,
    ) -> trademark_20180724_models.QuerySupplementDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_supplement_detail_with_options_async(request, runtime)

    def upload_trademark_on_sale_with_options(
        self,
        request: trademark_20180724_models.UploadTrademarkOnSaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UploadTrademarkOnSaleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UploadTrademarkOnSaleResponse(),
            self.do_rpcrequest('UploadTrademarkOnSale', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_trademark_on_sale_with_options_async(
        self,
        request: trademark_20180724_models.UploadTrademarkOnSaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UploadTrademarkOnSaleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UploadTrademarkOnSaleResponse(),
            await self.do_rpcrequest_async('UploadTrademarkOnSale', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_trademark_on_sale(
        self,
        request: trademark_20180724_models.UploadTrademarkOnSaleRequest,
    ) -> trademark_20180724_models.UploadTrademarkOnSaleResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_trademark_on_sale_with_options(request, runtime)

    async def upload_trademark_on_sale_async(
        self,
        request: trademark_20180724_models.UploadTrademarkOnSaleRequest,
    ) -> trademark_20180724_models.UploadTrademarkOnSaleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_trademark_on_sale_with_options_async(request, runtime)

    def apply_notary_post_with_options(
        self,
        request: trademark_20180724_models.ApplyNotaryPostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ApplyNotaryPostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ApplyNotaryPostResponse(),
            self.do_rpcrequest('ApplyNotaryPost', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_notary_post_with_options_async(
        self,
        request: trademark_20180724_models.ApplyNotaryPostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ApplyNotaryPostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ApplyNotaryPostResponse(),
            await self.do_rpcrequest_async('ApplyNotaryPost', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_notary_post(
        self,
        request: trademark_20180724_models.ApplyNotaryPostRequest,
    ) -> trademark_20180724_models.ApplyNotaryPostResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_notary_post_with_options(request, runtime)

    async def apply_notary_post_async(
        self,
        request: trademark_20180724_models.ApplyNotaryPostRequest,
    ) -> trademark_20180724_models.ApplyNotaryPostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_notary_post_with_options_async(request, runtime)

    def query_trade_mark_applications_by_intention_with_options(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationsByIntentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationsByIntentionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationsByIntentionResponse(),
            self.do_rpcrequest('QueryTradeMarkApplicationsByIntention', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trade_mark_applications_by_intention_with_options_async(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationsByIntentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationsByIntentionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationsByIntentionResponse(),
            await self.do_rpcrequest_async('QueryTradeMarkApplicationsByIntention', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_mark_applications_by_intention(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationsByIntentionRequest,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationsByIntentionResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_applications_by_intention_with_options(request, runtime)

    async def query_trade_mark_applications_by_intention_async(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationsByIntentionRequest,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationsByIntentionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trade_mark_applications_by_intention_with_options_async(request, runtime)

    def save_extension_attribute_with_options(
        self,
        request: trademark_20180724_models.SaveExtensionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SaveExtensionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveExtensionAttributeResponse(),
            self.do_rpcrequest('SaveExtensionAttribute', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_extension_attribute_with_options_async(
        self,
        request: trademark_20180724_models.SaveExtensionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SaveExtensionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveExtensionAttributeResponse(),
            await self.do_rpcrequest_async('SaveExtensionAttribute', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_extension_attribute(
        self,
        request: trademark_20180724_models.SaveExtensionAttributeRequest,
    ) -> trademark_20180724_models.SaveExtensionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_extension_attribute_with_options(request, runtime)

    async def save_extension_attribute_async(
        self,
        request: trademark_20180724_models.SaveExtensionAttributeRequest,
    ) -> trademark_20180724_models.SaveExtensionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_extension_attribute_with_options_async(request, runtime)

    def accept_partner_notification_with_options(
        self,
        request: trademark_20180724_models.AcceptPartnerNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.AcceptPartnerNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.AcceptPartnerNotificationResponse(),
            self.do_rpcrequest('AcceptPartnerNotification', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def accept_partner_notification_with_options_async(
        self,
        request: trademark_20180724_models.AcceptPartnerNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.AcceptPartnerNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.AcceptPartnerNotificationResponse(),
            await self.do_rpcrequest_async('AcceptPartnerNotification', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def accept_partner_notification(
        self,
        request: trademark_20180724_models.AcceptPartnerNotificationRequest,
    ) -> trademark_20180724_models.AcceptPartnerNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_partner_notification_with_options(request, runtime)

    async def accept_partner_notification_async(
        self,
        request: trademark_20180724_models.AcceptPartnerNotificationRequest,
    ) -> trademark_20180724_models.AcceptPartnerNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_partner_notification_with_options_async(request, runtime)

    def submit_supplement_with_options(
        self,
        tmp_req: trademark_20180724_models.SubmitSupplementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SubmitSupplementResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SubmitSupplementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.upload_oss_key_list):
            request.upload_oss_key_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.upload_oss_key_list, 'UploadOssKeyList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SubmitSupplementResponse(),
            self.do_rpcrequest('SubmitSupplement', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_supplement_with_options_async(
        self,
        tmp_req: trademark_20180724_models.SubmitSupplementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SubmitSupplementResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SubmitSupplementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.upload_oss_key_list):
            request.upload_oss_key_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.upload_oss_key_list, 'UploadOssKeyList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SubmitSupplementResponse(),
            await self.do_rpcrequest_async('SubmitSupplement', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_supplement(
        self,
        request: trademark_20180724_models.SubmitSupplementRequest,
    ) -> trademark_20180724_models.SubmitSupplementResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_supplement_with_options(request, runtime)

    async def submit_supplement_async(
        self,
        request: trademark_20180724_models.SubmitSupplementRequest,
    ) -> trademark_20180724_models.SubmitSupplementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_supplement_with_options_async(request, runtime)

    def force_upload_trademark_onsale_with_options(
        self,
        request: trademark_20180724_models.ForceUploadTrademarkOnsaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ForceUploadTrademarkOnsaleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ForceUploadTrademarkOnsaleResponse(),
            self.do_rpcrequest('ForceUploadTrademarkOnsale', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def force_upload_trademark_onsale_with_options_async(
        self,
        request: trademark_20180724_models.ForceUploadTrademarkOnsaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ForceUploadTrademarkOnsaleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ForceUploadTrademarkOnsaleResponse(),
            await self.do_rpcrequest_async('ForceUploadTrademarkOnsale', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def force_upload_trademark_onsale(
        self,
        request: trademark_20180724_models.ForceUploadTrademarkOnsaleRequest,
    ) -> trademark_20180724_models.ForceUploadTrademarkOnsaleResponse:
        runtime = util_models.RuntimeOptions()
        return self.force_upload_trademark_onsale_with_options(request, runtime)

    async def force_upload_trademark_onsale_async(
        self,
        request: trademark_20180724_models.ForceUploadTrademarkOnsaleRequest,
    ) -> trademark_20180724_models.ForceUploadTrademarkOnsaleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.force_upload_trademark_onsale_with_options_async(request, runtime)

    def bind_material_with_options(
        self,
        request: trademark_20180724_models.BindMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.BindMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.BindMaterialResponse(),
            self.do_rpcrequest('BindMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_material_with_options_async(
        self,
        request: trademark_20180724_models.BindMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.BindMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.BindMaterialResponse(),
            await self.do_rpcrequest_async('BindMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_material(
        self,
        request: trademark_20180724_models.BindMaterialRequest,
    ) -> trademark_20180724_models.BindMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_material_with_options(request, runtime)

    async def bind_material_async(
        self,
        request: trademark_20180724_models.BindMaterialRequest,
    ) -> trademark_20180724_models.BindMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_material_with_options_async(request, runtime)

    def get_default_principal_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GetDefaultPrincipalResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            trademark_20180724_models.GetDefaultPrincipalResponse(),
            self.do_rpcrequest('GetDefaultPrincipal', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_default_principal_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GetDefaultPrincipalResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            trademark_20180724_models.GetDefaultPrincipalResponse(),
            await self.do_rpcrequest_async('GetDefaultPrincipal', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_default_principal(self) -> trademark_20180724_models.GetDefaultPrincipalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_principal_with_options(runtime)

    async def get_default_principal_async(self) -> trademark_20180724_models.GetDefaultPrincipalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_principal_with_options_async(runtime)

    def query_communication_logs_with_options(
        self,
        request: trademark_20180724_models.QueryCommunicationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryCommunicationLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryCommunicationLogsResponse(),
            self.do_rpcrequest('QueryCommunicationLogs', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_communication_logs_with_options_async(
        self,
        request: trademark_20180724_models.QueryCommunicationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryCommunicationLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryCommunicationLogsResponse(),
            await self.do_rpcrequest_async('QueryCommunicationLogs', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_communication_logs(
        self,
        request: trademark_20180724_models.QueryCommunicationLogsRequest,
    ) -> trademark_20180724_models.QueryCommunicationLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_communication_logs_with_options(request, runtime)

    async def query_communication_logs_async(
        self,
        request: trademark_20180724_models.QueryCommunicationLogsRequest,
    ) -> trademark_20180724_models.QueryCommunicationLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_communication_logs_with_options_async(request, runtime)

    def generate_qr_code_with_options(
        self,
        request: trademark_20180724_models.GenerateQrCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GenerateQrCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GenerateQrCodeResponse(),
            self.do_rpcrequest('GenerateQrCode', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_qr_code_with_options_async(
        self,
        request: trademark_20180724_models.GenerateQrCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GenerateQrCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GenerateQrCodeResponse(),
            await self.do_rpcrequest_async('GenerateQrCode', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_qr_code(
        self,
        request: trademark_20180724_models.GenerateQrCodeRequest,
    ) -> trademark_20180724_models.GenerateQrCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_qr_code_with_options(request, runtime)

    async def generate_qr_code_async(
        self,
        request: trademark_20180724_models.GenerateQrCodeRequest,
    ) -> trademark_20180724_models.GenerateQrCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_qr_code_with_options_async(request, runtime)

    def confirm_dissent_original_with_options(
        self,
        request: trademark_20180724_models.ConfirmDissentOriginalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ConfirmDissentOriginalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmDissentOriginalResponse(),
            self.do_rpcrequest('ConfirmDissentOriginal', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def confirm_dissent_original_with_options_async(
        self,
        request: trademark_20180724_models.ConfirmDissentOriginalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ConfirmDissentOriginalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmDissentOriginalResponse(),
            await self.do_rpcrequest_async('ConfirmDissentOriginal', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def confirm_dissent_original(
        self,
        request: trademark_20180724_models.ConfirmDissentOriginalRequest,
    ) -> trademark_20180724_models.ConfirmDissentOriginalResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_dissent_original_with_options(request, runtime)

    async def confirm_dissent_original_async(
        self,
        request: trademark_20180724_models.ConfirmDissentOriginalRequest,
    ) -> trademark_20180724_models.ConfirmDissentOriginalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_dissent_original_with_options_async(request, runtime)

    def convert_image_to_gray_with_options(
        self,
        request: trademark_20180724_models.ConvertImageToGrayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ConvertImageToGrayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConvertImageToGrayResponse(),
            self.do_rpcrequest('ConvertImageToGray', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def convert_image_to_gray_with_options_async(
        self,
        request: trademark_20180724_models.ConvertImageToGrayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ConvertImageToGrayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConvertImageToGrayResponse(),
            await self.do_rpcrequest_async('ConvertImageToGray', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def convert_image_to_gray(
        self,
        request: trademark_20180724_models.ConvertImageToGrayRequest,
    ) -> trademark_20180724_models.ConvertImageToGrayResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_image_to_gray_with_options(request, runtime)

    async def convert_image_to_gray_async(
        self,
        request: trademark_20180724_models.ConvertImageToGrayRequest,
    ) -> trademark_20180724_models.ConvertImageToGrayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_image_to_gray_with_options_async(request, runtime)

    def query_intention_list_with_options(
        self,
        request: trademark_20180724_models.QueryIntentionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryIntentionListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionListResponse(),
            self.do_rpcrequest('QueryIntentionList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_intention_list_with_options_async(
        self,
        request: trademark_20180724_models.QueryIntentionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryIntentionListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionListResponse(),
            await self.do_rpcrequest_async('QueryIntentionList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_intention_list(
        self,
        request: trademark_20180724_models.QueryIntentionListRequest,
    ) -> trademark_20180724_models.QueryIntentionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_intention_list_with_options(request, runtime)

    async def query_intention_list_async(
        self,
        request: trademark_20180724_models.QueryIntentionListRequest,
    ) -> trademark_20180724_models.QueryIntentionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_intention_list_with_options_async(request, runtime)

    def get_authorization_letter_version_with_options(
        self,
        request: trademark_20180724_models.GetAuthorizationLetterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GetAuthorizationLetterVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetAuthorizationLetterVersionResponse(),
            self.do_rpcrequest('GetAuthorizationLetterVersion', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_authorization_letter_version_with_options_async(
        self,
        request: trademark_20180724_models.GetAuthorizationLetterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GetAuthorizationLetterVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetAuthorizationLetterVersionResponse(),
            await self.do_rpcrequest_async('GetAuthorizationLetterVersion', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_authorization_letter_version(
        self,
        request: trademark_20180724_models.GetAuthorizationLetterVersionRequest,
    ) -> trademark_20180724_models.GetAuthorizationLetterVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_letter_version_with_options(request, runtime)

    async def get_authorization_letter_version_async(
        self,
        request: trademark_20180724_models.GetAuthorizationLetterVersionRequest,
    ) -> trademark_20180724_models.GetAuthorizationLetterVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_authorization_letter_version_with_options_async(request, runtime)

    def query_trademark_price_with_options(
        self,
        tmp_req: trademark_20180724_models.QueryTrademarkPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTrademarkPriceResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.QueryTrademarkPriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_data):
            request.order_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_data, 'OrderData', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkPriceResponse(),
            self.do_rpcrequest('QueryTrademarkPrice', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trademark_price_with_options_async(
        self,
        tmp_req: trademark_20180724_models.QueryTrademarkPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTrademarkPriceResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.QueryTrademarkPriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_data):
            request.order_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_data, 'OrderData', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkPriceResponse(),
            await self.do_rpcrequest_async('QueryTrademarkPrice', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trademark_price(
        self,
        request: trademark_20180724_models.QueryTrademarkPriceRequest,
    ) -> trademark_20180724_models.QueryTrademarkPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_price_with_options(request, runtime)

    async def query_trademark_price_async(
        self,
        request: trademark_20180724_models.QueryTrademarkPriceRequest,
    ) -> trademark_20180724_models.QueryTrademarkPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trademark_price_with_options_async(request, runtime)

    def insert_tm_monitor_rule_with_options(
        self,
        tmp_req: trademark_20180724_models.InsertTmMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.InsertTmMonitorRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.InsertTmMonitorRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.classification):
            request.classification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.classification, 'Classification', 'json')
        if not UtilClient.is_unset(tmp_req.notify_status):
            request.notify_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_status, 'NotifyStatus', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertTmMonitorRuleResponse(),
            self.do_rpcrequest('InsertTmMonitorRule', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_tm_monitor_rule_with_options_async(
        self,
        tmp_req: trademark_20180724_models.InsertTmMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.InsertTmMonitorRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.InsertTmMonitorRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.classification):
            request.classification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.classification, 'Classification', 'json')
        if not UtilClient.is_unset(tmp_req.notify_status):
            request.notify_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_status, 'NotifyStatus', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertTmMonitorRuleResponse(),
            await self.do_rpcrequest_async('InsertTmMonitorRule', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_tm_monitor_rule(
        self,
        request: trademark_20180724_models.InsertTmMonitorRuleRequest,
    ) -> trademark_20180724_models.InsertTmMonitorRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_tm_monitor_rule_with_options(request, runtime)

    async def insert_tm_monitor_rule_async(
        self,
        request: trademark_20180724_models.InsertTmMonitorRuleRequest,
    ) -> trademark_20180724_models.InsertTmMonitorRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_tm_monitor_rule_with_options_async(request, runtime)

    def query_trademark_monitor_rules_with_options(
        self,
        request: trademark_20180724_models.QueryTrademarkMonitorRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTrademarkMonitorRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkMonitorRulesResponse(),
            self.do_rpcrequest('QueryTrademarkMonitorRules', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trademark_monitor_rules_with_options_async(
        self,
        request: trademark_20180724_models.QueryTrademarkMonitorRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTrademarkMonitorRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkMonitorRulesResponse(),
            await self.do_rpcrequest_async('QueryTrademarkMonitorRules', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trademark_monitor_rules(
        self,
        request: trademark_20180724_models.QueryTrademarkMonitorRulesRequest,
    ) -> trademark_20180724_models.QueryTrademarkMonitorRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_monitor_rules_with_options(request, runtime)

    async def query_trademark_monitor_rules_async(
        self,
        request: trademark_20180724_models.QueryTrademarkMonitorRulesRequest,
    ) -> trademark_20180724_models.QueryTrademarkMonitorRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trademark_monitor_rules_with_options_async(request, runtime)

    def deny_supplement_with_options(
        self,
        request: trademark_20180724_models.DenySupplementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.DenySupplementResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DenySupplementResponse(),
            self.do_rpcrequest('DenySupplement', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deny_supplement_with_options_async(
        self,
        request: trademark_20180724_models.DenySupplementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.DenySupplementResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DenySupplementResponse(),
            await self.do_rpcrequest_async('DenySupplement', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deny_supplement(
        self,
        request: trademark_20180724_models.DenySupplementRequest,
    ) -> trademark_20180724_models.DenySupplementResponse:
        runtime = util_models.RuntimeOptions()
        return self.deny_supplement_with_options(request, runtime)

    async def deny_supplement_async(
        self,
        request: trademark_20180724_models.DenySupplementRequest,
    ) -> trademark_20180724_models.DenySupplementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deny_supplement_with_options_async(request, runtime)

    def query_material_with_options(
        self,
        request: trademark_20180724_models.QueryMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMaterialResponse(),
            self.do_rpcrequest('QueryMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_material_with_options_async(
        self,
        request: trademark_20180724_models.QueryMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMaterialResponse(),
            await self.do_rpcrequest_async('QueryMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_material(
        self,
        request: trademark_20180724_models.QueryMaterialRequest,
    ) -> trademark_20180724_models.QueryMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_material_with_options(request, runtime)

    async def query_material_async(
        self,
        request: trademark_20180724_models.QueryMaterialRequest,
    ) -> trademark_20180724_models.QueryMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_material_with_options_async(request, runtime)

    def create_trademark_order_with_options(
        self,
        request: trademark_20180724_models.CreateTrademarkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CreateTrademarkOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateTrademarkOrderResponse(),
            self.do_rpcrequest('CreateTrademarkOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_trademark_order_with_options_async(
        self,
        request: trademark_20180724_models.CreateTrademarkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CreateTrademarkOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateTrademarkOrderResponse(),
            await self.do_rpcrequest_async('CreateTrademarkOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_trademark_order(
        self,
        request: trademark_20180724_models.CreateTrademarkOrderRequest,
    ) -> trademark_20180724_models.CreateTrademarkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_trademark_order_with_options(request, runtime)

    async def create_trademark_order_async(
        self,
        request: trademark_20180724_models.CreateTrademarkOrderRequest,
    ) -> trademark_20180724_models.CreateTrademarkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_trademark_order_with_options_async(request, runtime)

    def query_material_list_with_options(
        self,
        request: trademark_20180724_models.QueryMaterialListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryMaterialListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMaterialListResponse(),
            self.do_rpcrequest('QueryMaterialList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_material_list_with_options_async(
        self,
        request: trademark_20180724_models.QueryMaterialListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryMaterialListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMaterialListResponse(),
            await self.do_rpcrequest_async('QueryMaterialList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_material_list(
        self,
        request: trademark_20180724_models.QueryMaterialListRequest,
    ) -> trademark_20180724_models.QueryMaterialListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_material_list_with_options(request, runtime)

    async def query_material_list_async(
        self,
        request: trademark_20180724_models.QueryMaterialListRequest,
    ) -> trademark_20180724_models.QueryMaterialListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_material_list_with_options_async(request, runtime)

    def check_trademark_order_with_options(
        self,
        request: trademark_20180724_models.CheckTrademarkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CheckTrademarkOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckTrademarkOrderResponse(),
            self.do_rpcrequest('CheckTrademarkOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_trademark_order_with_options_async(
        self,
        request: trademark_20180724_models.CheckTrademarkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CheckTrademarkOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckTrademarkOrderResponse(),
            await self.do_rpcrequest_async('CheckTrademarkOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_trademark_order(
        self,
        request: trademark_20180724_models.CheckTrademarkOrderRequest,
    ) -> trademark_20180724_models.CheckTrademarkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_trademark_order_with_options(request, runtime)

    async def check_trademark_order_async(
        self,
        request: trademark_20180724_models.CheckTrademarkOrderRequest,
    ) -> trademark_20180724_models.CheckTrademarkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_trademark_order_with_options_async(request, runtime)

    def query_trade_mark_applications_with_options(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationsResponse(),
            self.do_rpcrequest('QueryTradeMarkApplications', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trade_mark_applications_with_options_async(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationsResponse(),
            await self.do_rpcrequest_async('QueryTradeMarkApplications', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_mark_applications(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationsRequest,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_applications_with_options(request, runtime)

    async def query_trade_mark_applications_async(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationsRequest,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trade_mark_applications_with_options_async(request, runtime)

    def update_applicant_contacter_with_options(
        self,
        request: trademark_20180724_models.UpdateApplicantContacterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UpdateApplicantContacterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateApplicantContacterResponse(),
            self.do_rpcrequest('UpdateApplicantContacter', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_applicant_contacter_with_options_async(
        self,
        request: trademark_20180724_models.UpdateApplicantContacterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UpdateApplicantContacterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateApplicantContacterResponse(),
            await self.do_rpcrequest_async('UpdateApplicantContacter', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_applicant_contacter(
        self,
        request: trademark_20180724_models.UpdateApplicantContacterRequest,
    ) -> trademark_20180724_models.UpdateApplicantContacterResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_applicant_contacter_with_options(request, runtime)

    async def update_applicant_contacter_async(
        self,
        request: trademark_20180724_models.UpdateApplicantContacterRequest,
    ) -> trademark_20180724_models.UpdateApplicantContacterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_applicant_contacter_with_options_async(request, runtime)

    def save_task_with_options(
        self,
        request: trademark_20180724_models.SaveTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SaveTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTaskResponse(),
            self.do_rpcrequest('SaveTask', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_task_with_options_async(
        self,
        request: trademark_20180724_models.SaveTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SaveTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTaskResponse(),
            await self.do_rpcrequest_async('SaveTask', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_task(
        self,
        request: trademark_20180724_models.SaveTaskRequest,
    ) -> trademark_20180724_models.SaveTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_task_with_options(request, runtime)

    async def save_task_async(
        self,
        request: trademark_20180724_models.SaveTaskRequest,
    ) -> trademark_20180724_models.SaveTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_task_with_options_async(request, runtime)

    def submit_trademark_application_complaint_with_options(
        self,
        tmp_req: trademark_20180724_models.SubmitTrademarkApplicationComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SubmitTrademarkApplicationComplaintResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SubmitTrademarkApplicationComplaintShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SubmitTrademarkApplicationComplaintResponse(),
            self.do_rpcrequest('SubmitTrademarkApplicationComplaint', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_trademark_application_complaint_with_options_async(
        self,
        tmp_req: trademark_20180724_models.SubmitTrademarkApplicationComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SubmitTrademarkApplicationComplaintResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SubmitTrademarkApplicationComplaintShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SubmitTrademarkApplicationComplaintResponse(),
            await self.do_rpcrequest_async('SubmitTrademarkApplicationComplaint', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_trademark_application_complaint(
        self,
        request: trademark_20180724_models.SubmitTrademarkApplicationComplaintRequest,
    ) -> trademark_20180724_models.SubmitTrademarkApplicationComplaintResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_trademark_application_complaint_with_options(request, runtime)

    async def submit_trademark_application_complaint_async(
        self,
        request: trademark_20180724_models.SubmitTrademarkApplicationComplaintRequest,
    ) -> trademark_20180724_models.SubmitTrademarkApplicationComplaintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_trademark_application_complaint_with_options_async(request, runtime)

    def write_intention_communication_log_with_options(
        self,
        request: trademark_20180724_models.WriteIntentionCommunicationLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.WriteIntentionCommunicationLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.WriteIntentionCommunicationLogResponse(),
            self.do_rpcrequest('WriteIntentionCommunicationLog', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def write_intention_communication_log_with_options_async(
        self,
        request: trademark_20180724_models.WriteIntentionCommunicationLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.WriteIntentionCommunicationLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.WriteIntentionCommunicationLogResponse(),
            await self.do_rpcrequest_async('WriteIntentionCommunicationLog', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def write_intention_communication_log(
        self,
        request: trademark_20180724_models.WriteIntentionCommunicationLogRequest,
    ) -> trademark_20180724_models.WriteIntentionCommunicationLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.write_intention_communication_log_with_options(request, runtime)

    async def write_intention_communication_log_async(
        self,
        request: trademark_20180724_models.WriteIntentionCommunicationLogRequest,
    ) -> trademark_20180724_models.WriteIntentionCommunicationLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.write_intention_communication_log_with_options_async(request, runtime)

    def save_task_for_official_file_custom_with_options(
        self,
        request: trademark_20180724_models.SaveTaskForOfficialFileCustomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SaveTaskForOfficialFileCustomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTaskForOfficialFileCustomResponse(),
            self.do_rpcrequest('SaveTaskForOfficialFileCustom', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_task_for_official_file_custom_with_options_async(
        self,
        request: trademark_20180724_models.SaveTaskForOfficialFileCustomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SaveTaskForOfficialFileCustomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTaskForOfficialFileCustomResponse(),
            await self.do_rpcrequest_async('SaveTaskForOfficialFileCustom', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_task_for_official_file_custom(
        self,
        request: trademark_20180724_models.SaveTaskForOfficialFileCustomRequest,
    ) -> trademark_20180724_models.SaveTaskForOfficialFileCustomResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_official_file_custom_with_options(request, runtime)

    async def save_task_for_official_file_custom_async(
        self,
        request: trademark_20180724_models.SaveTaskForOfficialFileCustomRequest,
    ) -> trademark_20180724_models.SaveTaskForOfficialFileCustomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_task_for_official_file_custom_with_options_async(request, runtime)

    def descirbe_combine_trademark_with_options(
        self,
        request: trademark_20180724_models.DescirbeCombineTrademarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.DescirbeCombineTrademarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DescirbeCombineTrademarkResponse(),
            self.do_rpcrequest('DescirbeCombineTrademark', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def descirbe_combine_trademark_with_options_async(
        self,
        request: trademark_20180724_models.DescirbeCombineTrademarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.DescirbeCombineTrademarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DescirbeCombineTrademarkResponse(),
            await self.do_rpcrequest_async('DescirbeCombineTrademark', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def descirbe_combine_trademark(
        self,
        request: trademark_20180724_models.DescirbeCombineTrademarkRequest,
    ) -> trademark_20180724_models.DescirbeCombineTrademarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.descirbe_combine_trademark_with_options(request, runtime)

    async def descirbe_combine_trademark_async(
        self,
        request: trademark_20180724_models.DescirbeCombineTrademarkRequest,
    ) -> trademark_20180724_models.DescirbeCombineTrademarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.descirbe_combine_trademark_with_options_async(request, runtime)

    def get_notary_order_with_options(
        self,
        request: trademark_20180724_models.GetNotaryOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GetNotaryOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetNotaryOrderResponse(),
            self.do_rpcrequest('GetNotaryOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_notary_order_with_options_async(
        self,
        request: trademark_20180724_models.GetNotaryOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GetNotaryOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetNotaryOrderResponse(),
            await self.do_rpcrequest_async('GetNotaryOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_notary_order(
        self,
        request: trademark_20180724_models.GetNotaryOrderRequest,
    ) -> trademark_20180724_models.GetNotaryOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_notary_order_with_options(request, runtime)

    async def get_notary_order_async(
        self,
        request: trademark_20180724_models.GetNotaryOrderRequest,
    ) -> trademark_20180724_models.GetNotaryOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_notary_order_with_options_async(request, runtime)

    def confirm_additional_material_with_options(
        self,
        request: trademark_20180724_models.ConfirmAdditionalMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ConfirmAdditionalMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmAdditionalMaterialResponse(),
            self.do_rpcrequest('ConfirmAdditionalMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def confirm_additional_material_with_options_async(
        self,
        request: trademark_20180724_models.ConfirmAdditionalMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ConfirmAdditionalMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmAdditionalMaterialResponse(),
            await self.do_rpcrequest_async('ConfirmAdditionalMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def confirm_additional_material(
        self,
        request: trademark_20180724_models.ConfirmAdditionalMaterialRequest,
    ) -> trademark_20180724_models.ConfirmAdditionalMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_additional_material_with_options(request, runtime)

    async def confirm_additional_material_async(
        self,
        request: trademark_20180724_models.ConfirmAdditionalMaterialRequest,
    ) -> trademark_20180724_models.ConfirmAdditionalMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_additional_material_with_options_async(request, runtime)

    def insert_renew_info_with_options(
        self,
        request: trademark_20180724_models.InsertRenewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.InsertRenewInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertRenewInfoResponse(),
            self.do_rpcrequest('InsertRenewInfo', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_renew_info_with_options_async(
        self,
        request: trademark_20180724_models.InsertRenewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.InsertRenewInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertRenewInfoResponse(),
            await self.do_rpcrequest_async('InsertRenewInfo', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_renew_info(
        self,
        request: trademark_20180724_models.InsertRenewInfoRequest,
    ) -> trademark_20180724_models.InsertRenewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_renew_info_with_options(request, runtime)

    async def insert_renew_info_async(
        self,
        request: trademark_20180724_models.InsertRenewInfoRequest,
    ) -> trademark_20180724_models.InsertRenewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_renew_info_with_options_async(request, runtime)

    def query_credentials_info_with_options(
        self,
        request: trademark_20180724_models.QueryCredentialsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryCredentialsInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryCredentialsInfoResponse(),
            self.do_rpcrequest('QueryCredentialsInfo', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_credentials_info_with_options_async(
        self,
        request: trademark_20180724_models.QueryCredentialsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryCredentialsInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryCredentialsInfoResponse(),
            await self.do_rpcrequest_async('QueryCredentialsInfo', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_credentials_info(
        self,
        request: trademark_20180724_models.QueryCredentialsInfoRequest,
    ) -> trademark_20180724_models.QueryCredentialsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_credentials_info_with_options(request, runtime)

    async def query_credentials_info_async(
        self,
        request: trademark_20180724_models.QueryCredentialsInfoRequest,
    ) -> trademark_20180724_models.QueryCredentialsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_credentials_info_with_options_async(request, runtime)

    def search_tm_onsales_with_options(
        self,
        request: trademark_20180724_models.SearchTmOnsalesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SearchTmOnsalesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SearchTmOnsalesResponse(),
            self.do_rpcrequest('SearchTmOnsales', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_tm_onsales_with_options_async(
        self,
        request: trademark_20180724_models.SearchTmOnsalesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SearchTmOnsalesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SearchTmOnsalesResponse(),
            await self.do_rpcrequest_async('SearchTmOnsales', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_tm_onsales(
        self,
        request: trademark_20180724_models.SearchTmOnsalesRequest,
    ) -> trademark_20180724_models.SearchTmOnsalesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_tm_onsales_with_options(request, runtime)

    async def search_tm_onsales_async(
        self,
        request: trademark_20180724_models.SearchTmOnsalesRequest,
    ) -> trademark_20180724_models.SearchTmOnsalesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_tm_onsales_with_options_async(request, runtime)

    def generate_upload_file_policy_with_options(
        self,
        request: trademark_20180724_models.GenerateUploadFilePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GenerateUploadFilePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GenerateUploadFilePolicyResponse(),
            self.do_rpcrequest('GenerateUploadFilePolicy', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_upload_file_policy_with_options_async(
        self,
        request: trademark_20180724_models.GenerateUploadFilePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GenerateUploadFilePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GenerateUploadFilePolicyResponse(),
            await self.do_rpcrequest_async('GenerateUploadFilePolicy', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_upload_file_policy(
        self,
        request: trademark_20180724_models.GenerateUploadFilePolicyRequest,
    ) -> trademark_20180724_models.GenerateUploadFilePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_file_policy_with_options(request, runtime)

    async def generate_upload_file_policy_async(
        self,
        request: trademark_20180724_models.GenerateUploadFilePolicyRequest,
    ) -> trademark_20180724_models.GenerateUploadFilePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_upload_file_policy_with_options_async(request, runtime)

    def delete_material_with_options(
        self,
        request: trademark_20180724_models.DeleteMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.DeleteMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteMaterialResponse(),
            self.do_rpcrequest('DeleteMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_material_with_options_async(
        self,
        request: trademark_20180724_models.DeleteMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.DeleteMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteMaterialResponse(),
            await self.do_rpcrequest_async('DeleteMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_material(
        self,
        request: trademark_20180724_models.DeleteMaterialRequest,
    ) -> trademark_20180724_models.DeleteMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_material_with_options(request, runtime)

    async def delete_material_async(
        self,
        request: trademark_20180724_models.DeleteMaterialRequest,
    ) -> trademark_20180724_models.DeleteMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_material_with_options_async(request, runtime)

    def write_communication_log_with_options(
        self,
        request: trademark_20180724_models.WriteCommunicationLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.WriteCommunicationLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.WriteCommunicationLogResponse(),
            self.do_rpcrequest('WriteCommunicationLog', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def write_communication_log_with_options_async(
        self,
        request: trademark_20180724_models.WriteCommunicationLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.WriteCommunicationLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.WriteCommunicationLogResponse(),
            await self.do_rpcrequest_async('WriteCommunicationLog', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def write_communication_log(
        self,
        request: trademark_20180724_models.WriteCommunicationLogRequest,
    ) -> trademark_20180724_models.WriteCommunicationLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.write_communication_log_with_options(request, runtime)

    async def write_communication_log_async(
        self,
        request: trademark_20180724_models.WriteCommunicationLogRequest,
    ) -> trademark_20180724_models.WriteCommunicationLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.write_communication_log_with_options_async(request, runtime)

    def insert_trade_intention_user_with_options(
        self,
        request: trademark_20180724_models.InsertTradeIntentionUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.InsertTradeIntentionUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertTradeIntentionUserResponse(),
            self.do_rpcrequest('InsertTradeIntentionUser', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_trade_intention_user_with_options_async(
        self,
        request: trademark_20180724_models.InsertTradeIntentionUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.InsertTradeIntentionUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertTradeIntentionUserResponse(),
            await self.do_rpcrequest_async('InsertTradeIntentionUser', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_trade_intention_user(
        self,
        request: trademark_20180724_models.InsertTradeIntentionUserRequest,
    ) -> trademark_20180724_models.InsertTradeIntentionUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_trade_intention_user_with_options(request, runtime)

    async def insert_trade_intention_user_async(
        self,
        request: trademark_20180724_models.InsertTradeIntentionUserRequest,
    ) -> trademark_20180724_models.InsertTradeIntentionUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_trade_intention_user_with_options_async(request, runtime)

    def query_extension_attribute_with_options(
        self,
        request: trademark_20180724_models.QueryExtensionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryExtensionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryExtensionAttributeResponse(),
            self.do_rpcrequest('QueryExtensionAttribute', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_extension_attribute_with_options_async(
        self,
        request: trademark_20180724_models.QueryExtensionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryExtensionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryExtensionAttributeResponse(),
            await self.do_rpcrequest_async('QueryExtensionAttribute', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_extension_attribute(
        self,
        request: trademark_20180724_models.QueryExtensionAttributeRequest,
    ) -> trademark_20180724_models.QueryExtensionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_extension_attribute_with_options(request, runtime)

    async def query_extension_attribute_async(
        self,
        request: trademark_20180724_models.QueryExtensionAttributeRequest,
    ) -> trademark_20180724_models.QueryExtensionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_extension_attribute_with_options_async(request, runtime)

    def update_trademark_onsale_with_options(
        self,
        request: trademark_20180724_models.UpdateTrademarkOnsaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UpdateTrademarkOnsaleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateTrademarkOnsaleResponse(),
            self.do_rpcrequest('UpdateTrademarkOnsale', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_trademark_onsale_with_options_async(
        self,
        request: trademark_20180724_models.UpdateTrademarkOnsaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UpdateTrademarkOnsaleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateTrademarkOnsaleResponse(),
            await self.do_rpcrequest_async('UpdateTrademarkOnsale', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_trademark_onsale(
        self,
        request: trademark_20180724_models.UpdateTrademarkOnsaleRequest,
    ) -> trademark_20180724_models.UpdateTrademarkOnsaleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_trademark_onsale_with_options(request, runtime)

    async def update_trademark_onsale_async(
        self,
        request: trademark_20180724_models.UpdateTrademarkOnsaleRequest,
    ) -> trademark_20180724_models.UpdateTrademarkOnsaleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_trademark_onsale_with_options_async(request, runtime)

    def query_trade_produce_detail_with_options(
        self,
        request: trademark_20180724_models.QueryTradeProduceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeProduceDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeProduceDetailResponse(),
            self.do_rpcrequest('QueryTradeProduceDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trade_produce_detail_with_options_async(
        self,
        request: trademark_20180724_models.QueryTradeProduceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeProduceDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeProduceDetailResponse(),
            await self.do_rpcrequest_async('QueryTradeProduceDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_produce_detail(
        self,
        request: trademark_20180724_models.QueryTradeProduceDetailRequest,
    ) -> trademark_20180724_models.QueryTradeProduceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trade_produce_detail_with_options(request, runtime)

    async def query_trade_produce_detail_async(
        self,
        request: trademark_20180724_models.QueryTradeProduceDetailRequest,
    ) -> trademark_20180724_models.QueryTradeProduceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trade_produce_detail_with_options_async(request, runtime)

    def query_qr_code_upload_status_with_options(
        self,
        request: trademark_20180724_models.QueryQrCodeUploadStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryQrCodeUploadStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryQrCodeUploadStatusResponse(),
            self.do_rpcrequest('QueryQrCodeUploadStatus', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_qr_code_upload_status_with_options_async(
        self,
        request: trademark_20180724_models.QueryQrCodeUploadStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryQrCodeUploadStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryQrCodeUploadStatusResponse(),
            await self.do_rpcrequest_async('QueryQrCodeUploadStatus', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_qr_code_upload_status(
        self,
        request: trademark_20180724_models.QueryQrCodeUploadStatusRequest,
    ) -> trademark_20180724_models.QueryQrCodeUploadStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_qr_code_upload_status_with_options(request, runtime)

    async def query_qr_code_upload_status_async(
        self,
        request: trademark_20180724_models.QueryQrCodeUploadStatusRequest,
    ) -> trademark_20180724_models.QueryQrCodeUploadStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_qr_code_upload_status_with_options_async(request, runtime)

    def reject_applicant_with_options(
        self,
        request: trademark_20180724_models.RejectApplicantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.RejectApplicantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RejectApplicantResponse(),
            self.do_rpcrequest('RejectApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reject_applicant_with_options_async(
        self,
        request: trademark_20180724_models.RejectApplicantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.RejectApplicantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RejectApplicantResponse(),
            await self.do_rpcrequest_async('RejectApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reject_applicant(
        self,
        request: trademark_20180724_models.RejectApplicantRequest,
    ) -> trademark_20180724_models.RejectApplicantResponse:
        runtime = util_models.RuntimeOptions()
        return self.reject_applicant_with_options(request, runtime)

    async def reject_applicant_async(
        self,
        request: trademark_20180724_models.RejectApplicantRequest,
    ) -> trademark_20180724_models.RejectApplicantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reject_applicant_with_options_async(request, runtime)

    def query_trade_intention_user_list_with_options(
        self,
        request: trademark_20180724_models.QueryTradeIntentionUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeIntentionUserListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeIntentionUserListResponse(),
            self.do_rpcrequest('QueryTradeIntentionUserList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trade_intention_user_list_with_options_async(
        self,
        request: trademark_20180724_models.QueryTradeIntentionUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeIntentionUserListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeIntentionUserListResponse(),
            await self.do_rpcrequest_async('QueryTradeIntentionUserList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_intention_user_list(
        self,
        request: trademark_20180724_models.QueryTradeIntentionUserListRequest,
    ) -> trademark_20180724_models.QueryTradeIntentionUserListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trade_intention_user_list_with_options(request, runtime)

    async def query_trade_intention_user_list_async(
        self,
        request: trademark_20180724_models.QueryTradeIntentionUserListRequest,
    ) -> trademark_20180724_models.QueryTradeIntentionUserListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trade_intention_user_list_with_options_async(request, runtime)

    def store_material_temporarily_with_options(
        self,
        request: trademark_20180724_models.StoreMaterialTemporarilyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.StoreMaterialTemporarilyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.StoreMaterialTemporarilyResponse(),
            self.do_rpcrequest('StoreMaterialTemporarily', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def store_material_temporarily_with_options_async(
        self,
        request: trademark_20180724_models.StoreMaterialTemporarilyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.StoreMaterialTemporarilyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.StoreMaterialTemporarilyResponse(),
            await self.do_rpcrequest_async('StoreMaterialTemporarily', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def store_material_temporarily(
        self,
        request: trademark_20180724_models.StoreMaterialTemporarilyRequest,
    ) -> trademark_20180724_models.StoreMaterialTemporarilyResponse:
        runtime = util_models.RuntimeOptions()
        return self.store_material_temporarily_with_options(request, runtime)

    async def store_material_temporarily_async(
        self,
        request: trademark_20180724_models.StoreMaterialTemporarilyRequest,
    ) -> trademark_20180724_models.StoreMaterialTemporarilyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.store_material_temporarily_with_options_async(request, runtime)

    def refuse_additional_material_with_options(
        self,
        request: trademark_20180724_models.RefuseAdditionalMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.RefuseAdditionalMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefuseAdditionalMaterialResponse(),
            self.do_rpcrequest('RefuseAdditionalMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refuse_additional_material_with_options_async(
        self,
        request: trademark_20180724_models.RefuseAdditionalMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.RefuseAdditionalMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefuseAdditionalMaterialResponse(),
            await self.do_rpcrequest_async('RefuseAdditionalMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refuse_additional_material(
        self,
        request: trademark_20180724_models.RefuseAdditionalMaterialRequest,
    ) -> trademark_20180724_models.RefuseAdditionalMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.refuse_additional_material_with_options(request, runtime)

    async def refuse_additional_material_async(
        self,
        request: trademark_20180724_models.RefuseAdditionalMaterialRequest,
    ) -> trademark_20180724_models.RefuseAdditionalMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refuse_additional_material_with_options_async(request, runtime)

    def list_notary_infos_with_options(
        self,
        request: trademark_20180724_models.ListNotaryInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ListNotaryInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ListNotaryInfosResponse(),
            self.do_rpcrequest('ListNotaryInfos', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_notary_infos_with_options_async(
        self,
        request: trademark_20180724_models.ListNotaryInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ListNotaryInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ListNotaryInfosResponse(),
            await self.do_rpcrequest_async('ListNotaryInfos', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_notary_infos(
        self,
        request: trademark_20180724_models.ListNotaryInfosRequest,
    ) -> trademark_20180724_models.ListNotaryInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_notary_infos_with_options(request, runtime)

    async def list_notary_infos_async(
        self,
        request: trademark_20180724_models.ListNotaryInfosRequest,
    ) -> trademark_20180724_models.ListNotaryInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_notary_infos_with_options_async(request, runtime)

    def get_default_principal_name_with_options(
        self,
        request: trademark_20180724_models.GetDefaultPrincipalNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GetDefaultPrincipalNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetDefaultPrincipalNameResponse(),
            self.do_rpcrequest('GetDefaultPrincipalName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_default_principal_name_with_options_async(
        self,
        request: trademark_20180724_models.GetDefaultPrincipalNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GetDefaultPrincipalNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetDefaultPrincipalNameResponse(),
            await self.do_rpcrequest_async('GetDefaultPrincipalName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_default_principal_name(
        self,
        request: trademark_20180724_models.GetDefaultPrincipalNameRequest,
    ) -> trademark_20180724_models.GetDefaultPrincipalNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_principal_name_with_options(request, runtime)

    async def get_default_principal_name_async(
        self,
        request: trademark_20180724_models.GetDefaultPrincipalNameRequest,
    ) -> trademark_20180724_models.GetDefaultPrincipalNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_principal_name_with_options_async(request, runtime)

    def query_trade_mark_application_detail_with_options(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationDetailResponse(),
            self.do_rpcrequest('QueryTradeMarkApplicationDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trade_mark_application_detail_with_options_async(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationDetailResponse(),
            await self.do_rpcrequest_async('QueryTradeMarkApplicationDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_mark_application_detail(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationDetailRequest,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_application_detail_with_options(request, runtime)

    async def query_trade_mark_application_detail_async(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationDetailRequest,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trade_mark_application_detail_with_options_async(request, runtime)

    def save_classification_conditions_with_options(
        self,
        request: trademark_20180724_models.SaveClassificationConditionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SaveClassificationConditionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveClassificationConditionsResponse(),
            self.do_rpcrequest('SaveClassificationConditions', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_classification_conditions_with_options_async(
        self,
        request: trademark_20180724_models.SaveClassificationConditionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SaveClassificationConditionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveClassificationConditionsResponse(),
            await self.do_rpcrequest_async('SaveClassificationConditions', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_classification_conditions(
        self,
        request: trademark_20180724_models.SaveClassificationConditionsRequest,
    ) -> trademark_20180724_models.SaveClassificationConditionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_classification_conditions_with_options(request, runtime)

    async def save_classification_conditions_async(
        self,
        request: trademark_20180724_models.SaveClassificationConditionsRequest,
    ) -> trademark_20180724_models.SaveClassificationConditionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_classification_conditions_with_options_async(request, runtime)

    def fill_logistics_with_options(
        self,
        request: trademark_20180724_models.FillLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.FillLogisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.FillLogisticsResponse(),
            self.do_rpcrequest('FillLogistics', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fill_logistics_with_options_async(
        self,
        request: trademark_20180724_models.FillLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.FillLogisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.FillLogisticsResponse(),
            await self.do_rpcrequest_async('FillLogistics', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fill_logistics(
        self,
        request: trademark_20180724_models.FillLogisticsRequest,
    ) -> trademark_20180724_models.FillLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.fill_logistics_with_options(request, runtime)

    async def fill_logistics_async(
        self,
        request: trademark_20180724_models.FillLogisticsRequest,
    ) -> trademark_20180724_models.FillLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fill_logistics_with_options_async(request, runtime)

    def update_material_with_options(
        self,
        request: trademark_20180724_models.UpdateMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UpdateMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateMaterialResponse(),
            self.do_rpcrequest('UpdateMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_material_with_options_async(
        self,
        request: trademark_20180724_models.UpdateMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UpdateMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateMaterialResponse(),
            await self.do_rpcrequest_async('UpdateMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_material(
        self,
        request: trademark_20180724_models.UpdateMaterialRequest,
    ) -> trademark_20180724_models.UpdateMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_material_with_options(request, runtime)

    async def update_material_async(
        self,
        request: trademark_20180724_models.UpdateMaterialRequest,
    ) -> trademark_20180724_models.UpdateMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_material_with_options_async(request, runtime)

    def query_trade_mark_application_logs_with_options(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationLogsResponse(),
            self.do_rpcrequest('QueryTradeMarkApplicationLogs', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trade_mark_application_logs_with_options_async(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationLogsResponse(),
            await self.do_rpcrequest_async('QueryTradeMarkApplicationLogs', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_mark_application_logs(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationLogsRequest,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_application_logs_with_options(request, runtime)

    async def query_trade_mark_application_logs_async(
        self,
        request: trademark_20180724_models.QueryTradeMarkApplicationLogsRequest,
    ) -> trademark_20180724_models.QueryTradeMarkApplicationLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trade_mark_application_logs_with_options_async(request, runtime)

    def refund_produce_with_options(
        self,
        request: trademark_20180724_models.RefundProduceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.RefundProduceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefundProduceResponse(),
            self.do_rpcrequest('RefundProduce', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refund_produce_with_options_async(
        self,
        request: trademark_20180724_models.RefundProduceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.RefundProduceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefundProduceResponse(),
            await self.do_rpcrequest_async('RefundProduce', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_produce(
        self,
        request: trademark_20180724_models.RefundProduceRequest,
    ) -> trademark_20180724_models.RefundProduceResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_produce_with_options(request, runtime)

    async def refund_produce_async(
        self,
        request: trademark_20180724_models.RefundProduceRequest,
    ) -> trademark_20180724_models.RefundProduceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_produce_with_options_async(request, runtime)

    def sync_trademark_with_options(
        self,
        request: trademark_20180724_models.SyncTrademarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SyncTrademarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SyncTrademarkResponse(),
            self.do_rpcrequest('SyncTrademark', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_trademark_with_options_async(
        self,
        request: trademark_20180724_models.SyncTrademarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SyncTrademarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SyncTrademarkResponse(),
            await self.do_rpcrequest_async('SyncTrademark', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_trademark(
        self,
        request: trademark_20180724_models.SyncTrademarkRequest,
    ) -> trademark_20180724_models.SyncTrademarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_trademark_with_options(request, runtime)

    async def sync_trademark_async(
        self,
        request: trademark_20180724_models.SyncTrademarkRequest,
    ) -> trademark_20180724_models.SyncTrademarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_trademark_with_options_async(request, runtime)

    def combine_loa_with_options(
        self,
        request: trademark_20180724_models.CombineLoaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CombineLoaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CombineLoaResponse(),
            self.do_rpcrequest('CombineLoa', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def combine_loa_with_options_async(
        self,
        request: trademark_20180724_models.CombineLoaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CombineLoaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CombineLoaResponse(),
            await self.do_rpcrequest_async('CombineLoa', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def combine_loa(
        self,
        request: trademark_20180724_models.CombineLoaRequest,
    ) -> trademark_20180724_models.CombineLoaResponse:
        runtime = util_models.RuntimeOptions()
        return self.combine_loa_with_options(request, runtime)

    async def combine_loa_async(
        self,
        request: trademark_20180724_models.CombineLoaRequest,
    ) -> trademark_20180724_models.CombineLoaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.combine_loa_with_options_async(request, runtime)

    def filter_unavailable_codes_with_options(
        self,
        tmp_req: trademark_20180724_models.FilterUnavailableCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.FilterUnavailableCodesResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.FilterUnavailableCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.codes):
            request.codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.FilterUnavailableCodesResponse(),
            self.do_rpcrequest('FilterUnavailableCodes', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def filter_unavailable_codes_with_options_async(
        self,
        tmp_req: trademark_20180724_models.FilterUnavailableCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.FilterUnavailableCodesResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.FilterUnavailableCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.codes):
            request.codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.FilterUnavailableCodesResponse(),
            await self.do_rpcrequest_async('FilterUnavailableCodes', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def filter_unavailable_codes(
        self,
        request: trademark_20180724_models.FilterUnavailableCodesRequest,
    ) -> trademark_20180724_models.FilterUnavailableCodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.filter_unavailable_codes_with_options(request, runtime)

    async def filter_unavailable_codes_async(
        self,
        request: trademark_20180724_models.FilterUnavailableCodesRequest,
    ) -> trademark_20180724_models.FilterUnavailableCodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.filter_unavailable_codes_with_options_async(request, runtime)

    def insert_material_with_options(
        self,
        request: trademark_20180724_models.InsertMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.InsertMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertMaterialResponse(),
            self.do_rpcrequest('InsertMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_material_with_options_async(
        self,
        request: trademark_20180724_models.InsertMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.InsertMaterialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertMaterialResponse(),
            await self.do_rpcrequest_async('InsertMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_material(
        self,
        request: trademark_20180724_models.InsertMaterialRequest,
    ) -> trademark_20180724_models.InsertMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_material_with_options(request, runtime)

    async def insert_material_async(
        self,
        request: trademark_20180724_models.InsertMaterialRequest,
    ) -> trademark_20180724_models.InsertMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_material_with_options_async(request, runtime)

    def save_trade_mark_review_material_detail_with_options(
        self,
        tmp_req: trademark_20180724_models.SaveTradeMarkReviewMaterialDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SaveTradeMarkReviewMaterialDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SaveTradeMarkReviewMaterialDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_oss_key_list):
            request.additional_oss_key_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_oss_key_list, 'AdditionalOssKeyList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTradeMarkReviewMaterialDetailResponse(),
            self.do_rpcrequest('SaveTradeMarkReviewMaterialDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_trade_mark_review_material_detail_with_options_async(
        self,
        tmp_req: trademark_20180724_models.SaveTradeMarkReviewMaterialDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.SaveTradeMarkReviewMaterialDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SaveTradeMarkReviewMaterialDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_oss_key_list):
            request.additional_oss_key_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_oss_key_list, 'AdditionalOssKeyList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTradeMarkReviewMaterialDetailResponse(),
            await self.do_rpcrequest_async('SaveTradeMarkReviewMaterialDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_trade_mark_review_material_detail(
        self,
        request: trademark_20180724_models.SaveTradeMarkReviewMaterialDetailRequest,
    ) -> trademark_20180724_models.SaveTradeMarkReviewMaterialDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_trade_mark_review_material_detail_with_options(request, runtime)

    async def save_trade_mark_review_material_detail_async(
        self,
        request: trademark_20180724_models.SaveTradeMarkReviewMaterialDetailRequest,
    ) -> trademark_20180724_models.SaveTradeMarkReviewMaterialDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_trade_mark_review_material_detail_with_options_async(request, runtime)

    def query_monitor_keywords_with_options(
        self,
        request: trademark_20180724_models.QueryMonitorKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryMonitorKeywordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMonitorKeywordsResponse(),
            self.do_rpcrequest('QueryMonitorKeywords', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_monitor_keywords_with_options_async(
        self,
        request: trademark_20180724_models.QueryMonitorKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryMonitorKeywordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMonitorKeywordsResponse(),
            await self.do_rpcrequest_async('QueryMonitorKeywords', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_monitor_keywords(
        self,
        request: trademark_20180724_models.QueryMonitorKeywordsRequest,
    ) -> trademark_20180724_models.QueryMonitorKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_monitor_keywords_with_options(request, runtime)

    async def query_monitor_keywords_async(
        self,
        request: trademark_20180724_models.QueryMonitorKeywordsRequest,
    ) -> trademark_20180724_models.QueryMonitorKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_monitor_keywords_with_options_async(request, runtime)

    def query_task_list_with_options(
        self,
        request: trademark_20180724_models.QueryTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTaskListResponse(),
            self.do_rpcrequest('QueryTaskList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_task_list_with_options_async(
        self,
        request: trademark_20180724_models.QueryTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTaskListResponse(),
            await self.do_rpcrequest_async('QueryTaskList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_task_list(
        self,
        request: trademark_20180724_models.QueryTaskListRequest,
    ) -> trademark_20180724_models.QueryTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_task_list_with_options(request, runtime)

    async def query_task_list_async(
        self,
        request: trademark_20180724_models.QueryTaskListRequest,
    ) -> trademark_20180724_models.QueryTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_task_list_with_options_async(request, runtime)

    def update_trademark_name_with_options(
        self,
        request: trademark_20180724_models.UpdateTrademarkNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UpdateTrademarkNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateTrademarkNameResponse(),
            self.do_rpcrequest('UpdateTrademarkName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_trademark_name_with_options_async(
        self,
        request: trademark_20180724_models.UpdateTrademarkNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UpdateTrademarkNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateTrademarkNameResponse(),
            await self.do_rpcrequest_async('UpdateTrademarkName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_trademark_name(
        self,
        request: trademark_20180724_models.UpdateTrademarkNameRequest,
    ) -> trademark_20180724_models.UpdateTrademarkNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_trademark_name_with_options(request, runtime)

    async def update_trademark_name_async(
        self,
        request: trademark_20180724_models.UpdateTrademarkNameRequest,
    ) -> trademark_20180724_models.UpdateTrademarkNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_trademark_name_with_options_async(request, runtime)

    def check_loa_fill_with_options(
        self,
        request: trademark_20180724_models.CheckLoaFillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CheckLoaFillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckLoaFillResponse(),
            self.do_rpcrequest('CheckLoaFill', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_loa_fill_with_options_async(
        self,
        request: trademark_20180724_models.CheckLoaFillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CheckLoaFillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckLoaFillResponse(),
            await self.do_rpcrequest_async('CheckLoaFill', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_loa_fill(
        self,
        request: trademark_20180724_models.CheckLoaFillRequest,
    ) -> trademark_20180724_models.CheckLoaFillResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_loa_fill_with_options(request, runtime)

    async def check_loa_fill_async(
        self,
        request: trademark_20180724_models.CheckLoaFillRequest,
    ) -> trademark_20180724_models.CheckLoaFillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_loa_fill_with_options_async(request, runtime)

    def confirm_applicant_with_options(
        self,
        request: trademark_20180724_models.ConfirmApplicantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ConfirmApplicantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmApplicantResponse(),
            self.do_rpcrequest('ConfirmApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def confirm_applicant_with_options_async(
        self,
        request: trademark_20180724_models.ConfirmApplicantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ConfirmApplicantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmApplicantResponse(),
            await self.do_rpcrequest_async('ConfirmApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def confirm_applicant(
        self,
        request: trademark_20180724_models.ConfirmApplicantRequest,
    ) -> trademark_20180724_models.ConfirmApplicantResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_applicant_with_options(request, runtime)

    async def confirm_applicant_async(
        self,
        request: trademark_20180724_models.ConfirmApplicantRequest,
    ) -> trademark_20180724_models.ConfirmApplicantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_applicant_with_options_async(request, runtime)

    def create_intention_order_with_options(
        self,
        request: trademark_20180724_models.CreateIntentionOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CreateIntentionOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateIntentionOrderResponse(),
            self.do_rpcrequest('CreateIntentionOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_intention_order_with_options_async(
        self,
        request: trademark_20180724_models.CreateIntentionOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CreateIntentionOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateIntentionOrderResponse(),
            await self.do_rpcrequest_async('CreateIntentionOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_intention_order(
        self,
        request: trademark_20180724_models.CreateIntentionOrderRequest,
    ) -> trademark_20180724_models.CreateIntentionOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_intention_order_with_options(request, runtime)

    async def create_intention_order_async(
        self,
        request: trademark_20180724_models.CreateIntentionOrderRequest,
    ) -> trademark_20180724_models.CreateIntentionOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_intention_order_with_options_async(request, runtime)

    def query_oss_resources_with_options(
        self,
        request: trademark_20180724_models.QueryOssResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryOssResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryOssResourcesResponse(),
            self.do_rpcrequest('QueryOssResources', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_oss_resources_with_options_async(
        self,
        request: trademark_20180724_models.QueryOssResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.QueryOssResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryOssResourcesResponse(),
            await self.do_rpcrequest_async('QueryOssResources', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_oss_resources(
        self,
        request: trademark_20180724_models.QueryOssResourcesRequest,
    ) -> trademark_20180724_models.QueryOssResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_oss_resources_with_options(request, runtime)

    async def query_oss_resources_async(
        self,
        request: trademark_20180724_models.QueryOssResourcesRequest,
    ) -> trademark_20180724_models.QueryOssResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_oss_resources_with_options_async(request, runtime)

    def refuse_applicant_with_options(
        self,
        request: trademark_20180724_models.RefuseApplicantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.RefuseApplicantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefuseApplicantResponse(),
            self.do_rpcrequest('RefuseApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refuse_applicant_with_options_async(
        self,
        request: trademark_20180724_models.RefuseApplicantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.RefuseApplicantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefuseApplicantResponse(),
            await self.do_rpcrequest_async('RefuseApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refuse_applicant(
        self,
        request: trademark_20180724_models.RefuseApplicantRequest,
    ) -> trademark_20180724_models.RefuseApplicantResponse:
        runtime = util_models.RuntimeOptions()
        return self.refuse_applicant_with_options(request, runtime)

    async def refuse_applicant_async(
        self,
        request: trademark_20180724_models.RefuseApplicantRequest,
    ) -> trademark_20180724_models.RefuseApplicantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refuse_applicant_with_options_async(request, runtime)

    def create_intention_order_generating_pay_with_options(
        self,
        request: trademark_20180724_models.CreateIntentionOrderGeneratingPayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CreateIntentionOrderGeneratingPayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateIntentionOrderGeneratingPayResponse(),
            self.do_rpcrequest('CreateIntentionOrderGeneratingPay', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_intention_order_generating_pay_with_options_async(
        self,
        request: trademark_20180724_models.CreateIntentionOrderGeneratingPayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.CreateIntentionOrderGeneratingPayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateIntentionOrderGeneratingPayResponse(),
            await self.do_rpcrequest_async('CreateIntentionOrderGeneratingPay', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_intention_order_generating_pay(
        self,
        request: trademark_20180724_models.CreateIntentionOrderGeneratingPayRequest,
    ) -> trademark_20180724_models.CreateIntentionOrderGeneratingPayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_intention_order_generating_pay_with_options(request, runtime)

    async def create_intention_order_generating_pay_async(
        self,
        request: trademark_20180724_models.CreateIntentionOrderGeneratingPayRequest,
    ) -> trademark_20180724_models.CreateIntentionOrderGeneratingPayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_intention_order_generating_pay_with_options_async(request, runtime)

    def list_notary_orders_with_options(
        self,
        request: trademark_20180724_models.ListNotaryOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ListNotaryOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ListNotaryOrdersResponse(),
            self.do_rpcrequest('ListNotaryOrders', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_notary_orders_with_options_async(
        self,
        request: trademark_20180724_models.ListNotaryOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.ListNotaryOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ListNotaryOrdersResponse(),
            await self.do_rpcrequest_async('ListNotaryOrders', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_notary_orders(
        self,
        request: trademark_20180724_models.ListNotaryOrdersRequest,
    ) -> trademark_20180724_models.ListNotaryOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_notary_orders_with_options(request, runtime)

    async def list_notary_orders_async(
        self,
        request: trademark_20180724_models.ListNotaryOrdersRequest,
    ) -> trademark_20180724_models.ListNotaryOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_notary_orders_with_options_async(request, runtime)

    def get_support_principal_name_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GetSupportPrincipalNameResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            trademark_20180724_models.GetSupportPrincipalNameResponse(),
            self.do_rpcrequest('GetSupportPrincipalName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_support_principal_name_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.GetSupportPrincipalNameResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            trademark_20180724_models.GetSupportPrincipalNameResponse(),
            await self.do_rpcrequest_async('GetSupportPrincipalName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_support_principal_name(self) -> trademark_20180724_models.GetSupportPrincipalNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_support_principal_name_with_options(runtime)

    async def get_support_principal_name_async(self) -> trademark_20180724_models.GetSupportPrincipalNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_support_principal_name_with_options_async(runtime)

    def start_notary_with_options(
        self,
        request: trademark_20180724_models.StartNotaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.StartNotaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.StartNotaryResponse(),
            self.do_rpcrequest('StartNotary', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_notary_with_options_async(
        self,
        request: trademark_20180724_models.StartNotaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.StartNotaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.StartNotaryResponse(),
            await self.do_rpcrequest_async('StartNotary', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_notary(
        self,
        request: trademark_20180724_models.StartNotaryRequest,
    ) -> trademark_20180724_models.StartNotaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_notary_with_options(request, runtime)

    async def start_notary_async(
        self,
        request: trademark_20180724_models.StartNotaryRequest,
    ) -> trademark_20180724_models.StartNotaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_notary_with_options_async(request, runtime)

    def update_send_material_num_with_options(
        self,
        request: trademark_20180724_models.UpdateSendMaterialNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UpdateSendMaterialNumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateSendMaterialNumResponse(),
            self.do_rpcrequest('UpdateSendMaterialNum', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_send_material_num_with_options_async(
        self,
        request: trademark_20180724_models.UpdateSendMaterialNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.UpdateSendMaterialNumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateSendMaterialNumResponse(),
            await self.do_rpcrequest_async('UpdateSendMaterialNum', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_send_material_num(
        self,
        request: trademark_20180724_models.UpdateSendMaterialNumRequest,
    ) -> trademark_20180724_models.UpdateSendMaterialNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_send_material_num_with_options(request, runtime)

    async def update_send_material_num_async(
        self,
        request: trademark_20180724_models.UpdateSendMaterialNumRequest,
    ) -> trademark_20180724_models.UpdateSendMaterialNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_send_material_num_with_options_async(request, runtime)

    def delete_trademark_application_with_options(
        self,
        request: trademark_20180724_models.DeleteTrademarkApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.DeleteTrademarkApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteTrademarkApplicationResponse(),
            self.do_rpcrequest('DeleteTrademarkApplication', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_trademark_application_with_options_async(
        self,
        request: trademark_20180724_models.DeleteTrademarkApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> trademark_20180724_models.DeleteTrademarkApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteTrademarkApplicationResponse(),
            await self.do_rpcrequest_async('DeleteTrademarkApplication', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_trademark_application(
        self,
        request: trademark_20180724_models.DeleteTrademarkApplicationRequest,
    ) -> trademark_20180724_models.DeleteTrademarkApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_trademark_application_with_options(request, runtime)

    async def delete_trademark_application_async(
        self,
        request: trademark_20180724_models.DeleteTrademarkApplicationRequest,
    ) -> trademark_20180724_models.DeleteTrademarkApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_trademark_application_with_options_async(request, runtime)
