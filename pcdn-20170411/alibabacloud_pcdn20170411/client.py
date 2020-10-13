# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_pcdn20170411 import models as pcdn_20170411_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "central"
        self.check_config(config)
        self._endpoint = self.get_endpoint("pcdn", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def stop_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.StopDomainResponse().from_map(self.do_request("StopDomain", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def stop_domain(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.stop_domain_with_options(request, runtime)

    def start_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.StartDomainResponse().from_map(self.do_request("StartDomain", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def start_domain(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.start_domain_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.DeleteDomainResponse().from_map(self.do_request("DeleteDomain", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def delete_domain(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_domain_with_options(request, runtime)

    def add_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.AddDomainResponse().from_map(self.do_request("AddDomain", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def add_domain(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.add_domain_with_options(request, runtime)

    def get_balance_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetBalanceTrafficDataResponse().from_map(self.do_request("GetBalanceTrafficData", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_balance_traffic_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_balance_traffic_data_with_options(request, runtime)

    def add_pcdn_control_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.AddPcdnControlRuleResponse().from_map(self.do_request("AddPcdnControlRule", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def add_pcdn_control_rule(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.add_pcdn_control_rule_with_options(request, runtime)

    def add_consumer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.AddConsumerResponse().from_map(self.do_request("AddConsumer", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def add_consumer(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.add_consumer_with_options(request, runtime)

    def get_access_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAccessDataResponse().from_map(self.do_request("GetAccessData", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_access_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_access_data_with_options(request, runtime)

    def enable_pcdn_control_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.EnablePcdnControlRuleResponse().from_map(self.do_request("EnablePcdnControlRule", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def enable_pcdn_control_rule(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.enable_pcdn_control_rule_with_options(request, runtime)

    def edit_pcdn_control_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.EditPcdnControlRuleResponse().from_map(self.do_request("EditPcdnControlRule", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def edit_pcdn_control_rule(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.edit_pcdn_control_rule_with_options(request, runtime)

    def disable_pcdn_control_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.DisablePcdnControlRuleResponse().from_map(self.do_request("DisablePcdnControlRule", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def disable_pcdn_control_rule(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.disable_pcdn_control_rule_with_options(request, runtime)

    def delete_pcdn_control_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.DeletePcdnControlRuleResponse().from_map(self.do_request("DeletePcdnControlRule", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def delete_pcdn_control_rule(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_pcdn_control_rule_with_options(request, runtime)

    def get_all_platform_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllPlatformTypesResponse().from_map(self.do_request("GetAllPlatformTypes", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_all_platform_types(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_all_platform_types_with_options(request, runtime)

    def get_all_markets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllMarketsResponse().from_map(self.do_request("GetAllMarkets", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_all_markets(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_all_markets_with_options(request, runtime)

    def get_all_isp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllIspResponse().from_map(self.do_request("GetAllIsp", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_all_isp(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_all_isp_with_options(request, runtime)

    def get_all_app_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllAppVersionsResponse().from_map(self.do_request("GetAllAppVersions", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_all_app_versions(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_all_app_versions_with_options(request, runtime)

    def get_consumer_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetConsumerStatusResponse().from_map(self.do_request("GetConsumerStatus", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_consumer_status(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_consumer_status_with_options(request, runtime)

    def get_clients_ratio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetClientsRatioResponse().from_map(self.do_request("GetClientsRatio", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_clients_ratio(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_clients_ratio_with_options(request, runtime)

    def get_bandwidth_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetBandwidthDataResponse().from_map(self.do_request("GetBandwidthData", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_bandwidth_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_bandwidth_data_with_options(request, runtime)

    def get_balance_bandwidth_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetBalanceBandwidthDataResponse().from_map(self.do_request("GetBalanceBandwidthData", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_balance_bandwidth_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_balance_bandwidth_data_with_options(request, runtime)

    def get_control_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetControlRulesResponse().from_map(self.do_request("GetControlRules", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_control_rules(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_control_rules_with_options(request, runtime)

    def get_domain_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetDomainCountResponse().from_map(self.do_request("GetDomainCount", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_domain_count(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_domain_count_with_options(request, runtime)

    def get_current_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetCurrentModeResponse().from_map(self.do_request("GetCurrentMode", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_current_mode(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_current_mode_with_options(request, runtime)

    def get_cover_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetCoverRateDataResponse().from_map(self.do_request("GetCoverRateData", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_cover_rate_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_cover_rate_data_with_options(request, runtime)

    def get_fee_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetFeeHistoryResponse().from_map(self.do_request("GetFeeHistory", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_fee_history(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_fee_history_with_options(request, runtime)

    def get_expense_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetExpenseSummaryResponse().from_map(self.do_request("GetExpenseSummary", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_expense_summary(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_expense_summary_with_options(request, runtime)

    def get_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetDomainsResponse().from_map(self.do_request("GetDomains", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_domains(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_domains_with_options(request, runtime)

    def get_logs_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetLogsListResponse().from_map(self.do_request("GetLogsList", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_logs_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_logs_list_with_options(request, runtime)

    def get_fluency_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetFluencyDataResponse().from_map(self.do_request("GetFluencyData", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_fluency_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_fluency_data_with_options(request, runtime)

    def get_first_frame_delay_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetFirstFrameDelayDataResponse().from_map(self.do_request("GetFirstFrameDelayData", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_first_frame_delay_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_first_frame_delay_data_with_options(request, runtime)

    def get_token_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetTokenListResponse().from_map(self.do_request("GetTokenList", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_token_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_token_list_with_options(request, runtime)

    def get_share_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetShareRateDataResponse().from_map(self.do_request("GetShareRateData", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_share_rate_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_share_rate_data_with_options(request, runtime)

    def get_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetTrafficDataResponse().from_map(self.do_request("GetTrafficData", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_traffic_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_traffic_data_with_options(request, runtime)

    def get_traffic_by_region_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetTrafficByRegionResponse().from_map(self.do_request("GetTrafficByRegion", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_traffic_by_region(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_traffic_by_region_with_options(request, runtime)

    def get_all_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return pcdn_20170411_models.GetAllRegionsResponse().from_map(self.do_request("GetAllRegions", "HTTPS", "GET", "2017-04-11", "AK", request.to_map(), None, runtime))

    def get_all_regions(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_all_regions_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
