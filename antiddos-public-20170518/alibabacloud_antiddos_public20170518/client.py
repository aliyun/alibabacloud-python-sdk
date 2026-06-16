# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_antiddos_public20170518 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'antiddos.aliyuncs.com',
            'cn-beijing': 'antiddos.aliyuncs.com',
            'cn-zhangjiakou': 'antiddos-openapi.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'antiddos-openapi.cn-huhehaote.aliyuncs.com',
            'cn-wulanchabu': 'antiddos-openapi.cn-wulanchabu.aliyuncs.com',
            'cn-hangzhou': 'antiddos.aliyuncs.com',
            'cn-shanghai': 'antiddos.aliyuncs.com',
            'cn-nanjing': 'antiddos-openapi.cn-hangzhou-cloudstone.aliyuncs.com',
            'cn-shenzhen': 'antiddos.aliyuncs.com',
            'cn-heyuan': 'antiddos-openapi.cn-heyuan.aliyuncs.com',
            'cn-guangzhou': 'antiddos-openapi.cn-guangzhou.aliyuncs.com',
            'cn-chengdu': 'antiddos-openapi.cn-chengdu.aliyuncs.com',
            'cn-hongkong': 'antiddos.aliyuncs.com',
            'ap-northeast-1': 'antiddos-openapi.ap-northeast-1.aliyuncs.com',
            'ap-northeast-2': 'antiddos-openapi.ap-northeast-2.aliyuncs.com',
            'ap-southeast-1': 'antiddos.aliyuncs.com',
            'ap-southeast-2': 'antiddos-openapi.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'antiddos-openapi.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'antiddos-openapi.ap-southeast-5.aliyuncs.com',
            'ap-southeast-6': 'antiddos-openapi.ap-southeast-6.aliyuncs.com',
            'us-east-1': 'antiddos.aliyuncs.com',
            'us-west-1': 'antiddos.aliyuncs.com',
            'eu-west-1': 'antiddos-openapi.eu-west-1.aliyuncs.com',
            'eu-central-1': 'antiddos-openapi.eu-central-1.aliyuncs.com',
            'ap-south-1': 'antiddos-openapi.ap-south-1.aliyuncs.com',
            'me-east-1': 'antiddos-openapi.me-east-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'antiddos.aliyuncs.com',
            'cn-shenzhen-finance-1': 'antiddos.aliyuncs.com',
            'cn-north-2-gov-1': 'antiddos.aliyuncs.com',
            'ap-northeast-2-pop': 'antiddos.aliyuncs.com',
            'cn-beijing-finance-1': 'antiddos.aliyuncs.com',
            'cn-beijing-finance-pop': 'antiddos.aliyuncs.com',
            'cn-beijing-gov-1': 'antiddos.aliyuncs.com',
            'cn-beijing-nu16-b01': 'antiddos.aliyuncs.com',
            'cn-edge-1': 'antiddos.aliyuncs.com',
            'cn-fujian': 'antiddos.aliyuncs.com',
            'cn-haidian-cm12-c01': 'antiddos.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'antiddos.aliyuncs.com',
            'cn-hangzhou-finance': 'antiddos.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'antiddos.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'antiddos.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'antiddos.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'antiddos.aliyuncs.com',
            'cn-hangzhou-test-306': 'antiddos.aliyuncs.com',
            'cn-hongkong-finance-pop': 'antiddos.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'antiddos.aliyuncs.com',
            'cn-qingdao-nebula': 'antiddos.aliyuncs.com',
            'cn-shanghai-et15-b01': 'antiddos.aliyuncs.com',
            'cn-shanghai-et2-b01': 'antiddos.aliyuncs.com',
            'cn-shanghai-inner': 'antiddos.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'antiddos.aliyuncs.com',
            'cn-shenzhen-inner': 'antiddos.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'antiddos.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'antiddos.aliyuncs.com',
            'cn-wuhan': 'antiddos.aliyuncs.com',
            'cn-yushanfang': 'antiddos.aliyuncs.com',
            'cn-zhangbei': 'antiddos.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'antiddos.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'antiddos-openapi.cn-zhangjiakou.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'antiddos.aliyuncs.com',
            'eu-west-1-oxs': 'antiddos.aliyuncs.com',
            'rus-west-1-pop': 'antiddos.aliyuncs.com',
            'us-southeast-1': 'antiddos-openapi.us-southeast-1.aliyuncs.com',
            'na-south-1': 'antiddos-openapi.na-south-1.aliyuncs.com',
            'me-central-1': 'antiddos-openapi.me-central-1.aliyuncs.com',
            'eu-west-2': 'antiddos-openapi.eu-west-2.aliyuncs.com',
            'cn-zhongwei': 'antiddos-openapi.cn-zhongwei.aliyuncs.com',
            'cn-zhengzhou-jva': 'antiddos-openapi.cn-zhengzhou-jva.aliyuncs.com',
            'cn-wuhan-lr': 'antiddos-openapi.cn-hangzhou-cloudstone.aliyuncs.com',
            'cn-fuzhou': 'antiddos-openapi.cn-hangzhou-cloudstone.aliyuncs.com',
            'ap-southeast-8': 'antiddos-openapi.ap-southeast-8.aliyuncs.com',
            'ap-southeast-7': 'antiddos-openapi.ap-southeast-7.aliyuncs.com'
        }
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_bgp_pack_by_ip_with_options(
        self,
        request: main_models.DescribeBgpPackByIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBgpPackByIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBgpPackByIp',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBgpPackByIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bgp_pack_by_ip_with_options_async(
        self,
        request: main_models.DescribeBgpPackByIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBgpPackByIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBgpPackByIp',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBgpPackByIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bgp_pack_by_ip(
        self,
        request: main_models.DescribeBgpPackByIpRequest,
    ) -> main_models.DescribeBgpPackByIpResponse:
        runtime = RuntimeOptions()
        return self.describe_bgp_pack_by_ip_with_options(request, runtime)

    async def describe_bgp_pack_by_ip_async(
        self,
        request: main_models.DescribeBgpPackByIpRequest,
    ) -> main_models.DescribeBgpPackByIpResponse:
        runtime = RuntimeOptions()
        return await self.describe_bgp_pack_by_ip_with_options_async(request, runtime)

    def describe_cap_with_options(
        self,
        request: main_models.DescribeCapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.beg_time):
            query['BegTime'] = request.beg_time
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCap',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCapResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cap_with_options_async(
        self,
        request: main_models.DescribeCapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.beg_time):
            query['BegTime'] = request.beg_time
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCap',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cap(
        self,
        request: main_models.DescribeCapRequest,
    ) -> main_models.DescribeCapResponse:
        runtime = RuntimeOptions()
        return self.describe_cap_with_options(request, runtime)

    async def describe_cap_async(
        self,
        request: main_models.DescribeCapRequest,
    ) -> main_models.DescribeCapResponse:
        runtime = RuntimeOptions()
        return await self.describe_cap_with_options_async(request, runtime)

    def describe_ddos_count_with_options(
        self,
        request: main_models.DescribeDdosCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosCount',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_count_with_options_async(
        self,
        request: main_models.DescribeDdosCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosCount',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_count(
        self,
        request: main_models.DescribeDdosCountRequest,
    ) -> main_models.DescribeDdosCountResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_count_with_options(request, runtime)

    async def describe_ddos_count_async(
        self,
        request: main_models.DescribeDdosCountRequest,
    ) -> main_models.DescribeDdosCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_count_with_options_async(request, runtime)

    def describe_ddos_credit_with_options(
        self,
        request: main_models.DescribeDdosCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosCreditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosCredit',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosCreditResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_credit_with_options_async(
        self,
        request: main_models.DescribeDdosCreditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosCreditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosCredit',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosCreditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_credit(
        self,
        request: main_models.DescribeDdosCreditRequest,
    ) -> main_models.DescribeDdosCreditResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_credit_with_options(request, runtime)

    async def describe_ddos_credit_async(
        self,
        request: main_models.DescribeDdosCreditRequest,
    ) -> main_models.DescribeDdosCreditResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_credit_with_options_async(request, runtime)

    def describe_ddos_event_list_with_options(
        self,
        request: main_models.DescribeDdosEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_days):
            query['QueryDays'] = request.query_days
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosEventList',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_list_with_options_async(
        self,
        request: main_models.DescribeDdosEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_days):
            query['QueryDays'] = request.query_days
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosEventList',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_event_list(
        self,
        request: main_models.DescribeDdosEventListRequest,
    ) -> main_models.DescribeDdosEventListResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_event_list_with_options(request, runtime)

    async def describe_ddos_event_list_async(
        self,
        request: main_models.DescribeDdosEventListRequest,
    ) -> main_models.DescribeDdosEventListResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_event_list_with_options_async(request, runtime)

    def describe_ddos_threshold_with_options(
        self,
        request: main_models.DescribeDdosThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.ddos_type):
            query['DdosType'] = request.ddos_type
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosThreshold',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_threshold_with_options_async(
        self,
        request: main_models.DescribeDdosThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDdosThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.ddos_type):
            query['DdosType'] = request.ddos_type
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDdosThreshold',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDdosThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_threshold(
        self,
        request: main_models.DescribeDdosThresholdRequest,
    ) -> main_models.DescribeDdosThresholdResponse:
        runtime = RuntimeOptions()
        return self.describe_ddos_threshold_with_options(request, runtime)

    async def describe_ddos_threshold_async(
        self,
        request: main_models.DescribeDdosThresholdRequest,
    ) -> main_models.DescribeDdosThresholdResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddos_threshold_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.ddos_status):
            query['DdosStatus'] = request.ddos_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.ddos_status):
            query['DdosStatus'] = request.ddos_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_instance_ip_address_with_options(
        self,
        request: main_models.DescribeInstanceIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceIpAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.ddos_status):
            query['DdosStatus'] = request.ddos_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceIpAddress',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ip_address_with_options_async(
        self,
        request: main_models.DescribeInstanceIpAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceIpAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.ddos_status):
            query['DdosStatus'] = request.ddos_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceIpAddress',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ip_address(
        self,
        request: main_models.DescribeInstanceIpAddressRequest,
    ) -> main_models.DescribeInstanceIpAddressResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_ip_address_with_options(request, runtime)

    async def describe_instance_ip_address_async(
        self,
        request: main_models.DescribeInstanceIpAddressRequest,
    ) -> main_models.DescribeInstanceIpAddressResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_ip_address_with_options_async(request, runtime)

    def describe_ip_ddos_threshold_with_options(
        self,
        request: main_models.DescribeIpDdosThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpDdosThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.ddos_type):
            query['DdosType'] = request.ddos_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpDdosThreshold',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpDdosThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_ddos_threshold_with_options_async(
        self,
        request: main_models.DescribeIpDdosThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpDdosThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.ddos_type):
            query['DdosType'] = request.ddos_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpDdosThreshold',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpDdosThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_ddos_threshold(
        self,
        request: main_models.DescribeIpDdosThresholdRequest,
    ) -> main_models.DescribeIpDdosThresholdResponse:
        runtime = RuntimeOptions()
        return self.describe_ip_ddos_threshold_with_options(request, runtime)

    async def describe_ip_ddos_threshold_async(
        self,
        request: main_models.DescribeIpDdosThresholdRequest,
    ) -> main_models.DescribeIpDdosThresholdResponse:
        runtime = RuntimeOptions()
        return await self.describe_ip_ddos_threshold_with_options_async(request, runtime)

    def describe_ip_location_service_with_options(
        self,
        request: main_models.DescribeIpLocationServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpLocationServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpLocationService',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpLocationServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_location_service_with_options_async(
        self,
        request: main_models.DescribeIpLocationServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpLocationServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpLocationService',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpLocationServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_location_service(
        self,
        request: main_models.DescribeIpLocationServiceRequest,
    ) -> main_models.DescribeIpLocationServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_ip_location_service_with_options(request, runtime)

    async def describe_ip_location_service_async(
        self,
        request: main_models.DescribeIpLocationServiceRequest,
    ) -> main_models.DescribeIpLocationServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_ip_location_service_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def modify_defense_threshold_with_options(
        self,
        request: main_models.ModifyDefenseThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bps):
            query['Bps'] = request.bps
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not DaraCore.is_null(request.is_auto):
            query['IsAuto'] = request.is_auto
        if not DaraCore.is_null(request.pps):
            query['Pps'] = request.pps
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseThreshold',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_threshold_with_options_async(
        self,
        request: main_models.ModifyDefenseThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bps):
            query['Bps'] = request.bps
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not DaraCore.is_null(request.is_auto):
            query['IsAuto'] = request.is_auto
        if not DaraCore.is_null(request.pps):
            query['Pps'] = request.pps
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseThreshold',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_threshold(
        self,
        request: main_models.ModifyDefenseThresholdRequest,
    ) -> main_models.ModifyDefenseThresholdResponse:
        runtime = RuntimeOptions()
        return self.modify_defense_threshold_with_options(request, runtime)

    async def modify_defense_threshold_async(
        self,
        request: main_models.ModifyDefenseThresholdRequest,
    ) -> main_models.ModifyDefenseThresholdResponse:
        runtime = RuntimeOptions()
        return await self.modify_defense_threshold_with_options_async(request, runtime)

    def modify_ip_defense_threshold_with_options(
        self,
        request: main_models.ModifyIpDefenseThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpDefenseThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bps):
            query['Bps'] = request.bps
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not DaraCore.is_null(request.is_auto):
            query['IsAuto'] = request.is_auto
        if not DaraCore.is_null(request.pps):
            query['Pps'] = request.pps
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpDefenseThreshold',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpDefenseThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ip_defense_threshold_with_options_async(
        self,
        request: main_models.ModifyIpDefenseThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpDefenseThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bps):
            query['Bps'] = request.bps
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not DaraCore.is_null(request.is_auto):
            query['IsAuto'] = request.is_auto
        if not DaraCore.is_null(request.pps):
            query['Pps'] = request.pps
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpDefenseThreshold',
            version = '2017-05-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpDefenseThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ip_defense_threshold(
        self,
        request: main_models.ModifyIpDefenseThresholdRequest,
    ) -> main_models.ModifyIpDefenseThresholdResponse:
        runtime = RuntimeOptions()
        return self.modify_ip_defense_threshold_with_options(request, runtime)

    async def modify_ip_defense_threshold_async(
        self,
        request: main_models.ModifyIpDefenseThresholdRequest,
    ) -> main_models.ModifyIpDefenseThresholdResponse:
        runtime = RuntimeOptions()
        return await self.modify_ip_defense_threshold_with_options_async(request, runtime)
