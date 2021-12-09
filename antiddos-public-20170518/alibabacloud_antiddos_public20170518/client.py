# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_antiddos_public20170518 import models as antiddos_public_20170518_models
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
        query = {}
        query['DdosRegionId'] = request.ddos_region_id
        query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBgpPackByIp',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeBgpPackByIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bgp_pack_by_ip_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackByIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeBgpPackByIpResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DdosRegionId'] = request.ddos_region_id
        query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBgpPackByIp',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeBgpPackByIpResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_cap_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeCapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeCapResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BegTime'] = request.beg_time
        query['DdosRegionId'] = request.ddos_region_id
        query['InstanceId'] = request.instance_id
        query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCap',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeCapResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cap_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeCapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeCapResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BegTime'] = request.beg_time
        query['DdosRegionId'] = request.ddos_region_id
        query['InstanceId'] = request.instance_id
        query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCap',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeCapResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_ddos_count_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DdosRegionId'] = request.ddos_region_id
        query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDdosCount',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_count_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DdosRegionId'] = request.ddos_region_id
        query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDdosCount',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosCountResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['DdosRegionId'] = request.ddos_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDdosCredit',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosCreditResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_credit_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCreditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCreditResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DdosRegionId'] = request.ddos_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDdosCredit',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosCreditResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CurrentPage'] = request.current_page
        query['DdosRegionId'] = request.ddos_region_id
        query['InstanceId'] = request.instance_id
        query['InstanceType'] = request.instance_type
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDdosEventList',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_list_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DdosRegionId'] = request.ddos_region_id
        query['InstanceId'] = request.instance_id
        query['InstanceType'] = request.instance_type
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDdosEventList',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosEventListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['DdosRegionId'] = request.ddos_region_id
        query['DdosType'] = request.ddos_type
        query['InstanceIds'] = request.instance_ids
        query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDdosThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_threshold_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosThresholdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DdosRegionId'] = request.ddos_region_id
        query['DdosType'] = request.ddos_type
        query['InstanceIds'] = request.instance_ids
        query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDdosThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosThresholdResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_instance_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DdosRegionId'] = request.ddos_region_id
        query['DdosStatus'] = request.ddos_status
        query['InstanceId'] = request.instance_id
        query['InstanceIp'] = request.instance_ip
        query['InstanceName'] = request.instance_name
        query['InstanceType'] = request.instance_type
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DdosRegionId'] = request.ddos_region_id
        query['DdosStatus'] = request.ddos_status
        query['InstanceId'] = request.instance_id
        query['InstanceIp'] = request.instance_ip
        query['InstanceName'] = request.instance_name
        query['InstanceType'] = request.instance_type
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceRequest,
    ) -> antiddos_public_20170518_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceRequest,
    ) -> antiddos_public_20170518_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def modify_ddos_status_with_options(
        self,
        request: antiddos_public_20170518_models.ModifyDdosStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyDdosStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DdosRegionId'] = request.ddos_region_id
        query['InstanceId'] = request.instance_id
        query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDdosStatus',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.ModifyDdosStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ddos_status_with_options_async(
        self,
        request: antiddos_public_20170518_models.ModifyDdosStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyDdosStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DdosRegionId'] = request.ddos_region_id
        query['InstanceId'] = request.instance_id
        query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDdosStatus',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.ModifyDdosStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Bps'] = request.bps
        query['DdosRegionId'] = request.ddos_region_id
        query['InstanceId'] = request.instance_id
        query['InstanceType'] = request.instance_type
        query['IsAuto'] = request.is_auto
        query['Pps'] = request.pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDefenseThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.ModifyDefenseThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_threshold_with_options_async(
        self,
        request: antiddos_public_20170518_models.ModifyDefenseThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyDefenseThresholdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bps'] = request.bps
        query['DdosRegionId'] = request.ddos_region_id
        query['InstanceId'] = request.instance_id
        query['InstanceType'] = request.instance_type
        query['IsAuto'] = request.is_auto
        query['Pps'] = request.pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDefenseThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.ModifyDefenseThresholdResponse(),
            await self.call_api_async(params, req, runtime)
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
