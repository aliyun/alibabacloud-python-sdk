# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dcdn20180115 import models as dcdn_20180115_models
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
            'ap-northeast-1': 'dcdn.aliyuncs.com',
            'ap-northeast-2-pop': 'dcdn.aliyuncs.com',
            'ap-south-1': 'dcdn.aliyuncs.com',
            'ap-southeast-1': 'dcdn.aliyuncs.com',
            'ap-southeast-2': 'dcdn.aliyuncs.com',
            'ap-southeast-3': 'dcdn.aliyuncs.com',
            'ap-southeast-5': 'dcdn.aliyuncs.com',
            'cn-beijing': 'dcdn.aliyuncs.com',
            'cn-beijing-finance-1': 'dcdn.aliyuncs.com',
            'cn-beijing-finance-pop': 'dcdn.aliyuncs.com',
            'cn-beijing-gov-1': 'dcdn.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dcdn.aliyuncs.com',
            'cn-chengdu': 'dcdn.aliyuncs.com',
            'cn-edge-1': 'dcdn.aliyuncs.com',
            'cn-fujian': 'dcdn.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dcdn.aliyuncs.com',
            'cn-hangzhou': 'dcdn.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dcdn.aliyuncs.com',
            'cn-hangzhou-finance': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dcdn.aliyuncs.com',
            'cn-hangzhou-test-306': 'dcdn.aliyuncs.com',
            'cn-hongkong': 'dcdn.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dcdn.aliyuncs.com',
            'cn-huhehaote': 'dcdn.aliyuncs.com',
            'cn-north-2-gov-1': 'dcdn.aliyuncs.com',
            'cn-qingdao': 'dcdn.aliyuncs.com',
            'cn-qingdao-nebula': 'dcdn.aliyuncs.com',
            'cn-shanghai': 'dcdn.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dcdn.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dcdn.aliyuncs.com',
            'cn-shanghai-finance-1': 'dcdn.aliyuncs.com',
            'cn-shanghai-inner': 'dcdn.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dcdn.aliyuncs.com',
            'cn-shenzhen': 'dcdn.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dcdn.aliyuncs.com',
            'cn-shenzhen-inner': 'dcdn.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dcdn.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dcdn.aliyuncs.com',
            'cn-wuhan': 'dcdn.aliyuncs.com',
            'cn-yushanfang': 'dcdn.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dcdn.aliyuncs.com',
            'cn-zhangjiakou': 'dcdn.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dcdn.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dcdn.aliyuncs.com',
            'eu-central-1': 'dcdn.aliyuncs.com',
            'eu-west-1': 'dcdn.aliyuncs.com',
            'eu-west-1-oxs': 'dcdn.aliyuncs.com',
            'me-east-1': 'dcdn.aliyuncs.com',
            'rus-west-1-pop': 'dcdn.aliyuncs.com',
            'us-east-1': 'dcdn.aliyuncs.com',
            'us-west-1': 'dcdn.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dcdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.AddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.AddDcdnDomainResponse().from_map(
            self.do_rpcrequest('AddDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.AddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.AddDcdnDomainResponse().from_map(
            await self.do_rpcrequest_async('AddDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_dcdn_domain(
        self,
        request: dcdn_20180115_models.AddDcdnDomainRequest,
    ) -> dcdn_20180115_models.AddDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_dcdn_domain_with_options(request, runtime)

    async def add_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.AddDcdnDomainRequest,
    ) -> dcdn_20180115_models.AddDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dcdn_domain_with_options_async(request, runtime)

    def add_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.AddDcdnIpaDomainResponse().from_map(
            self.do_rpcrequest('AddDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.AddDcdnIpaDomainResponse().from_map(
            await self.do_rpcrequest_async('AddDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_dcdn_ipa_domain(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_dcdn_ipa_domain_with_options(request, runtime)

    async def add_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.AddDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.AddDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_dcdn_ipa_domain_with_options_async(request, runtime)

    def batch_add_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchAddDcdnDomainResponse().from_map(
            self.do_rpcrequest('BatchAddDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_add_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchAddDcdnDomainResponse().from_map(
            await self.do_rpcrequest_async('BatchAddDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_add_dcdn_domain(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_add_dcdn_domain_with_options(request, runtime)

    async def batch_add_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.BatchAddDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchAddDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_dcdn_domain_with_options_async(request, runtime)

    def batch_delete_dcdn_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse().from_map(
            self.do_rpcrequest('BatchDeleteDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_delete_dcdn_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('BatchDeleteDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_delete_dcdn_domain_configs(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_dcdn_domain_configs_with_options(request, runtime)

    async def batch_delete_dcdn_domain_configs_async(
        self,
        request: dcdn_20180115_models.BatchDeleteDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_dcdn_domain_configs_with_options_async(request, runtime)

    def batch_set_dcdn_domain_certificate_with_options(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse().from_map(
            self.do_rpcrequest('BatchSetDcdnDomainCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_dcdn_domain_certificate_with_options_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse().from_map(
            await self.do_rpcrequest_async('BatchSetDcdnDomainCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_set_dcdn_domain_certificate(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_domain_certificate_with_options(request, runtime)

    async def batch_set_dcdn_domain_certificate_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainCertificateRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_dcdn_domain_certificate_with_options_async(request, runtime)

    def batch_set_dcdn_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse().from_map(
            self.do_rpcrequest('BatchSetDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_dcdn_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('BatchSetDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_set_dcdn_domain_configs(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_domain_configs_with_options(request, runtime)

    async def batch_set_dcdn_domain_configs_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_dcdn_domain_configs_with_options_async(request, runtime)

    def batch_set_dcdn_ipa_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse().from_map(
            self.do_rpcrequest('BatchSetDcdnIpaDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_dcdn_ipa_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('BatchSetDcdnIpaDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_set_dcdn_ipa_domain_configs(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_ipa_domain_configs_with_options(request, runtime)

    async def batch_set_dcdn_ipa_domain_configs_async(
        self,
        request: dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsRequest,
    ) -> dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_dcdn_ipa_domain_configs_with_options_async(request, runtime)

    def batch_start_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchStartDcdnDomainResponse().from_map(
            self.do_rpcrequest('BatchStartDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_start_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchStartDcdnDomainResponse().from_map(
            await self.do_rpcrequest_async('BatchStartDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_start_dcdn_domain(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_start_dcdn_domain_with_options(request, runtime)

    async def batch_start_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.BatchStartDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchStartDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_start_dcdn_domain_with_options_async(request, runtime)

    def batch_stop_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchStopDcdnDomainResponse().from_map(
            self.do_rpcrequest('BatchStopDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_stop_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.BatchStopDcdnDomainResponse().from_map(
            await self.do_rpcrequest_async('BatchStopDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_stop_dcdn_domain(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_dcdn_domain_with_options(request, runtime)

    async def batch_stop_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.BatchStopDcdnDomainRequest,
    ) -> dcdn_20180115_models.BatchStopDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_stop_dcdn_domain_with_options_async(request, runtime)

    def create_dcdn_certificate_signing_request_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnCertificateSigningRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse().from_map(
            self.do_rpcrequest('CreateDcdnCertificateSigningRequest', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dcdn_certificate_signing_request_with_options_async(
        self,
        request: dcdn_20180115_models.CreateDcdnCertificateSigningRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse().from_map(
            await self.do_rpcrequest_async('CreateDcdnCertificateSigningRequest', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dcdn_certificate_signing_request(
        self,
        request: dcdn_20180115_models.CreateDcdnCertificateSigningRequestRequest,
    ) -> dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_certificate_signing_request_with_options(request, runtime)

    async def create_dcdn_certificate_signing_request_async(
        self,
        request: dcdn_20180115_models.CreateDcdnCertificateSigningRequestRequest,
    ) -> dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_certificate_signing_request_with_options_async(request, runtime)

    def create_dcdn_domain_offline_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse().from_map(
            self.do_rpcrequest('CreateDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dcdn_domain_offline_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('CreateDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dcdn_domain_offline_log_delivery(
        self,
        request: dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_domain_offline_log_delivery_with_options(request, runtime)

    async def create_dcdn_domain_offline_log_delivery_async(
        self,
        request: dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dcdn_domain_offline_log_delivery_with_options_async(request, runtime)

    def delete_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DeleteDcdnDomainResponse().from_map(
            self.do_rpcrequest('DeleteDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DeleteDcdnDomainResponse().from_map(
            await self.do_rpcrequest_async('DeleteDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_domain(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_domain_with_options(request, runtime)

    async def delete_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnDomainRequest,
    ) -> dcdn_20180115_models.DeleteDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_domain_with_options_async(request, runtime)

    def delete_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DeleteDcdnIpaDomainResponse().from_map(
            self.do_rpcrequest('DeleteDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DeleteDcdnIpaDomainResponse().from_map(
            await self.do_rpcrequest_async('DeleteDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_ipa_domain(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_ipa_domain_with_options(request, runtime)

    async def delete_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.DeleteDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_ipa_domain_with_options_async(request, runtime)

    def delete_dcdn_ipa_specific_config_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse().from_map(
            self.do_rpcrequest('DeleteDcdnIpaSpecificConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_ipa_specific_config_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteDcdnIpaSpecificConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_ipa_specific_config(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_ipa_specific_config_with_options(request, runtime)

    async def delete_dcdn_ipa_specific_config_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnIpaSpecificConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_ipa_specific_config_with_options_async(request, runtime)

    def delete_dcdn_specific_config_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DeleteDcdnSpecificConfigResponse().from_map(
            self.do_rpcrequest('DeleteDcdnSpecificConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_specific_config_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DeleteDcdnSpecificConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteDcdnSpecificConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_specific_config(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_specific_config_with_options(request, runtime)

    async def delete_dcdn_specific_config_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_specific_config_with_options_async(request, runtime)

    def delete_dcdn_specific_staging_config_with_options(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse().from_map(
            self.do_rpcrequest('DeleteDcdnSpecificStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dcdn_specific_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteDcdnSpecificStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_specific_staging_config(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_specific_staging_config_with_options(request, runtime)

    async def delete_dcdn_specific_staging_config_async(
        self,
        request: dcdn_20180115_models.DeleteDcdnSpecificStagingConfigRequest,
    ) -> dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dcdn_specific_staging_config_with_options_async(request, runtime)

    def describe_dcdn_bgp_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnBgpBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_bgp_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnBgpBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_bgp_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_bgp_bps_data_with_options(request, runtime)

    async def describe_dcdn_bgp_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_bgp_bps_data_with_options_async(request, runtime)

    def describe_dcdn_bgp_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnBgpTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_bgp_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnBgpTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_bgp_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_bgp_traffic_data_with_options(request, runtime)

    async def describe_dcdn_bgp_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnBgpTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_bgp_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_certificate_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnCertificateDetailResponse().from_map(
            self.do_rpcrequest('DescribeDcdnCertificateDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_certificate_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnCertificateDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnCertificateDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_certificate_detail(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_certificate_detail_with_options(request, runtime)

    async def describe_dcdn_certificate_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_certificate_detail_with_options_async(request, runtime)

    def describe_dcdn_certificate_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnCertificateListResponse().from_map(
            self.do_rpcrequest('DescribeDcdnCertificateList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_certificate_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnCertificateListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnCertificateList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_certificate_list(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_certificate_list_with_options(request, runtime)

    async def describe_dcdn_certificate_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnCertificateListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_certificate_list_with_options_async(request, runtime)

    def describe_dcdn_config_of_version_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse().from_map(
            self.do_rpcrequest('DescribeDcdnConfigOfVersion', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_config_of_version_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnConfigOfVersion', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_config_of_version(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigOfVersionRequest,
    ) -> dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_config_of_version_with_options(request, runtime)

    async def describe_dcdn_config_of_version_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnConfigOfVersionRequest,
    ) -> dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_config_of_version_with_options_async(request, runtime)

    def describe_dcdn_domain_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_by_certificate_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainByCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_by_certificate_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainByCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_by_certificate(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_by_certificate_with_options(request, runtime)

    async def describe_dcdn_domain_by_certificate_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainByCertificateRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_by_certificate_with_options_async(request, runtime)

    def describe_dcdn_domain_certificate_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainCertificateInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_certificate_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainCertificateInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_certificate_info(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_certificate_info_with_options(request, runtime)

    async def describe_dcdn_domain_certificate_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCertificateInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_certificate_info_with_options_async(request, runtime)

    def describe_dcdn_domain_cname_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainCnameResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainCname', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_cname_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainCnameResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainCname', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_cname(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_cname_with_options(request, runtime)

    async def describe_dcdn_domain_cname_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainCnameRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainCnameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_cname_with_options_async(request, runtime)

    def describe_dcdn_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainConfigsResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_configs(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_configs_with_options(request, runtime)

    async def describe_dcdn_domain_configs_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_configs_with_options_async(request, runtime)

    def describe_dcdn_domain_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainDetailResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_detail(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_detail_with_options(request, runtime)

    async def describe_dcdn_domain_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_detail_with_options_async(request, runtime)

    def describe_dcdn_domain_hit_rate_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainHitRateData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_hit_rate_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainHitRateData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_hit_rate_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_hit_rate_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_http_code_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_ipa_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainIpaBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_ipa_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainIpaBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_ipa_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_ipa_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_ipa_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_ipa_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainIpaTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_ipa_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainIpaTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_ipa_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_ipa_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_ipa_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_isp_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainIspDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainIspData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_isp_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainIspDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainIspData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_isp_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_isp_data_with_options(request, runtime)

    async def describe_dcdn_domain_isp_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainIspDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainIspDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_isp_data_with_options_async(request, runtime)

    def describe_dcdn_domain_log_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainLogResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainLog', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_log_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainLog', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_log(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_log_with_options(request, runtime)

    async def describe_dcdn_domain_log_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainLogRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_log_with_options_async(request, runtime)

    def describe_dcdn_domain_multi_usage_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainMultiUsageData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_multi_usage_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainMultiUsageData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_multi_usage_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_multi_usage_data_with_options(request, runtime)

    async def describe_dcdn_domain_multi_usage_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_multi_usage_data_with_options_async(request, runtime)

    def describe_dcdn_domain_origin_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainOriginBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_origin_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainOriginBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_origin_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_origin_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_origin_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_origin_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_origin_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainOriginTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_origin_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainOriginTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_origin_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_origin_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_origin_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_origin_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_property_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainPropertyResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainProperty', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_property_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainPropertyResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainProperty', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_property(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_property_with_options(request, runtime)

    async def describe_dcdn_domain_property_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPropertyRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_property_with_options_async(request, runtime)

    def describe_dcdn_domain_pv_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainPvDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainPvData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_pv_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainPvDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainPvData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_pv_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPvDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_pv_data_with_options(request, runtime)

    async def describe_dcdn_domain_pv_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainPvDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainPvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_pv_data_with_options_async(request, runtime)

    def describe_dcdn_domain_qps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainQpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_qps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainQpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_qps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_qps_data_with_options(request, runtime)

    async def describe_dcdn_domain_qps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainQpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_qps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRealTimeBpsData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeBpsData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRealTimeByteHitRateData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_byte_hit_rate_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeByteHitRateData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_byte_hit_rate_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_byte_hit_rate_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_byte_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_detail_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRealTimeDetailData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_detail_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeDetailData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_detail_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_detail_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_detail_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_detail_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRealTimeHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_http_code_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_qps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRealTimeQpsData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_qps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeQpsData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_qps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_qps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_qps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_qps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_req_hit_rate_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRealTimeReqHitRateData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_req_hit_rate_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeReqHitRateData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_req_hit_rate_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_req_hit_rate_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_req_hit_rate_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRealTimeSrcBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeSrcBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_src_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRealTimeSrcHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeSrcHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_src_http_code_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_src_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRealTimeSrcTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_src_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeSrcTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_src_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_src_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_src_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_real_time_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRealTimeTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_real_time_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRealTimeTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_real_time_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_region_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainRegionData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_region_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainRegionData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_region_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_region_data_with_options(request, runtime)

    async def describe_dcdn_domain_region_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainRegionDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_region_data_with_options_async(request, runtime)

    def describe_dcdn_domain_staging_config_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_staging_config(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_staging_config_with_options(request, runtime)

    async def describe_dcdn_domain_staging_config_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainStagingConfigRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_staging_config_with_options_async(request, runtime)

    def describe_dcdn_domain_top_refer_visit_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainTopReferVisit', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_top_refer_visit_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainTopReferVisit', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_top_refer_visit(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_top_refer_visit_with_options(request, runtime)

    async def describe_dcdn_domain_top_refer_visit_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopReferVisitRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_top_refer_visit_with_options_async(request, runtime)

    def describe_dcdn_domain_top_url_visit_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainTopUrlVisit', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_top_url_visit_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainTopUrlVisit', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_top_url_visit(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_top_url_visit_with_options(request, runtime)

    async def describe_dcdn_domain_top_url_visit_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_top_url_visit_with_options_async(request, runtime)

    def describe_dcdn_domain_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_domain_uv_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainUvDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainUvData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_uv_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainUvDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainUvData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_uv_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_uv_data_with_options(request, runtime)

    async def describe_dcdn_domain_uv_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainUvDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_uv_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_bps_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainWebsocketBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_websocket_bps_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainWebsocketBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_websocket_bps_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_bps_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_bps_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_bps_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_http_code_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainWebsocketHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_websocket_http_code_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainWebsocketHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_websocket_http_code_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_http_code_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_http_code_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_http_code_data_with_options_async(request, runtime)

    def describe_dcdn_domain_websocket_traffic_data_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeDcdnDomainWebsocketTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_domain_websocket_traffic_data_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnDomainWebsocketTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_websocket_traffic_data(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_traffic_data_with_options(request, runtime)

    async def describe_dcdn_domain_websocket_traffic_data_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataRequest,
    ) -> dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_domain_websocket_traffic_data_with_options_async(request, runtime)

    def describe_dcdn_https_domain_list_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse().from_map(
            self.do_rpcrequest('DescribeDcdnHttpsDomainList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_https_domain_list_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnHttpsDomainList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_https_domain_list(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_https_domain_list_with_options(request, runtime)

    async def describe_dcdn_https_domain_list_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnHttpsDomainListRequest,
    ) -> dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_https_domain_list_with_options_async(request, runtime)

    def describe_dcdn_ipa_domain_configs_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse().from_map(
            self.do_rpcrequest('DescribeDcdnIpaDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_ipa_domain_configs_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnIpaDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_ipa_domain_configs(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_domain_configs_with_options(request, runtime)

    async def describe_dcdn_ipa_domain_configs_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainConfigsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_domain_configs_with_options_async(request, runtime)

    def describe_dcdn_ipa_domain_detail_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse().from_map(
            self.do_rpcrequest('DescribeDcdnIpaDomainDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_ipa_domain_detail_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnIpaDomainDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_ipa_domain_detail(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_domain_detail_with_options(request, runtime)

    async def describe_dcdn_ipa_domain_detail_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaDomainDetailRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_domain_detail_with_options_async(request, runtime)

    def describe_dcdn_ipa_service_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnIpaServiceResponse().from_map(
            self.do_rpcrequest('DescribeDcdnIpaService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_ipa_service_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnIpaServiceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnIpaService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_ipa_service(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_service_with_options(request, runtime)

    async def describe_dcdn_ipa_service_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_service_with_options_async(request, runtime)

    def describe_dcdn_ipa_user_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse().from_map(
            self.do_rpcrequest('DescribeDcdnIpaUserDomains', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_ipa_user_domains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnIpaUserDomains', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_ipa_user_domains(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_user_domains_with_options(request, runtime)

    async def describe_dcdn_ipa_user_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpaUserDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ipa_user_domains_with_options_async(request, runtime)

    def describe_dcdn_ip_info_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnIpInfoResponse().from_map(
            self.do_rpcrequest('DescribeDcdnIpInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_ip_info_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnIpInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnIpInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_ip_info(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ip_info_with_options(request, runtime)

    async def describe_dcdn_ip_info_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnIpInfoRequest,
    ) -> dcdn_20180115_models.DescribeDcdnIpInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_ip_info_with_options_async(request, runtime)

    def describe_dcdn_offline_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse().from_map(
            self.do_rpcrequest('DescribeDcdnOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_offline_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_with_options(request, runtime)

    async def describe_dcdn_offline_log_delivery_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_offline_log_delivery_with_options_async(request, runtime)

    def describe_dcdn_offline_log_delivery_field_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse().from_map(
            self.do_rpcrequest('DescribeDcdnOfflineLogDeliveryField', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_offline_log_delivery_field_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnOfflineLogDeliveryField', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery_field(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_field_with_options(request, runtime)

    async def describe_dcdn_offline_log_delivery_field_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_offline_log_delivery_field_with_options_async(request, runtime)

    def describe_dcdn_offline_log_delivery_regions_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse().from_map(
            self.do_rpcrequest('DescribeDcdnOfflineLogDeliveryRegions', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_offline_log_delivery_regions_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnOfflineLogDeliveryRegions', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery_regions(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_regions_with_options(request, runtime)

    async def describe_dcdn_offline_log_delivery_regions_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_offline_log_delivery_regions_with_options_async(request, runtime)

    def describe_dcdn_offline_log_delivery_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse().from_map(
            self.do_rpcrequest('DescribeDcdnOfflineLogDeliveryStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_offline_log_delivery_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnOfflineLogDeliveryStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery_status(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_status_with_options(request, runtime)

    async def describe_dcdn_offline_log_delivery_status_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusRequest,
    ) -> dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_offline_log_delivery_status_with_options_async(request, runtime)

    def describe_dcdn_refresh_quota_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse().from_map(
            self.do_rpcrequest('DescribeDcdnRefreshQuota', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_refresh_quota_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnRefreshQuota', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_refresh_quota(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_quota_with_options(request, runtime)

    async def describe_dcdn_refresh_quota_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshQuotaRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_refresh_quota_with_options_async(request, runtime)

    def describe_dcdn_refresh_tasks_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnRefreshTasksResponse().from_map(
            self.do_rpcrequest('DescribeDcdnRefreshTasks', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_refresh_tasks_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnRefreshTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnRefreshTasks', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_refresh_tasks(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_tasks_with_options(request, runtime)

    async def describe_dcdn_refresh_tasks_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRefreshTasksRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_refresh_tasks_with_options_async(request, runtime)

    def describe_dcdn_region_and_isp_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnRegionAndIspResponse().from_map(
            self.do_rpcrequest('DescribeDcdnRegionAndIsp', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_region_and_isp_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnRegionAndIspResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnRegionAndIsp', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_region_and_isp(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_region_and_isp_with_options(request, runtime)

    async def describe_dcdn_region_and_isp_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnRegionAndIspRequest,
    ) -> dcdn_20180115_models.DescribeDcdnRegionAndIspResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_region_and_isp_with_options_async(request, runtime)

    def describe_dcdn_service_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnServiceResponse().from_map(
            self.do_rpcrequest('DescribeDcdnService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_service_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnServiceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_service(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_service_with_options(request, runtime)

    async def describe_dcdn_service_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnServiceRequest,
    ) -> dcdn_20180115_models.DescribeDcdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_service_with_options_async(request, runtime)

    def describe_dcdn_staging_ip_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnStagingIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnStagingIpResponse().from_map(
            self.do_rpcrequest('DescribeDcdnStagingIp', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_staging_ip_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnStagingIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnStagingIpResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnStagingIp', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_staging_ip(
        self,
        request: dcdn_20180115_models.DescribeDcdnStagingIpRequest,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_staging_ip_with_options(request, runtime)

    async def describe_dcdn_staging_ip_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnStagingIpRequest,
    ) -> dcdn_20180115_models.DescribeDcdnStagingIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_staging_ip_with_options_async(request, runtime)

    def describe_dcdn_tag_resources_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnTagResourcesResponse().from_map(
            self.do_rpcrequest('DescribeDcdnTagResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_tag_resources_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnTagResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_tag_resources(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_tag_resources_with_options(request, runtime)

    async def describe_dcdn_tag_resources_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTagResourcesRequest,
    ) -> dcdn_20180115_models.DescribeDcdnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_tag_resources_with_options_async(request, runtime)

    def describe_dcdn_top_domains_by_flow_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse().from_map(
            self.do_rpcrequest('DescribeDcdnTopDomainsByFlow', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_top_domains_by_flow_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnTopDomainsByFlow', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_top_domains_by_flow(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_top_domains_by_flow_with_options(request, runtime)

    async def describe_dcdn_top_domains_by_flow_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnTopDomainsByFlowRequest,
    ) -> dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_top_domains_by_flow_with_options_async(request, runtime)

    def describe_dcdn_user_bill_history_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse().from_map(
            self.do_rpcrequest('DescribeDcdnUserBillHistory', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_bill_history_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnUserBillHistory', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_bill_history(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_bill_history_with_options(request, runtime)

    async def describe_dcdn_user_bill_history_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillHistoryRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_bill_history_with_options_async(request, runtime)

    def describe_dcdn_user_bill_type_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserBillTypeResponse().from_map(
            self.do_rpcrequest('DescribeDcdnUserBillType', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_bill_type_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserBillTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnUserBillType', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_bill_type(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillTypeRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_bill_type_with_options(request, runtime)

    async def describe_dcdn_user_bill_type_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserBillTypeRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserBillTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_bill_type_with_options_async(request, runtime)

    def describe_dcdn_user_domains_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserDomainsResponse().from_map(
            self.do_rpcrequest('DescribeDcdnUserDomains', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_domains_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnUserDomains', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_domains(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_domains_with_options(request, runtime)

    async def describe_dcdn_user_domains_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_domains_with_options_async(request, runtime)

    def describe_dcdn_user_domains_by_func_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse().from_map(
            self.do_rpcrequest('DescribeDcdnUserDomainsByFunc', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_domains_by_func_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnUserDomainsByFunc', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_domains_by_func(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_domains_by_func_with_options(request, runtime)

    async def describe_dcdn_user_domains_by_func_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserDomainsByFuncRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_domains_by_func_with_options_async(request, runtime)

    def describe_dcdn_user_quota_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserQuotaResponse().from_map(
            self.do_rpcrequest('DescribeDcdnUserQuota', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_quota_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserQuotaResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnUserQuota', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_quota(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_quota_with_options(request, runtime)

    async def describe_dcdn_user_quota_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserQuotaRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_quota_with_options_async(request, runtime)

    def describe_dcdn_user_resource_package_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse().from_map(
            self.do_rpcrequest('DescribeDcdnUserResourcePackage', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_resource_package_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnUserResourcePackage', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_resource_package(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_resource_package_with_options(request, runtime)

    async def describe_dcdn_user_resource_package_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserResourcePackageRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_resource_package_with_options_async(request, runtime)

    def describe_dcdn_user_sec_drop_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserSecDropResponse().from_map(
            self.do_rpcrequest('DescribeDcdnUserSecDrop', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_sec_drop_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserSecDropResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnUserSecDrop', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_sec_drop(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_with_options(request, runtime)

    async def describe_dcdn_user_sec_drop_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserSecDropRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserSecDropResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_sec_drop_with_options_async(request, runtime)

    def describe_dcdn_user_tags_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserTagsResponse().from_map(
            self.do_rpcrequest('DescribeDcdnUserTags', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_user_tags_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnUserTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnUserTags', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_tags(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserTagsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_tags_with_options(request, runtime)

    async def describe_dcdn_user_tags_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnUserTagsRequest,
    ) -> dcdn_20180115_models.DescribeDcdnUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_user_tags_with_options_async(request, runtime)

    def describe_dcdn_verify_content_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnVerifyContentResponse().from_map(
            self.do_rpcrequest('DescribeDcdnVerifyContent', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_verify_content_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnVerifyContentResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnVerifyContent', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_verify_content(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_verify_content_with_options(request, runtime)

    async def describe_dcdn_verify_content_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnVerifyContentRequest,
    ) -> dcdn_20180115_models.DescribeDcdnVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_verify_content_with_options_async(request, runtime)

    def describe_dcdn_waf_domain_with_options(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnWafDomainResponse().from_map(
            self.do_rpcrequest('DescribeDcdnWafDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dcdn_waf_domain_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeDcdnWafDomainResponse().from_map(
            await self.do_rpcrequest_async('DescribeDcdnWafDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_waf_domain(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_domain_with_options(request, runtime)

    async def describe_dcdn_waf_domain_async(
        self,
        request: dcdn_20180115_models.DescribeDcdnWafDomainRequest,
    ) -> dcdn_20180115_models.DescribeDcdnWafDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dcdn_waf_domain_with_options_async(request, runtime)

    def describe_user_dcdn_ipa_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse().from_map(
            self.do_rpcrequest('DescribeUserDcdnIpaStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_dcdn_ipa_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserDcdnIpaStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_dcdn_ipa_status(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_dcdn_ipa_status_with_options(request, runtime)

    async def describe_user_dcdn_ipa_status_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnIpaStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_dcdn_ipa_status_with_options_async(request, runtime)

    def describe_user_dcdn_status_with_options(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeUserDcdnStatusResponse().from_map(
            self.do_rpcrequest('DescribeUserDcdnStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_dcdn_status_with_options_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DescribeUserDcdnStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserDcdnStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_dcdn_status(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_dcdn_status_with_options(request, runtime)

    async def describe_user_dcdn_status_async(
        self,
        request: dcdn_20180115_models.DescribeUserDcdnStatusRequest,
    ) -> dcdn_20180115_models.DescribeUserDcdnStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_dcdn_status_with_options_async(request, runtime)

    def disable_dcdn_domain_offline_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse().from_map(
            self.do_rpcrequest('DisableDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_dcdn_domain_offline_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('DisableDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_dcdn_domain_offline_log_delivery(
        self,
        request: dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_dcdn_domain_offline_log_delivery_with_options(request, runtime)

    async def disable_dcdn_domain_offline_log_delivery_async(
        self,
        request: dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_dcdn_domain_offline_log_delivery_with_options_async(request, runtime)

    def disable_dcdn_offline_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.DisableDcdnOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse().from_map(
            self.do_rpcrequest('DisableDcdnOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_dcdn_offline_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.DisableDcdnOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('DisableDcdnOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_dcdn_offline_log_delivery(
        self,
        request: dcdn_20180115_models.DisableDcdnOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_dcdn_offline_log_delivery_with_options(request, runtime)

    async def disable_dcdn_offline_log_delivery_async(
        self,
        request: dcdn_20180115_models.DisableDcdnOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_dcdn_offline_log_delivery_with_options_async(request, runtime)

    def enable_dcdn_domain_offline_log_delivery_with_options(
        self,
        request: dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse().from_map(
            self.do_rpcrequest('EnableDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_dcdn_domain_offline_log_delivery_with_options_async(
        self,
        request: dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse().from_map(
            await self.do_rpcrequest_async('EnableDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_dcdn_domain_offline_log_delivery(
        self,
        request: dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_dcdn_domain_offline_log_delivery_with_options(request, runtime)

    async def enable_dcdn_domain_offline_log_delivery_async(
        self,
        request: dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryRequest,
    ) -> dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_dcdn_domain_offline_log_delivery_with_options_async(request, runtime)

    def modify_dcdn_domain_schdm_by_property_with_options(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse().from_map(
            self.do_rpcrequest('ModifyDCdnDomainSchdmByProperty', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dcdn_domain_schdm_by_property_with_options_async(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse().from_map(
            await self.do_rpcrequest_async('ModifyDCdnDomainSchdmByProperty', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dcdn_domain_schdm_by_property(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dcdn_domain_schdm_by_property_with_options(request, runtime)

    async def modify_dcdn_domain_schdm_by_property_async(
        self,
        request: dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyRequest,
    ) -> dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dcdn_domain_schdm_by_property_with_options_async(request, runtime)

    def open_dcdn_service_with_options(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.OpenDcdnServiceResponse().from_map(
            self.do_rpcrequest('OpenDcdnService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_dcdn_service_with_options_async(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.OpenDcdnServiceResponse().from_map(
            await self.do_rpcrequest_async('OpenDcdnService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_dcdn_service(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_dcdn_service_with_options(request, runtime)

    async def open_dcdn_service_async(
        self,
        request: dcdn_20180115_models.OpenDcdnServiceRequest,
    ) -> dcdn_20180115_models.OpenDcdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_dcdn_service_with_options_async(request, runtime)

    def preload_dcdn_object_caches_with_options(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.PreloadDcdnObjectCachesResponse().from_map(
            self.do_rpcrequest('PreloadDcdnObjectCaches', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def preload_dcdn_object_caches_with_options_async(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.PreloadDcdnObjectCachesResponse().from_map(
            await self.do_rpcrequest_async('PreloadDcdnObjectCaches', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def preload_dcdn_object_caches(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.preload_dcdn_object_caches_with_options(request, runtime)

    async def preload_dcdn_object_caches_async(
        self,
        request: dcdn_20180115_models.PreloadDcdnObjectCachesRequest,
    ) -> dcdn_20180115_models.PreloadDcdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preload_dcdn_object_caches_with_options_async(request, runtime)

    def publish_dcdn_staging_config_to_production_with_options(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse().from_map(
            self.do_rpcrequest('PublishDcdnStagingConfigToProduction', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_dcdn_staging_config_to_production_with_options_async(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse().from_map(
            await self.do_rpcrequest_async('PublishDcdnStagingConfigToProduction', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_dcdn_staging_config_to_production(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_dcdn_staging_config_to_production_with_options(request, runtime)

    async def publish_dcdn_staging_config_to_production_async(
        self,
        request: dcdn_20180115_models.PublishDcdnStagingConfigToProductionRequest,
    ) -> dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_dcdn_staging_config_to_production_with_options_async(request, runtime)

    def refresh_dcdn_object_caches_with_options(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.RefreshDcdnObjectCachesResponse().from_map(
            self.do_rpcrequest('RefreshDcdnObjectCaches', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_dcdn_object_caches_with_options_async(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.RefreshDcdnObjectCachesResponse().from_map(
            await self.do_rpcrequest_async('RefreshDcdnObjectCaches', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_dcdn_object_caches(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_dcdn_object_caches_with_options(request, runtime)

    async def refresh_dcdn_object_caches_async(
        self,
        request: dcdn_20180115_models.RefreshDcdnObjectCachesRequest,
    ) -> dcdn_20180115_models.RefreshDcdnObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_dcdn_object_caches_with_options_async(request, runtime)

    def rollback_dcdn_staging_config_with_options(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.RollbackDcdnStagingConfigResponse().from_map(
            self.do_rpcrequest('RollbackDcdnStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rollback_dcdn_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.RollbackDcdnStagingConfigResponse().from_map(
            await self.do_rpcrequest_async('RollbackDcdnStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rollback_dcdn_staging_config(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_dcdn_staging_config_with_options(request, runtime)

    async def rollback_dcdn_staging_config_async(
        self,
        request: dcdn_20180115_models.RollbackDcdnStagingConfigRequest,
    ) -> dcdn_20180115_models.RollbackDcdnStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_dcdn_staging_config_with_options_async(request, runtime)

    def set_dcdn_config_of_version_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.SetDcdnConfigOfVersionResponse().from_map(
            self.do_rpcrequest('SetDcdnConfigOfVersion', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dcdn_config_of_version_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnConfigOfVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnConfigOfVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.SetDcdnConfigOfVersionResponse().from_map(
            await self.do_rpcrequest_async('SetDcdnConfigOfVersion', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_dcdn_config_of_version(
        self,
        request: dcdn_20180115_models.SetDcdnConfigOfVersionRequest,
    ) -> dcdn_20180115_models.SetDcdnConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_config_of_version_with_options(request, runtime)

    async def set_dcdn_config_of_version_async(
        self,
        request: dcdn_20180115_models.SetDcdnConfigOfVersionRequest,
    ) -> dcdn_20180115_models.SetDcdnConfigOfVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_config_of_version_with_options_async(request, runtime)

    def set_dcdn_domain_certificate_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.SetDcdnDomainCertificateResponse().from_map(
            self.do_rpcrequest('SetDcdnDomainCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dcdn_domain_certificate_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.SetDcdnDomainCertificateResponse().from_map(
            await self.do_rpcrequest_async('SetDcdnDomainCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_dcdn_domain_certificate(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_certificate_with_options(request, runtime)

    async def set_dcdn_domain_certificate_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_certificate_with_options_async(request, runtime)

    def set_dcdn_domain_csrcertificate_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCSRCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse().from_map(
            self.do_rpcrequest('SetDcdnDomainCSRCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dcdn_domain_csrcertificate_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCSRCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse().from_map(
            await self.do_rpcrequest_async('SetDcdnDomainCSRCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_dcdn_domain_csrcertificate(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCSRCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_csrcertificate_with_options(request, runtime)

    async def set_dcdn_domain_csrcertificate_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainCSRCertificateRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_csrcertificate_with_options_async(request, runtime)

    def set_dcdn_domain_staging_config_with_options(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.SetDcdnDomainStagingConfigResponse().from_map(
            self.do_rpcrequest('SetDcdnDomainStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_dcdn_domain_staging_config_with_options_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.SetDcdnDomainStagingConfigResponse().from_map(
            await self.do_rpcrequest_async('SetDcdnDomainStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_dcdn_domain_staging_config(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_staging_config_with_options(request, runtime)

    async def set_dcdn_domain_staging_config_async(
        self,
        request: dcdn_20180115_models.SetDcdnDomainStagingConfigRequest,
    ) -> dcdn_20180115_models.SetDcdnDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dcdn_domain_staging_config_with_options_async(request, runtime)

    def start_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.StartDcdnDomainResponse().from_map(
            self.do_rpcrequest('StartDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.StartDcdnDomainResponse().from_map(
            await self.do_rpcrequest_async('StartDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_dcdn_domain(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_dcdn_domain_with_options(request, runtime)

    async def start_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.StartDcdnDomainRequest,
    ) -> dcdn_20180115_models.StartDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_dcdn_domain_with_options_async(request, runtime)

    def start_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.StartDcdnIpaDomainResponse().from_map(
            self.do_rpcrequest('StartDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.StartDcdnIpaDomainResponse().from_map(
            await self.do_rpcrequest_async('StartDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_dcdn_ipa_domain(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_dcdn_ipa_domain_with_options(request, runtime)

    async def start_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.StartDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.StartDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_dcdn_ipa_domain_with_options_async(request, runtime)

    def stop_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.StopDcdnDomainResponse().from_map(
            self.do_rpcrequest('StopDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.StopDcdnDomainResponse().from_map(
            await self.do_rpcrequest_async('StopDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_dcdn_domain(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_dcdn_domain_with_options(request, runtime)

    async def stop_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.StopDcdnDomainRequest,
    ) -> dcdn_20180115_models.StopDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_dcdn_domain_with_options_async(request, runtime)

    def stop_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.StopDcdnIpaDomainResponse().from_map(
            self.do_rpcrequest('StopDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.StopDcdnIpaDomainResponse().from_map(
            await self.do_rpcrequest_async('StopDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_dcdn_ipa_domain(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_dcdn_ipa_domain_with_options(request, runtime)

    async def stop_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.StopDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.StopDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_dcdn_ipa_domain_with_options_async(request, runtime)

    def tag_dcdn_resources_with_options(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.TagDcdnResourcesResponse().from_map(
            self.do_rpcrequest('TagDcdnResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_dcdn_resources_with_options_async(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.TagDcdnResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagDcdnResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_dcdn_resources(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_dcdn_resources_with_options(request, runtime)

    async def tag_dcdn_resources_async(
        self,
        request: dcdn_20180115_models.TagDcdnResourcesRequest,
    ) -> dcdn_20180115_models.TagDcdnResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_dcdn_resources_with_options_async(request, runtime)

    def untag_dcdn_resources_with_options(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.UntagDcdnResourcesResponse().from_map(
            self.do_rpcrequest('UntagDcdnResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_dcdn_resources_with_options_async(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.UntagDcdnResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagDcdnResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_dcdn_resources(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_dcdn_resources_with_options(request, runtime)

    async def untag_dcdn_resources_async(
        self,
        request: dcdn_20180115_models.UntagDcdnResourcesRequest,
    ) -> dcdn_20180115_models.UntagDcdnResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_dcdn_resources_with_options_async(request, runtime)

    def update_dcdn_domain_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.UpdateDcdnDomainResponse().from_map(
            self.do_rpcrequest('UpdateDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dcdn_domain_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.UpdateDcdnDomainResponse().from_map(
            await self.do_rpcrequest_async('UpdateDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dcdn_domain(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_domain_with_options(request, runtime)

    async def update_dcdn_domain_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnDomainRequest,
    ) -> dcdn_20180115_models.UpdateDcdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_domain_with_options_async(request, runtime)

    def update_dcdn_ipa_domain_with_options(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.UpdateDcdnIpaDomainResponse().from_map(
            self.do_rpcrequest('UpdateDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dcdn_ipa_domain_with_options_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.UpdateDcdnIpaDomainResponse().from_map(
            await self.do_rpcrequest_async('UpdateDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dcdn_ipa_domain(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_ipa_domain_with_options(request, runtime)

    async def update_dcdn_ipa_domain_async(
        self,
        request: dcdn_20180115_models.UpdateDcdnIpaDomainRequest,
    ) -> dcdn_20180115_models.UpdateDcdnIpaDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dcdn_ipa_domain_with_options_async(request, runtime)

    def verify_dcdn_domain_owner_with_options(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.VerifyDcdnDomainOwnerResponse().from_map(
            self.do_rpcrequest('VerifyDcdnDomainOwner', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_dcdn_domain_owner_with_options_async(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dcdn_20180115_models.VerifyDcdnDomainOwnerResponse().from_map(
            await self.do_rpcrequest_async('VerifyDcdnDomainOwner', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_dcdn_domain_owner(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_dcdn_domain_owner_with_options(request, runtime)

    async def verify_dcdn_domain_owner_async(
        self,
        request: dcdn_20180115_models.VerifyDcdnDomainOwnerRequest,
    ) -> dcdn_20180115_models.VerifyDcdnDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_dcdn_domain_owner_with_options_async(request, runtime)
