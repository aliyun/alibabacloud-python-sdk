# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_antiddos_public20170518 import models as antiddos_public_20170518_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('antiddos-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_bgp_pack_by_ip_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackByIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeBgpPackByIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeBgpPackByIpResponse().from_map(
            self.do_rpcrequest('DescribeBgpPackByIp', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bgp_pack_by_ip_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackByIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeBgpPackByIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeBgpPackByIpResponse().from_map(
            await self.do_rpcrequest_async('DescribeBgpPackByIp', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bgp_pack_by_ip(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackByIpRequest,
    ) -> antiddos_public_20170518_models.DescribeBgpPackByIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bgp_pack_by_ip_with_options(request, runtime)

    async def describe_bgp_pack_by_ip_async(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackByIpRequest,
    ) -> antiddos_public_20170518_models.DescribeBgpPackByIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bgp_pack_by_ip_with_options_async(request, runtime)

    def describe_bgp_pack_elastic_threshold_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackElasticThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeBgpPackElasticThresholdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeBgpPackElasticThresholdResponse().from_map(
            self.do_rpcrequest('DescribeBgpPackElasticThreshold', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bgp_pack_elastic_threshold_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackElasticThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeBgpPackElasticThresholdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeBgpPackElasticThresholdResponse().from_map(
            await self.do_rpcrequest_async('DescribeBgpPackElasticThreshold', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bgp_pack_elastic_threshold(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackElasticThresholdRequest,
    ) -> antiddos_public_20170518_models.DescribeBgpPackElasticThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bgp_pack_elastic_threshold_with_options(request, runtime)

    async def describe_bgp_pack_elastic_threshold_async(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackElasticThresholdRequest,
    ) -> antiddos_public_20170518_models.DescribeBgpPackElasticThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bgp_pack_elastic_threshold_with_options_async(request, runtime)

    def describe_cap_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeCapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeCapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeCapResponse().from_map(
            self.do_rpcrequest('DescribeCap', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cap_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeCapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeCapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeCapResponse().from_map(
            await self.do_rpcrequest_async('DescribeCap', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cap(
        self,
        request: antiddos_public_20170518_models.DescribeCapRequest,
    ) -> antiddos_public_20170518_models.DescribeCapResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cap_with_options(request, runtime)

    async def describe_cap_async(
        self,
        request: antiddos_public_20170518_models.DescribeCapRequest,
    ) -> antiddos_public_20170518_models.DescribeCapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cap_with_options_async(request, runtime)

    def describe_credit_info_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeCreditInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeCreditInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeCreditInfoResponse().from_map(
            self.do_rpcrequest('DescribeCreditInfo', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_credit_info_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeCreditInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeCreditInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeCreditInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeCreditInfo', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_credit_info(
        self,
        request: antiddos_public_20170518_models.DescribeCreditInfoRequest,
    ) -> antiddos_public_20170518_models.DescribeCreditInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_credit_info_with_options(request, runtime)

    async def describe_credit_info_async(
        self,
        request: antiddos_public_20170518_models.DescribeCreditInfoRequest,
    ) -> antiddos_public_20170518_models.DescribeCreditInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_credit_info_with_options_async(request, runtime)

    def describe_ddos_count_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeDdosCountResponse().from_map(
            self.do_rpcrequest('DescribeDdosCount', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_count_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeDdosCountResponse().from_map(
            await self.do_rpcrequest_async('DescribeDdosCount', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_count(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCountRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_count_with_options(request, runtime)

    async def describe_ddos_count_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCountRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_count_with_options_async(request, runtime)

    def describe_ddos_credit_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCreditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCreditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeDdosCreditResponse().from_map(
            self.do_rpcrequest('DescribeDdosCredit', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_credit_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCreditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCreditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeDdosCreditResponse().from_map(
            await self.do_rpcrequest_async('DescribeDdosCredit', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_credit(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCreditRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosCreditResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_credit_with_options(request, runtime)

    async def describe_ddos_credit_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCreditRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosCreditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_credit_with_options_async(request, runtime)

    def describe_ddos_event_list_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeDdosEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosEventListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeDdosEventListResponse().from_map(
            self.do_rpcrequest('DescribeDdosEventList', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_event_list_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosEventListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeDdosEventListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDdosEventList', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_list(
        self,
        request: antiddos_public_20170518_models.DescribeDdosEventListRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosEventListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_list_with_options(request, runtime)

    async def describe_ddos_event_list_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosEventListRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosEventListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_list_with_options_async(request, runtime)

    def describe_ddos_threshold_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeDdosThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosThresholdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeDdosThresholdResponse().from_map(
            self.do_rpcrequest('DescribeDdosThreshold', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ddos_threshold_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosThresholdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeDdosThresholdResponse().from_map(
            await self.do_rpcrequest_async('DescribeDdosThreshold', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_threshold(
        self,
        request: antiddos_public_20170518_models.DescribeDdosThresholdRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_threshold_with_options(request, runtime)

    async def describe_ddos_threshold_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosThresholdRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_threshold_with_options_async(request, runtime)

    def describe_flexible_protection_flow_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeFlexibleProtectionFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeFlexibleProtectionFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeFlexibleProtectionFlowResponse().from_map(
            self.do_rpcrequest('DescribeFlexibleProtectionFlow', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flexible_protection_flow_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeFlexibleProtectionFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeFlexibleProtectionFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeFlexibleProtectionFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlexibleProtectionFlow', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flexible_protection_flow(
        self,
        request: antiddos_public_20170518_models.DescribeFlexibleProtectionFlowRequest,
    ) -> antiddos_public_20170518_models.DescribeFlexibleProtectionFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flexible_protection_flow_with_options(request, runtime)

    async def describe_flexible_protection_flow_async(
        self,
        request: antiddos_public_20170518_models.DescribeFlexibleProtectionFlowRequest,
    ) -> antiddos_public_20170518_models.DescribeFlexibleProtectionFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flexible_protection_flow_with_options_async(request, runtime)

    def describe_flowgraph_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeFlowgraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeFlowgraphResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeFlowgraphResponse().from_map(
            self.do_rpcrequest('DescribeFlowgraph', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flowgraph_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeFlowgraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeFlowgraphResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeFlowgraphResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowgraph', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flowgraph(
        self,
        request: antiddos_public_20170518_models.DescribeFlowgraphRequest,
    ) -> antiddos_public_20170518_models.DescribeFlowgraphResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flowgraph_with_options(request, runtime)

    async def describe_flowgraph_async(
        self,
        request: antiddos_public_20170518_models.DescribeFlowgraphRequest,
    ) -> antiddos_public_20170518_models.DescribeFlowgraphResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flowgraph_with_options_async(request, runtime)

    def describe_region_ddos_threshold_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeRegionDdosThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeRegionDdosThresholdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeRegionDdosThresholdResponse().from_map(
            self.do_rpcrequest('DescribeRegionDdosThreshold', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_region_ddos_threshold_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeRegionDdosThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeRegionDdosThresholdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeRegionDdosThresholdResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegionDdosThreshold', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_region_ddos_threshold(
        self,
        request: antiddos_public_20170518_models.DescribeRegionDdosThresholdRequest,
    ) -> antiddos_public_20170518_models.DescribeRegionDdosThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_region_ddos_threshold_with_options(request, runtime)

    async def describe_region_ddos_threshold_async(
        self,
        request: antiddos_public_20170518_models.DescribeRegionDdosThresholdRequest,
    ) -> antiddos_public_20170518_models.DescribeRegionDdosThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_region_ddos_threshold_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: antiddos_public_20170518_models.DescribeRegionsRequest,
    ) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: antiddos_public_20170518_models.DescribeRegionsRequest,
    ) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_traffic_info_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeTrafficInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeTrafficInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeTrafficInfoResponse().from_map(
            self.do_rpcrequest('DescribeTrafficInfo', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_traffic_info_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeTrafficInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeTrafficInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.DescribeTrafficInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeTrafficInfo', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_traffic_info(
        self,
        request: antiddos_public_20170518_models.DescribeTrafficInfoRequest,
    ) -> antiddos_public_20170518_models.DescribeTrafficInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_info_with_options(request, runtime)

    async def describe_traffic_info_async(
        self,
        request: antiddos_public_20170518_models.DescribeTrafficInfoRequest,
    ) -> antiddos_public_20170518_models.DescribeTrafficInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_traffic_info_with_options_async(request, runtime)

    def modify_ddos_status_with_options(
        self,
        request: antiddos_public_20170518_models.ModifyDdosStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyDdosStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.ModifyDdosStatusResponse().from_map(
            self.do_rpcrequest('ModifyDdosStatus', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ddos_status_with_options_async(
        self,
        request: antiddos_public_20170518_models.ModifyDdosStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyDdosStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.ModifyDdosStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyDdosStatus', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ddos_status(
        self,
        request: antiddos_public_20170518_models.ModifyDdosStatusRequest,
    ) -> antiddos_public_20170518_models.ModifyDdosStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ddos_status_with_options(request, runtime)

    async def modify_ddos_status_async(
        self,
        request: antiddos_public_20170518_models.ModifyDdosStatusRequest,
    ) -> antiddos_public_20170518_models.ModifyDdosStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ddos_status_with_options_async(request, runtime)

    def modify_defense_threshold_with_options(
        self,
        request: antiddos_public_20170518_models.ModifyDefenseThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyDefenseThresholdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.ModifyDefenseThresholdResponse().from_map(
            self.do_rpcrequest('ModifyDefenseThreshold', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_defense_threshold_with_options_async(
        self,
        request: antiddos_public_20170518_models.ModifyDefenseThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyDefenseThresholdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return antiddos_public_20170518_models.ModifyDefenseThresholdResponse().from_map(
            await self.do_rpcrequest_async('ModifyDefenseThreshold', '2017-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_defense_threshold(
        self,
        request: antiddos_public_20170518_models.ModifyDefenseThresholdRequest,
    ) -> antiddos_public_20170518_models.ModifyDefenseThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_threshold_with_options(request, runtime)

    async def modify_defense_threshold_async(
        self,
        request: antiddos_public_20170518_models.ModifyDefenseThresholdRequest,
    ) -> antiddos_public_20170518_models.ModifyDefenseThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_threshold_with_options_async(request, runtime)
