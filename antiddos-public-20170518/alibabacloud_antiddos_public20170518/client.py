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
            'rus-west-1-pop': 'antiddos.aliyuncs.com'
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
        """
        @summary Queries the configurations of the Anti-DDoS Origin instance that is associated with an asset. The asset is assigned a public IP address.
        
        @description You can call the DescribeBgpPackByIp operation to query the configurations of the Anti-DDoS Origin instance that is associated with an asset. The configurations include the basic protection threshold, burstable protection threshold, and expiration time.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBgpPackByIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBgpPackByIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBgpPackByIp',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeBgpPackByIpResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeBgpPackByIpResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_bgp_pack_by_ip_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackByIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeBgpPackByIpResponse:
        """
        @summary Queries the configurations of the Anti-DDoS Origin instance that is associated with an asset. The asset is assigned a public IP address.
        
        @description You can call the DescribeBgpPackByIp operation to query the configurations of the Anti-DDoS Origin instance that is associated with an asset. The configurations include the basic protection threshold, burstable protection threshold, and expiration time.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBgpPackByIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBgpPackByIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBgpPackByIp',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeBgpPackByIpResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeBgpPackByIpResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_bgp_pack_by_ip(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackByIpRequest,
    ) -> antiddos_public_20170518_models.DescribeBgpPackByIpResponse:
        """
        @summary Queries the configurations of the Anti-DDoS Origin instance that is associated with an asset. The asset is assigned a public IP address.
        
        @description You can call the DescribeBgpPackByIp operation to query the configurations of the Anti-DDoS Origin instance that is associated with an asset. The configurations include the basic protection threshold, burstable protection threshold, and expiration time.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBgpPackByIpRequest
        @return: DescribeBgpPackByIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_bgp_pack_by_ip_with_options(request, runtime)

    async def describe_bgp_pack_by_ip_async(
        self,
        request: antiddos_public_20170518_models.DescribeBgpPackByIpRequest,
    ) -> antiddos_public_20170518_models.DescribeBgpPackByIpResponse:
        """
        @summary Queries the configurations of the Anti-DDoS Origin instance that is associated with an asset. The asset is assigned a public IP address.
        
        @description You can call the DescribeBgpPackByIp operation to query the configurations of the Anti-DDoS Origin instance that is associated with an asset. The configurations include the basic protection threshold, burstable protection threshold, and expiration time.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBgpPackByIpRequest
        @return: DescribeBgpPackByIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_bgp_pack_by_ip_with_options_async(request, runtime)

    def describe_cap_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeCapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeCapResponse:
        """
        @summary Queries the download link to the traffic data that is captured when a DDoS attack event occurs.
        
        @description You can call the DescribeCap operation to query the download link to the traffic data that is captured when a DDoS attack event occurs. You can download the traffic data from the download link and use the data as evidence.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.beg_time):
            query['BegTime'] = request.beg_time
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCap',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeCapResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeCapResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cap_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeCapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeCapResponse:
        """
        @summary Queries the download link to the traffic data that is captured when a DDoS attack event occurs.
        
        @description You can call the DescribeCap operation to query the download link to the traffic data that is captured when a DDoS attack event occurs. You can download the traffic data from the download link and use the data as evidence.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.beg_time):
            query['BegTime'] = request.beg_time
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCap',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeCapResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeCapResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cap(
        self,
        request: antiddos_public_20170518_models.DescribeCapRequest,
    ) -> antiddos_public_20170518_models.DescribeCapResponse:
        """
        @summary Queries the download link to the traffic data that is captured when a DDoS attack event occurs.
        
        @description You can call the DescribeCap operation to query the download link to the traffic data that is captured when a DDoS attack event occurs. You can download the traffic data from the download link and use the data as evidence.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCapRequest
        @return: DescribeCapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cap_with_options(request, runtime)

    async def describe_cap_async(
        self,
        request: antiddos_public_20170518_models.DescribeCapRequest,
    ) -> antiddos_public_20170518_models.DescribeCapResponse:
        """
        @summary Queries the download link to the traffic data that is captured when a DDoS attack event occurs.
        
        @description You can call the DescribeCap operation to query the download link to the traffic data that is captured when a DDoS attack event occurs. You can download the traffic data from the download link and use the data as evidence.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCapRequest
        @return: DescribeCapResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cap_with_options_async(request, runtime)

    def describe_ddos_count_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCountResponse:
        """
        @summary Queries the number of assets that are under DDoS attacks in a specific region. The assets are assigned public IP addresses.
        
        @description ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosCount',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosCountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosCountResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_ddos_count_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCountResponse:
        """
        @summary Queries the number of assets that are under DDoS attacks in a specific region. The assets are assigned public IP addresses.
        
        @description ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosCount',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosCountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosCountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_ddos_count(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCountRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosCountResponse:
        """
        @summary Queries the number of assets that are under DDoS attacks in a specific region. The assets are assigned public IP addresses.
        
        @description ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosCountRequest
        @return: DescribeDdosCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_count_with_options(request, runtime)

    async def describe_ddos_count_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCountRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosCountResponse:
        """
        @summary Queries the number of assets that are under DDoS attacks in a specific region. The assets are assigned public IP addresses.
        
        @description ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosCountRequest
        @return: DescribeDdosCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_count_with_options_async(request, runtime)

    def describe_ddos_credit_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCreditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCreditResponse:
        """
        @summary Queries the details of the security credit score of the current Alibaba Cloud account in a specific region.
        
        @description You can call the DescribeDdosCredit operation to query the details of the security credit score of the current Alibaba Cloud account in a specific region. The details include the security credit score, security credit level, and the time period after which blackhole filtering is automatically deactivated.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosCreditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosCreditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosCredit',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosCreditResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosCreditResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_ddos_credit_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCreditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosCreditResponse:
        """
        @summary Queries the details of the security credit score of the current Alibaba Cloud account in a specific region.
        
        @description You can call the DescribeDdosCredit operation to query the details of the security credit score of the current Alibaba Cloud account in a specific region. The details include the security credit score, security credit level, and the time period after which blackhole filtering is automatically deactivated.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosCreditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosCreditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosCredit',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosCreditResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosCreditResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_ddos_credit(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCreditRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosCreditResponse:
        """
        @summary Queries the details of the security credit score of the current Alibaba Cloud account in a specific region.
        
        @description You can call the DescribeDdosCredit operation to query the details of the security credit score of the current Alibaba Cloud account in a specific region. The details include the security credit score, security credit level, and the time period after which blackhole filtering is automatically deactivated.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosCreditRequest
        @return: DescribeDdosCreditResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_credit_with_options(request, runtime)

    async def describe_ddos_credit_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosCreditRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosCreditResponse:
        """
        @summary Queries the details of the security credit score of the current Alibaba Cloud account in a specific region.
        
        @description You can call the DescribeDdosCredit operation to query the details of the security credit score of the current Alibaba Cloud account in a specific region. The details include the security credit score, security credit level, and the time period after which blackhole filtering is automatically deactivated.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosCreditRequest
        @return: DescribeDdosCreditResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_credit_with_options_async(request, runtime)

    def describe_ddos_event_list_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeDdosEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosEventListResponse:
        """
        @summary Queries the details of the DDoS attack events that occur on an asset. The asset is assigned a public IP address.
        
        @description You can call the DescribeDdosEventList operation to query the details of the DDoS attack events that occur on an asset by page. The details include the start time, end time, and status of each DDoS attack event.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosEventList',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosEventListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosEventListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_ddos_event_list_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosEventListResponse:
        """
        @summary Queries the details of the DDoS attack events that occur on an asset. The asset is assigned a public IP address.
        
        @description You can call the DescribeDdosEventList operation to query the details of the DDoS attack events that occur on an asset by page. The details include the start time, end time, and status of each DDoS attack event.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosEventList',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosEventListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosEventListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_ddos_event_list(
        self,
        request: antiddos_public_20170518_models.DescribeDdosEventListRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosEventListResponse:
        """
        @summary Queries the details of the DDoS attack events that occur on an asset. The asset is assigned a public IP address.
        
        @description You can call the DescribeDdosEventList operation to query the details of the DDoS attack events that occur on an asset by page. The details include the start time, end time, and status of each DDoS attack event.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosEventListRequest
        @return: DescribeDdosEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_list_with_options(request, runtime)

    async def describe_ddos_event_list_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosEventListRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosEventListResponse:
        """
        @summary Queries the details of the DDoS attack events that occur on an asset. The asset is assigned a public IP address.
        
        @description You can call the DescribeDdosEventList operation to query the details of the DDoS attack events that occur on an asset by page. The details include the start time, end time, and status of each DDoS attack event.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosEventListRequest
        @return: DescribeDdosEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_list_with_options_async(request, runtime)

    def describe_ddos_threshold_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeDdosThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosThresholdResponse:
        """
        @summary Queries the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description You can call the DescribeDdosThreshold operation to query the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The details include the current traffic scrubbing threshold, maximum traffic scrubbing threshold, current DDoS mitigation threshold, and maximum DDoS mitigation threshold.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_type):
            query['DdosType'] = request.ddos_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosThresholdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosThresholdResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_ddos_threshold_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeDdosThresholdResponse:
        """
        @summary Queries the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description You can call the DescribeDdosThreshold operation to query the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The details include the current traffic scrubbing threshold, maximum traffic scrubbing threshold, current DDoS mitigation threshold, and maximum DDoS mitigation threshold.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_type):
            query['DdosType'] = request.ddos_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosThresholdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeDdosThresholdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_ddos_threshold(
        self,
        request: antiddos_public_20170518_models.DescribeDdosThresholdRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosThresholdResponse:
        """
        @summary Queries the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description You can call the DescribeDdosThreshold operation to query the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The details include the current traffic scrubbing threshold, maximum traffic scrubbing threshold, current DDoS mitigation threshold, and maximum DDoS mitigation threshold.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosThresholdRequest
        @return: DescribeDdosThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_threshold_with_options(request, runtime)

    async def describe_ddos_threshold_async(
        self,
        request: antiddos_public_20170518_models.DescribeDdosThresholdRequest,
    ) -> antiddos_public_20170518_models.DescribeDdosThresholdResponse:
        """
        @summary Queries the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description You can call the DescribeDdosThreshold operation to query the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The details include the current traffic scrubbing threshold, maximum traffic scrubbing threshold, current DDoS mitigation threshold, and maximum DDoS mitigation threshold.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosThresholdRequest
        @return: DescribeDdosThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_threshold_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeInstanceResponse:
        """
        @summary Queries the details of the assets within the current Alibaba Cloud account. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses. This operation is phased out. We recommend that you use the DescribeInstanceIpAddress operation.
        
        @description You can call the DescribeInstance operation to query the details of the assets that are within the current Alibaba Cloud account by page. The details include the IDs and IP addresses of the assets, the basic protection thresholds and traffic scrubbing thresholds that are configured for the assets in Anti-DDoS Origin, and whether the assets are associated with Anti-DDoS Origin instances.
        ### [](#qps-)Limits
        You can call this operation up to 200 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_status):
            query['DdosStatus'] = request.ddos_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeInstanceResponse:
        """
        @summary Queries the details of the assets within the current Alibaba Cloud account. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses. This operation is phased out. We recommend that you use the DescribeInstanceIpAddress operation.
        
        @description You can call the DescribeInstance operation to query the details of the assets that are within the current Alibaba Cloud account by page. The details include the IDs and IP addresses of the assets, the basic protection thresholds and traffic scrubbing thresholds that are configured for the assets in Anti-DDoS Origin, and whether the assets are associated with Anti-DDoS Origin instances.
        ### [](#qps-)Limits
        You can call this operation up to 200 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_status):
            query['DdosStatus'] = request.ddos_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceRequest,
    ) -> antiddos_public_20170518_models.DescribeInstanceResponse:
        """
        @summary Queries the details of the assets within the current Alibaba Cloud account. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses. This operation is phased out. We recommend that you use the DescribeInstanceIpAddress operation.
        
        @description You can call the DescribeInstance operation to query the details of the assets that are within the current Alibaba Cloud account by page. The details include the IDs and IP addresses of the assets, the basic protection thresholds and traffic scrubbing thresholds that are configured for the assets in Anti-DDoS Origin, and whether the assets are associated with Anti-DDoS Origin instances.
        ### [](#qps-)Limits
        You can call this operation up to 200 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceRequest,
    ) -> antiddos_public_20170518_models.DescribeInstanceResponse:
        """
        @summary Queries the details of the assets within the current Alibaba Cloud account. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses. This operation is phased out. We recommend that you use the DescribeInstanceIpAddress operation.
        
        @description You can call the DescribeInstance operation to query the details of the assets that are within the current Alibaba Cloud account by page. The details include the IDs and IP addresses of the assets, the basic protection thresholds and traffic scrubbing thresholds that are configured for the assets in Anti-DDoS Origin, and whether the assets are associated with Anti-DDoS Origin instances.
        ### [](#qps-)Limits
        You can call this operation up to 200 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_instance_ip_address_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeInstanceIpAddressResponse:
        """
        @summary Queries the details of the assets within the current Alibaba Cloud account and the details of the Anti-DDoS Origin instance to which the assets belong. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description If one or more assets of the current Alibaba Cloud account are added to an Anti-DDoS Origin instance, you can call the DescribeInstanceIpAddress operation to query the DDoS mitigation information and the details of the Anti-DDoS Origin instance. The information and the details include the basic protection threshold and traffic scrubbing threshold for the assets, DDoS mitigation status of the assets, ID of the instance, and the mitigation status of the instance.
        ## Limits
        You can call this operation up to 200 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceIpAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_status):
            query['DdosStatus'] = request.ddos_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIpAddress',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeInstanceIpAddressResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeInstanceIpAddressResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_ip_address_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeInstanceIpAddressResponse:
        """
        @summary Queries the details of the assets within the current Alibaba Cloud account and the details of the Anti-DDoS Origin instance to which the assets belong. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description If one or more assets of the current Alibaba Cloud account are added to an Anti-DDoS Origin instance, you can call the DescribeInstanceIpAddress operation to query the DDoS mitigation information and the details of the Anti-DDoS Origin instance. The information and the details include the basic protection threshold and traffic scrubbing threshold for the assets, DDoS mitigation status of the assets, ID of the instance, and the mitigation status of the instance.
        ## Limits
        You can call this operation up to 200 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceIpAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_status):
            query['DdosStatus'] = request.ddos_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIpAddress',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeInstanceIpAddressResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeInstanceIpAddressResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_ip_address(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceIpAddressRequest,
    ) -> antiddos_public_20170518_models.DescribeInstanceIpAddressResponse:
        """
        @summary Queries the details of the assets within the current Alibaba Cloud account and the details of the Anti-DDoS Origin instance to which the assets belong. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description If one or more assets of the current Alibaba Cloud account are added to an Anti-DDoS Origin instance, you can call the DescribeInstanceIpAddress operation to query the DDoS mitigation information and the details of the Anti-DDoS Origin instance. The information and the details include the basic protection threshold and traffic scrubbing threshold for the assets, DDoS mitigation status of the assets, ID of the instance, and the mitigation status of the instance.
        ## Limits
        You can call this operation up to 200 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceIpAddressRequest
        @return: DescribeInstanceIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ip_address_with_options(request, runtime)

    async def describe_instance_ip_address_async(
        self,
        request: antiddos_public_20170518_models.DescribeInstanceIpAddressRequest,
    ) -> antiddos_public_20170518_models.DescribeInstanceIpAddressResponse:
        """
        @summary Queries the details of the assets within the current Alibaba Cloud account and the details of the Anti-DDoS Origin instance to which the assets belong. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description If one or more assets of the current Alibaba Cloud account are added to an Anti-DDoS Origin instance, you can call the DescribeInstanceIpAddress operation to query the DDoS mitigation information and the details of the Anti-DDoS Origin instance. The information and the details include the basic protection threshold and traffic scrubbing threshold for the assets, DDoS mitigation status of the assets, ID of the instance, and the mitigation status of the instance.
        ## Limits
        You can call this operation up to 200 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceIpAddressRequest
        @return: DescribeInstanceIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_ip_address_with_options_async(request, runtime)

    def describe_ip_ddos_threshold_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeIpDdosThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeIpDdosThresholdResponse:
        """
        @summary Queries the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description If one or more assets of the current Alibaba Cloud account are added to an Anti-DDoS Origin instance, you can call the DescribeIpDdosThreshold operation to query the details of the DDoS mitigation threshold or traffic scrubbing threshold for a specific asset. The details include the current traffic scrubbing threshold, maximum scrubbing threshold, current DDoS mitigation threshold, and maximum DDoS mitigation threshold.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeIpDdosThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIpDdosThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_type):
            query['DdosType'] = request.ddos_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpDdosThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeIpDdosThresholdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeIpDdosThresholdResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_ip_ddos_threshold_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeIpDdosThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeIpDdosThresholdResponse:
        """
        @summary Queries the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description If one or more assets of the current Alibaba Cloud account are added to an Anti-DDoS Origin instance, you can call the DescribeIpDdosThreshold operation to query the details of the DDoS mitigation threshold or traffic scrubbing threshold for a specific asset. The details include the current traffic scrubbing threshold, maximum scrubbing threshold, current DDoS mitigation threshold, and maximum DDoS mitigation threshold.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeIpDdosThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIpDdosThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_type):
            query['DdosType'] = request.ddos_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpDdosThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeIpDdosThresholdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeIpDdosThresholdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_ip_ddos_threshold(
        self,
        request: antiddos_public_20170518_models.DescribeIpDdosThresholdRequest,
    ) -> antiddos_public_20170518_models.DescribeIpDdosThresholdResponse:
        """
        @summary Queries the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description If one or more assets of the current Alibaba Cloud account are added to an Anti-DDoS Origin instance, you can call the DescribeIpDdosThreshold operation to query the details of the DDoS mitigation threshold or traffic scrubbing threshold for a specific asset. The details include the current traffic scrubbing threshold, maximum scrubbing threshold, current DDoS mitigation threshold, and maximum DDoS mitigation threshold.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeIpDdosThresholdRequest
        @return: DescribeIpDdosThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_ddos_threshold_with_options(request, runtime)

    async def describe_ip_ddos_threshold_async(
        self,
        request: antiddos_public_20170518_models.DescribeIpDdosThresholdRequest,
    ) -> antiddos_public_20170518_models.DescribeIpDdosThresholdResponse:
        """
        @summary Queries the details of the DDoS mitigation thresholds or traffic scrubbing thresholds for specified assets. The assets can be elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS) instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description If one or more assets of the current Alibaba Cloud account are added to an Anti-DDoS Origin instance, you can call the DescribeIpDdosThreshold operation to query the details of the DDoS mitigation threshold or traffic scrubbing threshold for a specific asset. The details include the current traffic scrubbing threshold, maximum scrubbing threshold, current DDoS mitigation threshold, and maximum DDoS mitigation threshold.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeIpDdosThresholdRequest
        @return: DescribeIpDdosThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_ddos_threshold_with_options_async(request, runtime)

    def describe_ip_location_service_with_options(
        self,
        request: antiddos_public_20170518_models.DescribeIpLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeIpLocationServiceResponse:
        """
        @summary Queries the region to which the public IP address of the asset within the current Alibaba Cloud account belongs. The asset can be an elastic IP address (EIP). The asset can also be an Elastic Compute Service (ECS) instance or Server Load Balancer (SLB) instance that is assigned a public IP address.
        
        @description You can call the DescribeIpLocationService operation to query the region of the public IP address for a specified asset that is within the current Alibaba Cloud account. You can also query the details of the Anti-DDoS Origin instance to which the asset is added. The details include the ID and name.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeIpLocationServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIpLocationServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpLocationService',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeIpLocationServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeIpLocationServiceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_ip_location_service_with_options_async(
        self,
        request: antiddos_public_20170518_models.DescribeIpLocationServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeIpLocationServiceResponse:
        """
        @summary Queries the region to which the public IP address of the asset within the current Alibaba Cloud account belongs. The asset can be an elastic IP address (EIP). The asset can also be an Elastic Compute Service (ECS) instance or Server Load Balancer (SLB) instance that is assigned a public IP address.
        
        @description You can call the DescribeIpLocationService operation to query the region of the public IP address for a specified asset that is within the current Alibaba Cloud account. You can also query the details of the Anti-DDoS Origin instance to which the asset is added. The details include the ID and name.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeIpLocationServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIpLocationServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpLocationService',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeIpLocationServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeIpLocationServiceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_ip_location_service(
        self,
        request: antiddos_public_20170518_models.DescribeIpLocationServiceRequest,
    ) -> antiddos_public_20170518_models.DescribeIpLocationServiceResponse:
        """
        @summary Queries the region to which the public IP address of the asset within the current Alibaba Cloud account belongs. The asset can be an elastic IP address (EIP). The asset can also be an Elastic Compute Service (ECS) instance or Server Load Balancer (SLB) instance that is assigned a public IP address.
        
        @description You can call the DescribeIpLocationService operation to query the region of the public IP address for a specified asset that is within the current Alibaba Cloud account. You can also query the details of the Anti-DDoS Origin instance to which the asset is added. The details include the ID and name.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeIpLocationServiceRequest
        @return: DescribeIpLocationServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_location_service_with_options(request, runtime)

    async def describe_ip_location_service_async(
        self,
        request: antiddos_public_20170518_models.DescribeIpLocationServiceRequest,
    ) -> antiddos_public_20170518_models.DescribeIpLocationServiceResponse:
        """
        @summary Queries the region to which the public IP address of the asset within the current Alibaba Cloud account belongs. The asset can be an elastic IP address (EIP). The asset can also be an Elastic Compute Service (ECS) instance or Server Load Balancer (SLB) instance that is assigned a public IP address.
        
        @description You can call the DescribeIpLocationService operation to query the region of the public IP address for a specified asset that is within the current Alibaba Cloud account. You can also query the details of the Anti-DDoS Origin instance to which the asset is added. The details include the ID and name.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeIpLocationServiceRequest
        @return: DescribeIpLocationServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_location_service_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which Anti-DDoS Origin Basic is available.
        
        @description You can call this operation to query information about the regions in which Anti-DDoS Origin Basic is available. The information includes the region ID, region name, and code.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeRegionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeRegionsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which Anti-DDoS Origin Basic is available.
        
        @description You can call this operation to query information about the regions in which Anti-DDoS Origin Basic is available. The information includes the region ID, region name, and code.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeRegionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.DescribeRegionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_regions(self) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which Anti-DDoS Origin Basic is available.
        
        @description You can call this operation to query information about the regions in which Anti-DDoS Origin Basic is available. The information includes the region ID, region name, and code.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> antiddos_public_20170518_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which Anti-DDoS Origin Basic is available.
        
        @description You can call this operation to query information about the regions in which Anti-DDoS Origin Basic is available. The information includes the region ID, region name, and code.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def modify_defense_threshold_with_options(
        self,
        request: antiddos_public_20170518_models.ModifyDefenseThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyDefenseThresholdResponse:
        """
        @summary Changes the scrubbing thresholds for an asset that is assigned a public IP address.
        
        @description ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDefenseThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bps):
            query['Bps'] = request.bps
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not UtilClient.is_unset(request.is_auto):
            query['IsAuto'] = request.is_auto
        if not UtilClient.is_unset(request.pps):
            query['Pps'] = request.pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.ModifyDefenseThresholdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.ModifyDefenseThresholdResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_defense_threshold_with_options_async(
        self,
        request: antiddos_public_20170518_models.ModifyDefenseThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyDefenseThresholdResponse:
        """
        @summary Changes the scrubbing thresholds for an asset that is assigned a public IP address.
        
        @description ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDefenseThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefenseThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bps):
            query['Bps'] = request.bps
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not UtilClient.is_unset(request.is_auto):
            query['IsAuto'] = request.is_auto
        if not UtilClient.is_unset(request.pps):
            query['Pps'] = request.pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.ModifyDefenseThresholdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.ModifyDefenseThresholdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_defense_threshold(
        self,
        request: antiddos_public_20170518_models.ModifyDefenseThresholdRequest,
    ) -> antiddos_public_20170518_models.ModifyDefenseThresholdResponse:
        """
        @summary Changes the scrubbing thresholds for an asset that is assigned a public IP address.
        
        @description ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDefenseThresholdRequest
        @return: ModifyDefenseThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_threshold_with_options(request, runtime)

    async def modify_defense_threshold_async(
        self,
        request: antiddos_public_20170518_models.ModifyDefenseThresholdRequest,
    ) -> antiddos_public_20170518_models.ModifyDefenseThresholdResponse:
        """
        @summary Changes the scrubbing thresholds for an asset that is assigned a public IP address.
        
        @description ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDefenseThresholdRequest
        @return: ModifyDefenseThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_defense_threshold_with_options_async(request, runtime)

    def modify_ip_defense_threshold_with_options(
        self,
        request: antiddos_public_20170518_models.ModifyIpDefenseThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyIpDefenseThresholdResponse:
        """
        @summary Modifies the scrubbing thresholds for an asset that is assigned a public IP address. This operation is a synchronous operation that supports Terraform.
        
        @description ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyIpDefenseThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIpDefenseThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bps):
            query['Bps'] = request.bps
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not UtilClient.is_unset(request.is_auto):
            query['IsAuto'] = request.is_auto
        if not UtilClient.is_unset(request.pps):
            query['Pps'] = request.pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpDefenseThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.ModifyIpDefenseThresholdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.ModifyIpDefenseThresholdResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_ip_defense_threshold_with_options_async(
        self,
        request: antiddos_public_20170518_models.ModifyIpDefenseThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> antiddos_public_20170518_models.ModifyIpDefenseThresholdResponse:
        """
        @summary Modifies the scrubbing thresholds for an asset that is assigned a public IP address. This operation is a synchronous operation that supports Terraform.
        
        @description ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyIpDefenseThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIpDefenseThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bps):
            query['Bps'] = request.bps
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not UtilClient.is_unset(request.is_auto):
            query['IsAuto'] = request.is_auto
        if not UtilClient.is_unset(request.pps):
            query['Pps'] = request.pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpDefenseThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                antiddos_public_20170518_models.ModifyIpDefenseThresholdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                antiddos_public_20170518_models.ModifyIpDefenseThresholdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_ip_defense_threshold(
        self,
        request: antiddos_public_20170518_models.ModifyIpDefenseThresholdRequest,
    ) -> antiddos_public_20170518_models.ModifyIpDefenseThresholdResponse:
        """
        @summary Modifies the scrubbing thresholds for an asset that is assigned a public IP address. This operation is a synchronous operation that supports Terraform.
        
        @description ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyIpDefenseThresholdRequest
        @return: ModifyIpDefenseThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_defense_threshold_with_options(request, runtime)

    async def modify_ip_defense_threshold_async(
        self,
        request: antiddos_public_20170518_models.ModifyIpDefenseThresholdRequest,
    ) -> antiddos_public_20170518_models.ModifyIpDefenseThresholdResponse:
        """
        @summary Modifies the scrubbing thresholds for an asset that is assigned a public IP address. This operation is a synchronous operation that supports Terraform.
        
        @description ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyIpDefenseThresholdRequest
        @return: ModifyIpDefenseThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_defense_threshold_with_options_async(request, runtime)
