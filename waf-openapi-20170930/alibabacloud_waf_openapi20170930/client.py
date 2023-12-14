# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_waf_openapi20170930 import models as waf_openapi_20170930_models
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
            'cn-qingdao': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-heyuan': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-wulanchabu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'wafopenapi.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('waf-openapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def app_open_ack_with_options(
        self,
        request: waf_openapi_20170930_models.AppOpenAckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.AppOpenAckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ack):
            query['Ack'] = request.ack
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.async_method):
            query['AsyncMethod'] = request.async_method
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AppOpenAck',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.AppOpenAckResponse(),
            self.call_api(params, req, runtime)
        )

    async def app_open_ack_with_options_async(
        self,
        request: waf_openapi_20170930_models.AppOpenAckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.AppOpenAckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ack):
            query['Ack'] = request.ack
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.async_method):
            query['AsyncMethod'] = request.async_method
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AppOpenAck',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.AppOpenAckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def app_open_ack(
        self,
        request: waf_openapi_20170930_models.AppOpenAckRequest,
    ) -> waf_openapi_20170930_models.AppOpenAckResponse:
        runtime = util_models.RuntimeOptions()
        return self.app_open_ack_with_options(request, runtime)

    async def app_open_ack_async(
        self,
        request: waf_openapi_20170930_models.AppOpenAckRequest,
    ) -> waf_openapi_20170930_models.AppOpenAckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.app_open_ack_with_options_async(request, runtime)

    def create_domain_config_with_options(
        self,
        request: waf_openapi_20170930_models.CreateDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.CreateDomainConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.http_to_user_ip):
            query['HttpToUserIp'] = request.http_to_user_ip
        if not UtilClient.is_unset(request.https_port):
            query['HttpsPort'] = request.https_port
        if not UtilClient.is_unset(request.https_redirect):
            query['HttpsRedirect'] = request.https_redirect
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_access_product):
            query['IsAccessProduct'] = request.is_access_product
        if not UtilClient.is_unset(request.is_non_standard_port):
            query['IsNonStandardPort'] = request.is_non_standard_port
        if not UtilClient.is_unset(request.load_balancing):
            query['LoadBalancing'] = request.load_balancing
        if not UtilClient.is_unset(request.protocols):
            query['Protocols'] = request.protocols
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        if not UtilClient.is_unset(request.source_ips):
            query['SourceIps'] = request.source_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainConfig',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.CreateDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_config_with_options_async(
        self,
        request: waf_openapi_20170930_models.CreateDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.CreateDomainConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.http_to_user_ip):
            query['HttpToUserIp'] = request.http_to_user_ip
        if not UtilClient.is_unset(request.https_port):
            query['HttpsPort'] = request.https_port
        if not UtilClient.is_unset(request.https_redirect):
            query['HttpsRedirect'] = request.https_redirect
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_access_product):
            query['IsAccessProduct'] = request.is_access_product
        if not UtilClient.is_unset(request.is_non_standard_port):
            query['IsNonStandardPort'] = request.is_non_standard_port
        if not UtilClient.is_unset(request.load_balancing):
            query['LoadBalancing'] = request.load_balancing
        if not UtilClient.is_unset(request.protocols):
            query['Protocols'] = request.protocols
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        if not UtilClient.is_unset(request.source_ips):
            query['SourceIps'] = request.source_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainConfig',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.CreateDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain_config(
        self,
        request: waf_openapi_20170930_models.CreateDomainConfigRequest,
    ) -> waf_openapi_20170930_models.CreateDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_domain_config_with_options(request, runtime)

    async def create_domain_config_async(
        self,
        request: waf_openapi_20170930_models.CreateDomainConfigRequest,
    ) -> waf_openapi_20170930_models.CreateDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_config_with_options_async(request, runtime)

    def delete_domain_config_with_options(
        self,
        request: waf_openapi_20170930_models.DeleteDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DeleteDomainConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainConfig',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DeleteDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_config_with_options_async(
        self,
        request: waf_openapi_20170930_models.DeleteDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DeleteDomainConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainConfig',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DeleteDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_config(
        self,
        request: waf_openapi_20170930_models.DeleteDomainConfigRequest,
    ) -> waf_openapi_20170930_models.DeleteDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_config_with_options(request, runtime)

    async def delete_domain_config_async(
        self,
        request: waf_openapi_20170930_models.DeleteDomainConfigRequest,
    ) -> waf_openapi_20170930_models.DeleteDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_config_with_options_async(request, runtime)

    def describe_domain_names_with_options(
        self,
        request: waf_openapi_20170930_models.DescribeDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeDomainNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainNames',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeDomainNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_names_with_options_async(
        self,
        request: waf_openapi_20170930_models.DescribeDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeDomainNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainNames',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeDomainNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_names(
        self,
        request: waf_openapi_20170930_models.DescribeDomainNamesRequest,
    ) -> waf_openapi_20170930_models.DescribeDomainNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_names_with_options(request, runtime)

    async def describe_domain_names_async(
        self,
        request: waf_openapi_20170930_models.DescribeDomainNamesRequest,
    ) -> waf_openapi_20170930_models.DescribeDomainNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_names_with_options_async(request, runtime)

    def describe_domain_transfer_config_with_options(
        self,
        request: waf_openapi_20170930_models.DescribeDomainTransferConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeDomainTransferConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainTransferConfig',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeDomainTransferConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_transfer_config_with_options_async(
        self,
        request: waf_openapi_20170930_models.DescribeDomainTransferConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeDomainTransferConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainTransferConfig',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeDomainTransferConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_transfer_config(
        self,
        request: waf_openapi_20170930_models.DescribeDomainTransferConfigRequest,
    ) -> waf_openapi_20170930_models.DescribeDomainTransferConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_transfer_config_with_options(request, runtime)

    async def describe_domain_transfer_config_async(
        self,
        request: waf_openapi_20170930_models.DescribeDomainTransferConfigRequest,
    ) -> waf_openapi_20170930_models.DescribeDomainTransferConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_transfer_config_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: waf_openapi_20170930_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: waf_openapi_20170930_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains(
        self,
        request: waf_openapi_20170930_models.DescribeDomainsRequest,
    ) -> waf_openapi_20170930_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: waf_openapi_20170930_models.DescribeDomainsRequest,
    ) -> waf_openapi_20170930_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_https_cert_in_use_with_options(
        self,
        request: waf_openapi_20170930_models.DescribeHttpsCertInUseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeHttpsCertInUseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHttpsCertInUse',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeHttpsCertInUseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_https_cert_in_use_with_options_async(
        self,
        request: waf_openapi_20170930_models.DescribeHttpsCertInUseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeHttpsCertInUseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHttpsCertInUse',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeHttpsCertInUseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_https_cert_in_use(
        self,
        request: waf_openapi_20170930_models.DescribeHttpsCertInUseRequest,
    ) -> waf_openapi_20170930_models.DescribeHttpsCertInUseResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_https_cert_in_use_with_options(request, runtime)

    async def describe_https_cert_in_use_async(
        self,
        request: waf_openapi_20170930_models.DescribeHttpsCertInUseRequest,
    ) -> waf_openapi_20170930_models.DescribeHttpsCertInUseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_https_cert_in_use_with_options_async(request, runtime)

    def describe_need_upgrade_domain_limit_with_options(
        self,
        request: waf_openapi_20170930_models.DescribeNeedUpgradeDomainLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeNeedUpgradeDomainLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNeedUpgradeDomainLimit',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeNeedUpgradeDomainLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_need_upgrade_domain_limit_with_options_async(
        self,
        request: waf_openapi_20170930_models.DescribeNeedUpgradeDomainLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeNeedUpgradeDomainLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNeedUpgradeDomainLimit',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeNeedUpgradeDomainLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_need_upgrade_domain_limit(
        self,
        request: waf_openapi_20170930_models.DescribeNeedUpgradeDomainLimitRequest,
    ) -> waf_openapi_20170930_models.DescribeNeedUpgradeDomainLimitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_need_upgrade_domain_limit_with_options(request, runtime)

    async def describe_need_upgrade_domain_limit_async(
        self,
        request: waf_openapi_20170930_models.DescribeNeedUpgradeDomainLimitRequest,
    ) -> waf_openapi_20170930_models.DescribeNeedUpgradeDomainLimitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_need_upgrade_domain_limit_with_options_async(request, runtime)

    def describe_package_with_options(
        self,
        request: waf_openapi_20170930_models.DescribePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackage',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_package_with_options_async(
        self,
        request: waf_openapi_20170930_models.DescribePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackage',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_package(
        self,
        request: waf_openapi_20170930_models.DescribePackageRequest,
    ) -> waf_openapi_20170930_models.DescribePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_package_with_options(request, runtime)

    async def describe_package_async(
        self,
        request: waf_openapi_20170930_models.DescribePackageRequest,
    ) -> waf_openapi_20170930_models.DescribePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_package_with_options_async(request, runtime)

    def describe_qps_with_options(
        self,
        request: waf_openapi_20170930_models.DescribeQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeQpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_millisecond):
            query['EndMillisecond'] = request.end_millisecond
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_millisecond):
            query['StartMillisecond'] = request.start_millisecond
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQps',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qps_with_options_async(
        self,
        request: waf_openapi_20170930_models.DescribeQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeQpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_millisecond):
            query['EndMillisecond'] = request.end_millisecond
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_millisecond):
            query['StartMillisecond'] = request.start_millisecond
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQps',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_qps(
        self,
        request: waf_openapi_20170930_models.DescribeQpsRequest,
    ) -> waf_openapi_20170930_models.DescribeQpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_qps_with_options(request, runtime)

    async def describe_qps_async(
        self,
        request: waf_openapi_20170930_models.DescribeQpsRequest,
    ) -> waf_openapi_20170930_models.DescribeQpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_qps_with_options_async(request, runtime)

    def describe_region_status_with_options(
        self,
        request: waf_openapi_20170930_models.DescribeRegionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeRegionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_source):
            query['InstanceSource'] = request.instance_source
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegionStatus',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeRegionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_region_status_with_options_async(
        self,
        request: waf_openapi_20170930_models.DescribeRegionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeRegionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_source):
            query['InstanceSource'] = request.instance_source
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegionStatus',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeRegionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_region_status(
        self,
        request: waf_openapi_20170930_models.DescribeRegionStatusRequest,
    ) -> waf_openapi_20170930_models.DescribeRegionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_region_status_with_options(request, runtime)

    async def describe_region_status_async(
        self,
        request: waf_openapi_20170930_models.DescribeRegionStatusRequest,
    ) -> waf_openapi_20170930_models.DescribeRegionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_region_status_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: waf_openapi_20170930_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: waf_openapi_20170930_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: waf_openapi_20170930_models.DescribeRegionsRequest,
    ) -> waf_openapi_20170930_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: waf_openapi_20170930_models.DescribeRegionsRequest,
    ) -> waf_openapi_20170930_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_transfer_config_in_work_with_options(
        self,
        request: waf_openapi_20170930_models.DescribeTransferConfigInWorkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeTransferConfigInWorkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_request_id):
            query['CheckRequestId'] = request.check_request_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransferConfigInWork',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeTransferConfigInWorkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transfer_config_in_work_with_options_async(
        self,
        request: waf_openapi_20170930_models.DescribeTransferConfigInWorkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.DescribeTransferConfigInWorkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_request_id):
            query['CheckRequestId'] = request.check_request_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransferConfigInWork',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.DescribeTransferConfigInWorkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transfer_config_in_work(
        self,
        request: waf_openapi_20170930_models.DescribeTransferConfigInWorkRequest,
    ) -> waf_openapi_20170930_models.DescribeTransferConfigInWorkResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_transfer_config_in_work_with_options(request, runtime)

    async def describe_transfer_config_in_work_async(
        self,
        request: waf_openapi_20170930_models.DescribeTransferConfigInWorkRequest,
    ) -> waf_openapi_20170930_models.DescribeTransferConfigInWorkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transfer_config_in_work_with_options_async(request, runtime)

    def get_qps_with_options(
        self,
        request: waf_openapi_20170930_models.GetQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.GetQpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.e):
            query['e'] = request.e
        if not UtilClient.is_unset(request.f):
            query['f'] = request.f
        if not UtilClient.is_unset(request.n):
            query['n'] = request.n
        if not UtilClient.is_unset(request.s):
            query['s'] = request.s
        if not UtilClient.is_unset(request.x):
            query['x'] = request.x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQps',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.GetQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qps_with_options_async(
        self,
        request: waf_openapi_20170930_models.GetQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.GetQpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.e):
            query['e'] = request.e
        if not UtilClient.is_unset(request.f):
            query['f'] = request.f
        if not UtilClient.is_unset(request.n):
            query['n'] = request.n
        if not UtilClient.is_unset(request.s):
            query['s'] = request.s
        if not UtilClient.is_unset(request.x):
            query['x'] = request.x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQps',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.GetQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qps(
        self,
        request: waf_openapi_20170930_models.GetQpsRequest,
    ) -> waf_openapi_20170930_models.GetQpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_qps_with_options(request, runtime)

    async def get_qps_async(
        self,
        request: waf_openapi_20170930_models.GetQpsRequest,
    ) -> waf_openapi_20170930_models.GetQpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_qps_with_options_async(request, runtime)

    def get_qps_total_with_options(
        self,
        request: waf_openapi_20170930_models.GetQpsTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.GetQpsTotalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.e):
            query['e'] = request.e
        if not UtilClient.is_unset(request.f):
            query['f'] = request.f
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.n):
            query['n'] = request.n
        if not UtilClient.is_unset(request.s):
            query['s'] = request.s
        if not UtilClient.is_unset(request.x):
            query['x'] = request.x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQpsTotal',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.GetQpsTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qps_total_with_options_async(
        self,
        request: waf_openapi_20170930_models.GetQpsTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.GetQpsTotalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.e):
            query['e'] = request.e
        if not UtilClient.is_unset(request.f):
            query['f'] = request.f
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.n):
            query['n'] = request.n
        if not UtilClient.is_unset(request.s):
            query['s'] = request.s
        if not UtilClient.is_unset(request.x):
            query['x'] = request.x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQpsTotal',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.GetQpsTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qps_total(
        self,
        request: waf_openapi_20170930_models.GetQpsTotalRequest,
    ) -> waf_openapi_20170930_models.GetQpsTotalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_qps_total_with_options(request, runtime)

    async def get_qps_total_async(
        self,
        request: waf_openapi_20170930_models.GetQpsTotalRequest,
    ) -> waf_openapi_20170930_models.GetQpsTotalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_qps_total_with_options_async(request, runtime)

    def get_region_list_with_options(
        self,
        request: waf_openapi_20170930_models.GetRegionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.GetRegionListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegionList',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.GetRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_region_list_with_options_async(
        self,
        request: waf_openapi_20170930_models.GetRegionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.GetRegionListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegionList',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.GetRegionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_region_list(
        self,
        request: waf_openapi_20170930_models.GetRegionListRequest,
    ) -> waf_openapi_20170930_models.GetRegionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_region_list_with_options(request, runtime)

    async def get_region_list_async(
        self,
        request: waf_openapi_20170930_models.GetRegionListRequest,
    ) -> waf_openapi_20170930_models.GetRegionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_region_list_with_options_async(request, runtime)

    def modify_cert_and_key_with_options(
        self,
        request: waf_openapi_20170930_models.ModifyCertAndKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.ModifyCertAndKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.cert):
            query['Cert'] = request.cert
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_cert_id):
            query['HttpsCertId'] = request.https_cert_id
        if not UtilClient.is_unset(request.https_cert_name):
            query['HttpsCertName'] = request.https_cert_name
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCertAndKey',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.ModifyCertAndKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cert_and_key_with_options_async(
        self,
        request: waf_openapi_20170930_models.ModifyCertAndKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.ModifyCertAndKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.cert):
            query['Cert'] = request.cert
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_cert_id):
            query['HttpsCertId'] = request.https_cert_id
        if not UtilClient.is_unset(request.https_cert_name):
            query['HttpsCertName'] = request.https_cert_name
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCertAndKey',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.ModifyCertAndKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cert_and_key(
        self,
        request: waf_openapi_20170930_models.ModifyCertAndKeyRequest,
    ) -> waf_openapi_20170930_models.ModifyCertAndKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cert_and_key_with_options(request, runtime)

    async def modify_cert_and_key_async(
        self,
        request: waf_openapi_20170930_models.ModifyCertAndKeyRequest,
    ) -> waf_openapi_20170930_models.ModifyCertAndKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cert_and_key_with_options_async(request, runtime)

    def modify_domain_config_with_options(
        self,
        request: waf_openapi_20170930_models.ModifyDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.ModifyDomainConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.http_to_user_ip):
            query['HttpToUserIp'] = request.http_to_user_ip
        if not UtilClient.is_unset(request.https_port):
            query['HttpsPort'] = request.https_port
        if not UtilClient.is_unset(request.https_redirect):
            query['HttpsRedirect'] = request.https_redirect
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_access_product):
            query['IsAccessProduct'] = request.is_access_product
        if not UtilClient.is_unset(request.is_non_standard_port):
            query['IsNonStandardPort'] = request.is_non_standard_port
        if not UtilClient.is_unset(request.load_balancing):
            query['LoadBalancing'] = request.load_balancing
        if not UtilClient.is_unset(request.protocols):
            query['Protocols'] = request.protocols
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        if not UtilClient.is_unset(request.source_ips):
            query['SourceIps'] = request.source_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainConfig',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.ModifyDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_config_with_options_async(
        self,
        request: waf_openapi_20170930_models.ModifyDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.ModifyDomainConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.http_to_user_ip):
            query['HttpToUserIp'] = request.http_to_user_ip
        if not UtilClient.is_unset(request.https_port):
            query['HttpsPort'] = request.https_port
        if not UtilClient.is_unset(request.https_redirect):
            query['HttpsRedirect'] = request.https_redirect
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_access_product):
            query['IsAccessProduct'] = request.is_access_product
        if not UtilClient.is_unset(request.is_non_standard_port):
            query['IsNonStandardPort'] = request.is_non_standard_port
        if not UtilClient.is_unset(request.load_balancing):
            query['LoadBalancing'] = request.load_balancing
        if not UtilClient.is_unset(request.protocols):
            query['Protocols'] = request.protocols
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        if not UtilClient.is_unset(request.source_ips):
            query['SourceIps'] = request.source_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainConfig',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.ModifyDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain_config(
        self,
        request: waf_openapi_20170930_models.ModifyDomainConfigRequest,
    ) -> waf_openapi_20170930_models.ModifyDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_config_with_options(request, runtime)

    async def modify_domain_config_async(
        self,
        request: waf_openapi_20170930_models.ModifyDomainConfigRequest,
    ) -> waf_openapi_20170930_models.ModifyDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_config_with_options_async(request, runtime)

    def modify_domain_package_count_with_options(
        self,
        request: waf_openapi_20170930_models.ModifyDomainPackageCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.ModifyDomainPackageCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_package_count):
            query['DomainPackageCount'] = request.domain_package_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainPackageCount',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.ModifyDomainPackageCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_package_count_with_options_async(
        self,
        request: waf_openapi_20170930_models.ModifyDomainPackageCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.ModifyDomainPackageCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_package_count):
            query['DomainPackageCount'] = request.domain_package_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainPackageCount',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.ModifyDomainPackageCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain_package_count(
        self,
        request: waf_openapi_20170930_models.ModifyDomainPackageCountRequest,
    ) -> waf_openapi_20170930_models.ModifyDomainPackageCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_package_count_with_options(request, runtime)

    async def modify_domain_package_count_async(
        self,
        request: waf_openapi_20170930_models.ModifyDomainPackageCountRequest,
    ) -> waf_openapi_20170930_models.ModifyDomainPackageCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_package_count_with_options_async(request, runtime)

    def modify_waf_switch_with_options(
        self,
        request: waf_openapi_20170930_models.ModifyWafSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.ModifyWafSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_on):
            query['ServiceOn'] = request.service_on
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWafSwitch',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.ModifyWafSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_waf_switch_with_options_async(
        self,
        request: waf_openapi_20170930_models.ModifyWafSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20170930_models.ModifyWafSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_on):
            query['ServiceOn'] = request.service_on
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWafSwitch',
            version='2017-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20170930_models.ModifyWafSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_waf_switch(
        self,
        request: waf_openapi_20170930_models.ModifyWafSwitchRequest,
    ) -> waf_openapi_20170930_models.ModifyWafSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_waf_switch_with_options(request, runtime)

    async def modify_waf_switch_async(
        self,
        request: waf_openapi_20170930_models.ModifyWafSwitchRequest,
    ) -> waf_openapi_20170930_models.ModifyWafSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_waf_switch_with_options_async(request, runtime)
