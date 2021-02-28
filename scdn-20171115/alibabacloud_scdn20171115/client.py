# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_scdn20171115 import models as scdn_20171115_models
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
            'ap-northeast-1': 'scdn.aliyuncs.com',
            'ap-northeast-2-pop': 'scdn.aliyuncs.com',
            'ap-south-1': 'scdn.aliyuncs.com',
            'ap-southeast-1': 'scdn.aliyuncs.com',
            'ap-southeast-2': 'scdn.aliyuncs.com',
            'ap-southeast-3': 'scdn.aliyuncs.com',
            'ap-southeast-5': 'scdn.aliyuncs.com',
            'cn-beijing': 'scdn.aliyuncs.com',
            'cn-beijing-finance-1': 'scdn.aliyuncs.com',
            'cn-beijing-finance-pop': 'scdn.aliyuncs.com',
            'cn-beijing-gov-1': 'scdn.aliyuncs.com',
            'cn-beijing-nu16-b01': 'scdn.aliyuncs.com',
            'cn-chengdu': 'scdn.aliyuncs.com',
            'cn-edge-1': 'scdn.aliyuncs.com',
            'cn-fujian': 'scdn.aliyuncs.com',
            'cn-haidian-cm12-c01': 'scdn.aliyuncs.com',
            'cn-hangzhou': 'scdn.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'scdn.aliyuncs.com',
            'cn-hangzhou-finance': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'scdn.aliyuncs.com',
            'cn-hangzhou-test-306': 'scdn.aliyuncs.com',
            'cn-hongkong': 'scdn.aliyuncs.com',
            'cn-hongkong-finance-pop': 'scdn.aliyuncs.com',
            'cn-huhehaote': 'scdn.aliyuncs.com',
            'cn-north-2-gov-1': 'scdn.aliyuncs.com',
            'cn-qingdao': 'scdn.aliyuncs.com',
            'cn-qingdao-nebula': 'scdn.aliyuncs.com',
            'cn-shanghai': 'scdn.aliyuncs.com',
            'cn-shanghai-et15-b01': 'scdn.aliyuncs.com',
            'cn-shanghai-et2-b01': 'scdn.aliyuncs.com',
            'cn-shanghai-finance-1': 'scdn.aliyuncs.com',
            'cn-shanghai-inner': 'scdn.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'scdn.aliyuncs.com',
            'cn-shenzhen': 'scdn.aliyuncs.com',
            'cn-shenzhen-finance-1': 'scdn.aliyuncs.com',
            'cn-shenzhen-inner': 'scdn.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'scdn.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'scdn.aliyuncs.com',
            'cn-wuhan': 'scdn.aliyuncs.com',
            'cn-yushanfang': 'scdn.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'scdn.aliyuncs.com',
            'cn-zhangjiakou': 'scdn.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'scdn.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'scdn.aliyuncs.com',
            'eu-central-1': 'scdn.aliyuncs.com',
            'eu-west-1': 'scdn.aliyuncs.com',
            'eu-west-1-oxs': 'scdn.aliyuncs.com',
            'me-east-1': 'scdn.aliyuncs.com',
            'rus-west-1-pop': 'scdn.aliyuncs.com',
            'us-east-1': 'scdn.aliyuncs.com',
            'us-west-1': 'scdn.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('scdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.AddScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.AddScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.AddScdnDomainResponse().from_map(
            self.do_rpcrequest('AddScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.AddScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.AddScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.AddScdnDomainResponse().from_map(
            await self.do_rpcrequest_async('AddScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_scdn_domain(
        self,
        request: scdn_20171115_models.AddScdnDomainRequest,
    ) -> scdn_20171115_models.AddScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_scdn_domain_with_options(request, runtime)

    async def add_scdn_domain_async(
        self,
        request: scdn_20171115_models.AddScdnDomainRequest,
    ) -> scdn_20171115_models.AddScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_scdn_domain_with_options_async(request, runtime)

    def batch_delete_scdn_domain_configs_with_options(
        self,
        request: scdn_20171115_models.BatchDeleteScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse().from_map(
            self.do_rpcrequest('BatchDeleteScdnDomainConfigs', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_delete_scdn_domain_configs_with_options_async(
        self,
        request: scdn_20171115_models.BatchDeleteScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('BatchDeleteScdnDomainConfigs', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_delete_scdn_domain_configs(
        self,
        request: scdn_20171115_models.BatchDeleteScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_scdn_domain_configs_with_options(request, runtime)

    async def batch_delete_scdn_domain_configs_async(
        self,
        request: scdn_20171115_models.BatchDeleteScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_scdn_domain_configs_with_options_async(request, runtime)

    def batch_set_scdn_domain_configs_with_options(
        self,
        request: scdn_20171115_models.BatchSetScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchSetScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.BatchSetScdnDomainConfigsResponse().from_map(
            self.do_rpcrequest('BatchSetScdnDomainConfigs', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_scdn_domain_configs_with_options_async(
        self,
        request: scdn_20171115_models.BatchSetScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchSetScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.BatchSetScdnDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('BatchSetScdnDomainConfigs', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_set_scdn_domain_configs(
        self,
        request: scdn_20171115_models.BatchSetScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.BatchSetScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_scdn_domain_configs_with_options(request, runtime)

    async def batch_set_scdn_domain_configs_async(
        self,
        request: scdn_20171115_models.BatchSetScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.BatchSetScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_scdn_domain_configs_with_options_async(request, runtime)

    def batch_update_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.BatchUpdateScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchUpdateScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.BatchUpdateScdnDomainResponse().from_map(
            self.do_rpcrequest('BatchUpdateScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_update_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.BatchUpdateScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.BatchUpdateScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.BatchUpdateScdnDomainResponse().from_map(
            await self.do_rpcrequest_async('BatchUpdateScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_update_scdn_domain(
        self,
        request: scdn_20171115_models.BatchUpdateScdnDomainRequest,
    ) -> scdn_20171115_models.BatchUpdateScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_update_scdn_domain_with_options(request, runtime)

    async def batch_update_scdn_domain_async(
        self,
        request: scdn_20171115_models.BatchUpdateScdnDomainRequest,
    ) -> scdn_20171115_models.BatchUpdateScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_update_scdn_domain_with_options_async(request, runtime)

    def check_scdn_service_with_options(
        self,
        request: scdn_20171115_models.CheckScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.CheckScdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.CheckScdnServiceResponse().from_map(
            self.do_rpcrequest('CheckScdnService', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_scdn_service_with_options_async(
        self,
        request: scdn_20171115_models.CheckScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.CheckScdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.CheckScdnServiceResponse().from_map(
            await self.do_rpcrequest_async('CheckScdnService', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_scdn_service(
        self,
        request: scdn_20171115_models.CheckScdnServiceRequest,
    ) -> scdn_20171115_models.CheckScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_scdn_service_with_options(request, runtime)

    async def check_scdn_service_async(
        self,
        request: scdn_20171115_models.CheckScdnServiceRequest,
    ) -> scdn_20171115_models.CheckScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_scdn_service_with_options_async(request, runtime)

    def delete_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.DeleteScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DeleteScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DeleteScdnDomainResponse().from_map(
            self.do_rpcrequest('DeleteScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.DeleteScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DeleteScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DeleteScdnDomainResponse().from_map(
            await self.do_rpcrequest_async('DeleteScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scdn_domain(
        self,
        request: scdn_20171115_models.DeleteScdnDomainRequest,
    ) -> scdn_20171115_models.DeleteScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scdn_domain_with_options(request, runtime)

    async def delete_scdn_domain_async(
        self,
        request: scdn_20171115_models.DeleteScdnDomainRequest,
    ) -> scdn_20171115_models.DeleteScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scdn_domain_with_options_async(request, runtime)

    def delete_scdn_specific_config_with_options(
        self,
        request: scdn_20171115_models.DeleteScdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DeleteScdnSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DeleteScdnSpecificConfigResponse().from_map(
            self.do_rpcrequest('DeleteScdnSpecificConfig', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scdn_specific_config_with_options_async(
        self,
        request: scdn_20171115_models.DeleteScdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DeleteScdnSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DeleteScdnSpecificConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteScdnSpecificConfig', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scdn_specific_config(
        self,
        request: scdn_20171115_models.DeleteScdnSpecificConfigRequest,
    ) -> scdn_20171115_models.DeleteScdnSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scdn_specific_config_with_options(request, runtime)

    async def delete_scdn_specific_config_async(
        self,
        request: scdn_20171115_models.DeleteScdnSpecificConfigRequest,
    ) -> scdn_20171115_models.DeleteScdnSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scdn_specific_config_with_options_async(request, runtime)

    def describe_scdn_cc_qps_info_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnCcQpsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcQpsInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnCcQpsInfoResponse().from_map(
            self.do_rpcrequest('DescribeScdnCcQpsInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_cc_qps_info_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcQpsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcQpsInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnCcQpsInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnCcQpsInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_cc_qps_info(
        self,
        request: scdn_20171115_models.DescribeScdnCcQpsInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnCcQpsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_cc_qps_info_with_options(request, runtime)

    async def describe_scdn_cc_qps_info_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcQpsInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnCcQpsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_cc_qps_info_with_options_async(request, runtime)

    def describe_scdn_cc_top_ip_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcTopIpResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnCcTopIpResponse().from_map(
            self.do_rpcrequest('DescribeScdnCcTopIp', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_cc_top_ip_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcTopIpResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnCcTopIpResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnCcTopIp', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_cc_top_ip(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopIpRequest,
    ) -> scdn_20171115_models.DescribeScdnCcTopIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_cc_top_ip_with_options(request, runtime)

    async def describe_scdn_cc_top_ip_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopIpRequest,
    ) -> scdn_20171115_models.DescribeScdnCcTopIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_cc_top_ip_with_options_async(request, runtime)

    def describe_scdn_cc_top_url_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcTopUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnCcTopUrlResponse().from_map(
            self.do_rpcrequest('DescribeScdnCcTopUrl', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_cc_top_url_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCcTopUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnCcTopUrlResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnCcTopUrl', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_cc_top_url(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopUrlRequest,
    ) -> scdn_20171115_models.DescribeScdnCcTopUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_cc_top_url_with_options(request, runtime)

    async def describe_scdn_cc_top_url_async(
        self,
        request: scdn_20171115_models.DescribeScdnCcTopUrlRequest,
    ) -> scdn_20171115_models.DescribeScdnCcTopUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_cc_top_url_with_options_async(request, runtime)

    def describe_scdn_certificate_detail_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCertificateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnCertificateDetailResponse().from_map(
            self.do_rpcrequest('DescribeScdnCertificateDetail', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_certificate_detail_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCertificateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnCertificateDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnCertificateDetail', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_certificate_detail(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateDetailRequest,
    ) -> scdn_20171115_models.DescribeScdnCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_certificate_detail_with_options(request, runtime)

    async def describe_scdn_certificate_detail_async(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateDetailRequest,
    ) -> scdn_20171115_models.DescribeScdnCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_certificate_detail_with_options_async(request, runtime)

    def describe_scdn_certificate_list_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnCertificateListResponse().from_map(
            self.do_rpcrequest('DescribeScdnCertificateList', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_certificate_list_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnCertificateListResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnCertificateList', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_certificate_list(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateListRequest,
    ) -> scdn_20171115_models.DescribeScdnCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_certificate_list_with_options(request, runtime)

    async def describe_scdn_certificate_list_async(
        self,
        request: scdn_20171115_models.DescribeScdnCertificateListRequest,
    ) -> scdn_20171115_models.DescribeScdnCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_certificate_list_with_options_async(request, runtime)

    def describe_scdn_ddo_sinfo_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDDoSInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDDoSInfoResponse().from_map(
            self.do_rpcrequest('DescribeScdnDDoSInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_ddo_sinfo_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDDoSInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDDoSInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDDoSInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_ddo_sinfo(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDDoSInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_ddo_sinfo_with_options(request, runtime)

    async def describe_scdn_ddo_sinfo_async(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDDoSInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_ddo_sinfo_with_options_async(request, runtime)

    def describe_scdn_ddo_straffic_info_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSTrafficInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse().from_map(
            self.do_rpcrequest('DescribeScdnDDoSTrafficInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_ddo_straffic_info_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSTrafficInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDDoSTrafficInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_ddo_straffic_info(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSTrafficInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_ddo_straffic_info_with_options(request, runtime)

    async def describe_scdn_ddo_straffic_info_async(
        self,
        request: scdn_20171115_models.DescribeScdnDDoSTrafficInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_ddo_straffic_info_with_options_async(request, runtime)

    def describe_scdn_domain_bps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainBpsData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_bps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainBpsData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_bps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_bps_data_with_options(request, runtime)

    async def describe_scdn_domain_bps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_bps_data_with_options_async(request, runtime)

    def describe_scdn_domain_certificate_info_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainCertificateInfo', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_certificate_info_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainCertificateInfo', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_certificate_info(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCertificateInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_certificate_info_with_options(request, runtime)

    async def describe_scdn_domain_certificate_info_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCertificateInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_certificate_info_with_options_async(request, runtime)

    def describe_scdn_domain_cname_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainCnameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDomainCnameResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainCname', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_cname_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainCnameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDomainCnameResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainCname', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_cname(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCnameRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainCnameResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_cname_with_options(request, runtime)

    async def describe_scdn_domain_cname_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainCnameRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainCnameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_cname_with_options_async(request, runtime)

    def describe_scdn_domain_configs_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainConfigsResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainConfigs', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_configs_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainConfigs', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_configs(
        self,
        request: scdn_20171115_models.DescribeScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_configs_with_options(request, runtime)

    async def describe_scdn_domain_configs_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainConfigsRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_configs_with_options_async(request, runtime)

    def describe_scdn_domain_detail_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainDetailResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainDetail', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_detail_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainDetail', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_detail(
        self,
        request: scdn_20171115_models.DescribeScdnDomainDetailRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_detail_with_options(request, runtime)

    async def describe_scdn_domain_detail_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainDetailRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_detail_with_options_async(request, runtime)

    def describe_scdn_domain_hit_rate_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainHitRateDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainHitRateData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_hit_rate_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainHitRateDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainHitRateData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_hit_rate_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_hit_rate_data_with_options(request, runtime)

    async def describe_scdn_domain_hit_rate_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_scdn_domain_http_code_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainHttpCodeData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_http_code_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainHttpCodeData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_http_code_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHttpCodeDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_http_code_data_with_options(request, runtime)

    async def describe_scdn_domain_http_code_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainHttpCodeDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_http_code_data_with_options_async(request, runtime)

    def describe_scdn_domain_isp_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainIspDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainIspDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainIspDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainIspData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_isp_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainIspDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainIspDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainIspDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainIspData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_isp_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainIspDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainIspDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_isp_data_with_options(request, runtime)

    async def describe_scdn_domain_isp_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainIspDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainIspDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_isp_data_with_options_async(request, runtime)

    def describe_scdn_domain_log_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainLogResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainLog', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_log_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainLog', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_log(
        self,
        request: scdn_20171115_models.DescribeScdnDomainLogRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_log_with_options(request, runtime)

    async def describe_scdn_domain_log_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainLogRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_log_with_options_async(request, runtime)

    def describe_scdn_domain_origin_bps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainOriginBpsData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_origin_bps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainOriginBpsData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_origin_bps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_origin_bps_data_with_options(request, runtime)

    async def describe_scdn_domain_origin_bps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_origin_bps_data_with_options_async(request, runtime)

    def describe_scdn_domain_origin_traffic_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainOriginTrafficData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_origin_traffic_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainOriginTrafficData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_origin_traffic_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_origin_traffic_data_with_options(request, runtime)

    async def describe_scdn_domain_origin_traffic_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainOriginTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_origin_traffic_data_with_options_async(request, runtime)

    def describe_scdn_domain_pv_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainPvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainPvDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainPvData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_pv_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainPvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainPvDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainPvData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_pv_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainPvDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainPvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_pv_data_with_options(request, runtime)

    async def describe_scdn_domain_pv_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainPvDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainPvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_pv_data_with_options_async(request, runtime)

    def describe_scdn_domain_qps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainQpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainQpsDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainQpsData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_qps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainQpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainQpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainQpsData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_qps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainQpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_qps_data_with_options(request, runtime)

    async def describe_scdn_domain_qps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainQpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_qps_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_bps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainRealTimeBpsData', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_real_time_bps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainRealTimeBpsData', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_real_time_bps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_bps_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_bps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_bps_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_byte_hit_rate_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainRealTimeByteHitRateData', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_real_time_byte_hit_rate_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainRealTimeByteHitRateData', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_real_time_byte_hit_rate_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_byte_hit_rate_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_byte_hit_rate_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_http_code_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainRealTimeHttpCodeData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_real_time_http_code_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainRealTimeHttpCodeData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_real_time_http_code_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_http_code_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_qps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainRealTimeQpsData', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_real_time_qps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainRealTimeQpsData', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_real_time_qps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_qps_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_qps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_qps_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_req_hit_rate_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainRealTimeReqHitRateData', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_real_time_req_hit_rate_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainRealTimeReqHitRateData', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_real_time_req_hit_rate_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_req_hit_rate_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_req_hit_rate_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_src_bps_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainRealTimeSrcBpsData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_real_time_src_bps_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainRealTimeSrcBpsData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_real_time_src_bps_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_src_bps_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_src_bps_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_src_bps_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_src_traffic_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainRealTimeSrcTrafficData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_real_time_src_traffic_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainRealTimeSrcTrafficData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_real_time_src_traffic_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_src_traffic_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_src_traffic_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_src_traffic_data_with_options_async(request, runtime)

    def describe_scdn_domain_real_time_traffic_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainRealTimeTrafficData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_real_time_traffic_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainRealTimeTrafficData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_real_time_traffic_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_scdn_domain_real_time_traffic_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_scdn_domain_region_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRegionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainRegionDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainRegionData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_region_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainRegionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainRegionDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainRegionData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_region_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRegionDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_region_data_with_options(request, runtime)

    async def describe_scdn_domain_region_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainRegionDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_region_data_with_options_async(request, runtime)

    def describe_scdn_domain_top_refer_visit_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainTopReferVisit', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_top_refer_visit_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainTopReferVisit', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_top_refer_visit(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopReferVisitRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_top_refer_visit_with_options(request, runtime)

    async def describe_scdn_domain_top_refer_visit_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopReferVisitRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_top_refer_visit_with_options_async(request, runtime)

    def describe_scdn_domain_top_url_visit_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainTopUrlVisit', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_top_url_visit_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainTopUrlVisit', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_top_url_visit(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopUrlVisitRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_top_url_visit_with_options(request, runtime)

    async def describe_scdn_domain_top_url_visit_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTopUrlVisitRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_top_url_visit_with_options_async(request, runtime)

    def describe_scdn_domain_traffic_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainTrafficData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_traffic_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainTrafficData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_traffic_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_traffic_data_with_options(request, runtime)

    async def describe_scdn_domain_traffic_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainTrafficDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_traffic_data_with_options_async(request, runtime)

    def describe_scdn_domain_uv_data_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainUvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainUvDataResponse().from_map(
            self.do_rpcrequest('DescribeScdnDomainUvData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_domain_uv_data_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnDomainUvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnDomainUvDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnDomainUvData', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_domain_uv_data(
        self,
        request: scdn_20171115_models.DescribeScdnDomainUvDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_uv_data_with_options(request, runtime)

    async def describe_scdn_domain_uv_data_async(
        self,
        request: scdn_20171115_models.DescribeScdnDomainUvDataRequest,
    ) -> scdn_20171115_models.DescribeScdnDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_domain_uv_data_with_options_async(request, runtime)

    def describe_scdn_refresh_quota_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnRefreshQuotaResponse().from_map(
            self.do_rpcrequest('DescribeScdnRefreshQuota', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_refresh_quota_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnRefreshQuotaResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnRefreshQuota', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_refresh_quota(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshQuotaRequest,
    ) -> scdn_20171115_models.DescribeScdnRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_refresh_quota_with_options(request, runtime)

    async def describe_scdn_refresh_quota_async(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshQuotaRequest,
    ) -> scdn_20171115_models.DescribeScdnRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_refresh_quota_with_options_async(request, runtime)

    def describe_scdn_refresh_tasks_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnRefreshTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnRefreshTasksResponse().from_map(
            self.do_rpcrequest('DescribeScdnRefreshTasks', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_refresh_tasks_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnRefreshTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnRefreshTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnRefreshTasks', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_refresh_tasks(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshTasksRequest,
    ) -> scdn_20171115_models.DescribeScdnRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_refresh_tasks_with_options(request, runtime)

    async def describe_scdn_refresh_tasks_async(
        self,
        request: scdn_20171115_models.DescribeScdnRefreshTasksRequest,
    ) -> scdn_20171115_models.DescribeScdnRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_refresh_tasks_with_options_async(request, runtime)

    def describe_scdn_service_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnServiceResponse().from_map(
            self.do_rpcrequest('DescribeScdnService', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_service_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnServiceResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnService', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_service(
        self,
        request: scdn_20171115_models.DescribeScdnServiceRequest,
    ) -> scdn_20171115_models.DescribeScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_service_with_options(request, runtime)

    async def describe_scdn_service_async(
        self,
        request: scdn_20171115_models.DescribeScdnServiceRequest,
    ) -> scdn_20171115_models.DescribeScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_service_with_options_async(request, runtime)

    def describe_scdn_top_domains_by_flow_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse().from_map(
            self.do_rpcrequest('DescribeScdnTopDomainsByFlow', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_top_domains_by_flow_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnTopDomainsByFlow', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_top_domains_by_flow(
        self,
        request: scdn_20171115_models.DescribeScdnTopDomainsByFlowRequest,
    ) -> scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_top_domains_by_flow_with_options(request, runtime)

    async def describe_scdn_top_domains_by_flow_async(
        self,
        request: scdn_20171115_models.DescribeScdnTopDomainsByFlowRequest,
    ) -> scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_top_domains_by_flow_with_options_async(request, runtime)

    def describe_scdn_user_domains_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnUserDomainsResponse().from_map(
            self.do_rpcrequest('DescribeScdnUserDomains', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_user_domains_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnUserDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnUserDomains', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_user_domains(
        self,
        request: scdn_20171115_models.DescribeScdnUserDomainsRequest,
    ) -> scdn_20171115_models.DescribeScdnUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_user_domains_with_options(request, runtime)

    async def describe_scdn_user_domains_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserDomainsRequest,
    ) -> scdn_20171115_models.DescribeScdnUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_user_domains_with_options_async(request, runtime)

    def describe_scdn_user_protect_info_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnUserProtectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserProtectInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnUserProtectInfoResponse().from_map(
            self.do_rpcrequest('DescribeScdnUserProtectInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_user_protect_info_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserProtectInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserProtectInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.DescribeScdnUserProtectInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnUserProtectInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_scdn_user_protect_info(
        self,
        request: scdn_20171115_models.DescribeScdnUserProtectInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnUserProtectInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_user_protect_info_with_options(request, runtime)

    async def describe_scdn_user_protect_info_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserProtectInfoRequest,
    ) -> scdn_20171115_models.DescribeScdnUserProtectInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_user_protect_info_with_options_async(request, runtime)

    def describe_scdn_user_quota_with_options(
        self,
        request: scdn_20171115_models.DescribeScdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnUserQuotaResponse().from_map(
            self.do_rpcrequest('DescribeScdnUserQuota', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scdn_user_quota_with_options_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.DescribeScdnUserQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.DescribeScdnUserQuotaResponse().from_map(
            await self.do_rpcrequest_async('DescribeScdnUserQuota', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scdn_user_quota(
        self,
        request: scdn_20171115_models.DescribeScdnUserQuotaRequest,
    ) -> scdn_20171115_models.DescribeScdnUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_user_quota_with_options(request, runtime)

    async def describe_scdn_user_quota_async(
        self,
        request: scdn_20171115_models.DescribeScdnUserQuotaRequest,
    ) -> scdn_20171115_models.DescribeScdnUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scdn_user_quota_with_options_async(request, runtime)

    def open_scdn_service_with_options(
        self,
        request: scdn_20171115_models.OpenScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.OpenScdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.OpenScdnServiceResponse().from_map(
            self.do_rpcrequest('OpenScdnService', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_scdn_service_with_options_async(
        self,
        request: scdn_20171115_models.OpenScdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.OpenScdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.OpenScdnServiceResponse().from_map(
            await self.do_rpcrequest_async('OpenScdnService', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_scdn_service(
        self,
        request: scdn_20171115_models.OpenScdnServiceRequest,
    ) -> scdn_20171115_models.OpenScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_scdn_service_with_options(request, runtime)

    async def open_scdn_service_async(
        self,
        request: scdn_20171115_models.OpenScdnServiceRequest,
    ) -> scdn_20171115_models.OpenScdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_scdn_service_with_options_async(request, runtime)

    def preload_scdn_object_caches_with_options(
        self,
        request: scdn_20171115_models.PreloadScdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.PreloadScdnObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.PreloadScdnObjectCachesResponse().from_map(
            self.do_rpcrequest('PreloadScdnObjectCaches', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def preload_scdn_object_caches_with_options_async(
        self,
        request: scdn_20171115_models.PreloadScdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.PreloadScdnObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.PreloadScdnObjectCachesResponse().from_map(
            await self.do_rpcrequest_async('PreloadScdnObjectCaches', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def preload_scdn_object_caches(
        self,
        request: scdn_20171115_models.PreloadScdnObjectCachesRequest,
    ) -> scdn_20171115_models.PreloadScdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.preload_scdn_object_caches_with_options(request, runtime)

    async def preload_scdn_object_caches_async(
        self,
        request: scdn_20171115_models.PreloadScdnObjectCachesRequest,
    ) -> scdn_20171115_models.PreloadScdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preload_scdn_object_caches_with_options_async(request, runtime)

    def refresh_scdn_object_caches_with_options(
        self,
        request: scdn_20171115_models.RefreshScdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.RefreshScdnObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.RefreshScdnObjectCachesResponse().from_map(
            self.do_rpcrequest('RefreshScdnObjectCaches', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_scdn_object_caches_with_options_async(
        self,
        request: scdn_20171115_models.RefreshScdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.RefreshScdnObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.RefreshScdnObjectCachesResponse().from_map(
            await self.do_rpcrequest_async('RefreshScdnObjectCaches', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_scdn_object_caches(
        self,
        request: scdn_20171115_models.RefreshScdnObjectCachesRequest,
    ) -> scdn_20171115_models.RefreshScdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_scdn_object_caches_with_options(request, runtime)

    async def refresh_scdn_object_caches_async(
        self,
        request: scdn_20171115_models.RefreshScdnObjectCachesRequest,
    ) -> scdn_20171115_models.RefreshScdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_scdn_object_caches_with_options_async(request, runtime)

    def set_scdn_bot_info_with_options(
        self,
        request: scdn_20171115_models.SetScdnBotInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnBotInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.SetScdnBotInfoResponse().from_map(
            self.do_rpcrequest('SetScdnBotInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def set_scdn_bot_info_with_options_async(
        self,
        request: scdn_20171115_models.SetScdnBotInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnBotInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.SetScdnBotInfoResponse().from_map(
            await self.do_rpcrequest_async('SetScdnBotInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_scdn_bot_info(
        self,
        request: scdn_20171115_models.SetScdnBotInfoRequest,
    ) -> scdn_20171115_models.SetScdnBotInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_bot_info_with_options(request, runtime)

    async def set_scdn_bot_info_async(
        self,
        request: scdn_20171115_models.SetScdnBotInfoRequest,
    ) -> scdn_20171115_models.SetScdnBotInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scdn_bot_info_with_options_async(request, runtime)

    def set_scdn_cc_info_with_options(
        self,
        request: scdn_20171115_models.SetScdnCcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnCcInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.SetScdnCcInfoResponse().from_map(
            self.do_rpcrequest('SetScdnCcInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def set_scdn_cc_info_with_options_async(
        self,
        request: scdn_20171115_models.SetScdnCcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnCcInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.SetScdnCcInfoResponse().from_map(
            await self.do_rpcrequest_async('SetScdnCcInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_scdn_cc_info(
        self,
        request: scdn_20171115_models.SetScdnCcInfoRequest,
    ) -> scdn_20171115_models.SetScdnCcInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_cc_info_with_options(request, runtime)

    async def set_scdn_cc_info_async(
        self,
        request: scdn_20171115_models.SetScdnCcInfoRequest,
    ) -> scdn_20171115_models.SetScdnCcInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scdn_cc_info_with_options_async(request, runtime)

    def set_scdn_ddo_sinfo_with_options(
        self,
        request: scdn_20171115_models.SetScdnDDoSInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDDoSInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.SetScdnDDoSInfoResponse().from_map(
            self.do_rpcrequest('SetScdnDDoSInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def set_scdn_ddo_sinfo_with_options_async(
        self,
        request: scdn_20171115_models.SetScdnDDoSInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDDoSInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.SetScdnDDoSInfoResponse().from_map(
            await self.do_rpcrequest_async('SetScdnDDoSInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_scdn_ddo_sinfo(
        self,
        request: scdn_20171115_models.SetScdnDDoSInfoRequest,
    ) -> scdn_20171115_models.SetScdnDDoSInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_ddo_sinfo_with_options(request, runtime)

    async def set_scdn_ddo_sinfo_async(
        self,
        request: scdn_20171115_models.SetScdnDDoSInfoRequest,
    ) -> scdn_20171115_models.SetScdnDDoSInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scdn_ddo_sinfo_with_options_async(request, runtime)

    def set_scdn_domain_biz_info_with_options(
        self,
        request: scdn_20171115_models.SetScdnDomainBizInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDomainBizInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.SetScdnDomainBizInfoResponse().from_map(
            self.do_rpcrequest('SetScdnDomainBizInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def set_scdn_domain_biz_info_with_options_async(
        self,
        request: scdn_20171115_models.SetScdnDomainBizInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDomainBizInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return scdn_20171115_models.SetScdnDomainBizInfoResponse().from_map(
            await self.do_rpcrequest_async('SetScdnDomainBizInfo', '2017-11-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_scdn_domain_biz_info(
        self,
        request: scdn_20171115_models.SetScdnDomainBizInfoRequest,
    ) -> scdn_20171115_models.SetScdnDomainBizInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_domain_biz_info_with_options(request, runtime)

    async def set_scdn_domain_biz_info_async(
        self,
        request: scdn_20171115_models.SetScdnDomainBizInfoRequest,
    ) -> scdn_20171115_models.SetScdnDomainBizInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scdn_domain_biz_info_with_options_async(request, runtime)

    def set_scdn_domain_certificate_with_options(
        self,
        request: scdn_20171115_models.SetScdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.SetScdnDomainCertificateResponse().from_map(
            self.do_rpcrequest('SetScdnDomainCertificate', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_scdn_domain_certificate_with_options_async(
        self,
        request: scdn_20171115_models.SetScdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.SetScdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.SetScdnDomainCertificateResponse().from_map(
            await self.do_rpcrequest_async('SetScdnDomainCertificate', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_scdn_domain_certificate(
        self,
        request: scdn_20171115_models.SetScdnDomainCertificateRequest,
    ) -> scdn_20171115_models.SetScdnDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_domain_certificate_with_options(request, runtime)

    async def set_scdn_domain_certificate_async(
        self,
        request: scdn_20171115_models.SetScdnDomainCertificateRequest,
    ) -> scdn_20171115_models.SetScdnDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scdn_domain_certificate_with_options_async(request, runtime)

    def start_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.StartScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.StartScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.StartScdnDomainResponse().from_map(
            self.do_rpcrequest('StartScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.StartScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.StartScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.StartScdnDomainResponse().from_map(
            await self.do_rpcrequest_async('StartScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_scdn_domain(
        self,
        request: scdn_20171115_models.StartScdnDomainRequest,
    ) -> scdn_20171115_models.StartScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_scdn_domain_with_options(request, runtime)

    async def start_scdn_domain_async(
        self,
        request: scdn_20171115_models.StartScdnDomainRequest,
    ) -> scdn_20171115_models.StartScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_scdn_domain_with_options_async(request, runtime)

    def stop_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.StopScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.StopScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.StopScdnDomainResponse().from_map(
            self.do_rpcrequest('StopScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.StopScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.StopScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.StopScdnDomainResponse().from_map(
            await self.do_rpcrequest_async('StopScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_scdn_domain(
        self,
        request: scdn_20171115_models.StopScdnDomainRequest,
    ) -> scdn_20171115_models.StopScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_scdn_domain_with_options(request, runtime)

    async def stop_scdn_domain_async(
        self,
        request: scdn_20171115_models.StopScdnDomainRequest,
    ) -> scdn_20171115_models.StopScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_scdn_domain_with_options_async(request, runtime)

    def update_scdn_domain_with_options(
        self,
        request: scdn_20171115_models.UpdateScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.UpdateScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.UpdateScdnDomainResponse().from_map(
            self.do_rpcrequest('UpdateScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_scdn_domain_with_options_async(
        self,
        request: scdn_20171115_models.UpdateScdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> scdn_20171115_models.UpdateScdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return scdn_20171115_models.UpdateScdnDomainResponse().from_map(
            await self.do_rpcrequest_async('UpdateScdnDomain', '2017-11-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_scdn_domain(
        self,
        request: scdn_20171115_models.UpdateScdnDomainRequest,
    ) -> scdn_20171115_models.UpdateScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scdn_domain_with_options(request, runtime)

    async def update_scdn_domain_async(
        self,
        request: scdn_20171115_models.UpdateScdnDomainRequest,
    ) -> scdn_20171115_models.UpdateScdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scdn_domain_with_options_async(request, runtime)
