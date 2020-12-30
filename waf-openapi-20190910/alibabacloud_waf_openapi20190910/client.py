# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_waf_openapi20190910 import models as waf_openapi_20190910_models
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

    def create_certificate_with_options(
        self,
        request: waf_openapi_20190910_models.CreateCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.CreateCertificateResponse().from_map(
            self.do_rpcrequest('CreateCertificate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_certificate_with_options_async(
        self,
        request: waf_openapi_20190910_models.CreateCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.CreateCertificateResponse().from_map(
            await self.do_rpcrequest_async('CreateCertificate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_certificate(
        self,
        request: waf_openapi_20190910_models.CreateCertificateRequest,
    ) -> waf_openapi_20190910_models.CreateCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_options(request, runtime)

    async def create_certificate_async(
        self,
        request: waf_openapi_20190910_models.CreateCertificateRequest,
    ) -> waf_openapi_20190910_models.CreateCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_with_options_async(request, runtime)

    def create_certificate_by_certificate_id_with_options(
        self,
        request: waf_openapi_20190910_models.CreateCertificateByCertificateIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse().from_map(
            self.do_rpcrequest('CreateCertificateByCertificateId', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_certificate_by_certificate_id_with_options_async(
        self,
        request: waf_openapi_20190910_models.CreateCertificateByCertificateIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse().from_map(
            await self.do_rpcrequest_async('CreateCertificateByCertificateId', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_certificate_by_certificate_id(
        self,
        request: waf_openapi_20190910_models.CreateCertificateByCertificateIdRequest,
    ) -> waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_by_certificate_id_with_options(request, runtime)

    async def create_certificate_by_certificate_id_async(
        self,
        request: waf_openapi_20190910_models.CreateCertificateByCertificateIdRequest,
    ) -> waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_by_certificate_id_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        request: waf_openapi_20190910_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.CreateDomainResponse().from_map(
            self.do_rpcrequest('CreateDomain', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: waf_openapi_20190910_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.CreateDomainResponse().from_map(
            await self.do_rpcrequest_async('CreateDomain', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_domain(
        self,
        request: waf_openapi_20190910_models.CreateDomainRequest,
    ) -> waf_openapi_20190910_models.CreateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: waf_openapi_20190910_models.CreateDomainRequest,
    ) -> waf_openapi_20190910_models.CreateDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_protection_module_rule_with_options(
        self,
        request: waf_openapi_20190910_models.CreateProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateProtectionModuleRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.CreateProtectionModuleRuleResponse().from_map(
            self.do_rpcrequest('CreateProtectionModuleRule', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_protection_module_rule_with_options_async(
        self,
        request: waf_openapi_20190910_models.CreateProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateProtectionModuleRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.CreateProtectionModuleRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateProtectionModuleRule', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_protection_module_rule(
        self,
        request: waf_openapi_20190910_models.CreateProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.CreateProtectionModuleRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_protection_module_rule_with_options(request, runtime)

    async def create_protection_module_rule_async(
        self,
        request: waf_openapi_20190910_models.CreateProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.CreateProtectionModuleRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_protection_module_rule_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: waf_openapi_20190910_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DeleteDomainResponse().from_map(
            self.do_rpcrequest('DeleteDomain', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: waf_openapi_20190910_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DeleteDomainResponse().from_map(
            await self.do_rpcrequest_async('DeleteDomain', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_domain(
        self,
        request: waf_openapi_20190910_models.DeleteDomainRequest,
    ) -> waf_openapi_20190910_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: waf_openapi_20190910_models.DeleteDomainRequest,
    ) -> waf_openapi_20190910_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: waf_openapi_20190910_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DeleteInstanceResponse().from_map(
            self.do_rpcrequest('DeleteInstance', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: waf_openapi_20190910_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DeleteInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteInstance', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(
        self,
        request: waf_openapi_20190910_models.DeleteInstanceRequest,
    ) -> waf_openapi_20190910_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: waf_openapi_20190910_models.DeleteInstanceRequest,
    ) -> waf_openapi_20190910_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_protection_module_rule_with_options(
        self,
        request: waf_openapi_20190910_models.DeleteProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse().from_map(
            self.do_rpcrequest('DeleteProtectionModuleRule', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_protection_module_rule_with_options_async(
        self,
        request: waf_openapi_20190910_models.DeleteProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteProtectionModuleRule', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_protection_module_rule(
        self,
        request: waf_openapi_20190910_models.DeleteProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_protection_module_rule_with_options(request, runtime)

    async def delete_protection_module_rule_async(
        self,
        request: waf_openapi_20190910_models.DeleteProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_protection_module_rule_with_options_async(request, runtime)

    def describe_certificates_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeCertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeCertificatesResponse().from_map(
            self.do_rpcrequest('DescribeCertificates', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_certificates_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeCertificatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeCertificatesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCertificates', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_certificates(
        self,
        request: waf_openapi_20190910_models.DescribeCertificatesRequest,
    ) -> waf_openapi_20190910_models.DescribeCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_certificates_with_options(request, runtime)

    async def describe_certificates_async(
        self,
        request: waf_openapi_20190910_models.DescribeCertificatesRequest,
    ) -> waf_openapi_20190910_models.DescribeCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificates_with_options_async(request, runtime)

    def describe_cert_match_status_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeCertMatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeCertMatchStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeCertMatchStatusResponse().from_map(
            self.do_rpcrequest('DescribeCertMatchStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cert_match_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeCertMatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeCertMatchStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeCertMatchStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeCertMatchStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cert_match_status(
        self,
        request: waf_openapi_20190910_models.DescribeCertMatchStatusRequest,
    ) -> waf_openapi_20190910_models.DescribeCertMatchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cert_match_status_with_options(request, runtime)

    async def describe_cert_match_status_async(
        self,
        request: waf_openapi_20190910_models.DescribeCertMatchStatusRequest,
    ) -> waf_openapi_20190910_models.DescribeCertMatchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cert_match_status_with_options_async(request, runtime)

    def describe_domain_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeDomainResponse().from_map(
            self.do_rpcrequest('DescribeDomain', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeDomainResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomain', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    async def describe_domain_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_with_options_async(request, runtime)

    def describe_domain_advance_configs_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainAdvanceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse().from_map(
            self.do_rpcrequest('DescribeDomainAdvanceConfigs', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_advance_configs_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainAdvanceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainAdvanceConfigs', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_advance_configs(
        self,
        request: waf_openapi_20190910_models.DescribeDomainAdvanceConfigsRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_advance_configs_with_options(request, runtime)

    async def describe_domain_advance_configs_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainAdvanceConfigsRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_advance_configs_with_options_async(request, runtime)

    def describe_domain_basic_configs_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainBasicConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse().from_map(
            self.do_rpcrequest('DescribeDomainBasicConfigs', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_basic_configs_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainBasicConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainBasicConfigs', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_basic_configs(
        self,
        request: waf_openapi_20190910_models.DescribeDomainBasicConfigsRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_basic_configs_with_options(request, runtime)

    async def describe_domain_basic_configs_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainBasicConfigsRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_basic_configs_with_options_async(request, runtime)

    def describe_domain_names_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeDomainNamesResponse().from_map(
            self.do_rpcrequest('DescribeDomainNames', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_names_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeDomainNamesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainNames', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_names(
        self,
        request: waf_openapi_20190910_models.DescribeDomainNamesRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_names_with_options(request, runtime)

    async def describe_domain_names_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainNamesRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_names_with_options_async(request, runtime)

    def describe_domain_rule_group_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainRuleGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeDomainRuleGroupResponse().from_map(
            self.do_rpcrequest('DescribeDomainRuleGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_rule_group_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainRuleGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeDomainRuleGroupResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainRuleGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_rule_group(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRuleGroupRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainRuleGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_rule_group_with_options(request, runtime)

    async def describe_domain_rule_group_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRuleGroupRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainRuleGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_rule_group_with_options_async(request, runtime)

    def describe_instance_info_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeInstanceInfoResponse().from_map(
            self.do_rpcrequest('DescribeInstanceInfo', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_info_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeInstanceInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceInfo', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_info(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfoRequest,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_info_with_options(request, runtime)

    async def describe_instance_info_async(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfoRequest,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_info_with_options_async(request, runtime)

    def describe_instance_infos_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeInstanceInfosResponse().from_map(
            self.do_rpcrequest('DescribeInstanceInfos', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_infos_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeInstanceInfosResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceInfos', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_infos(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfosRequest,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_infos_with_options(request, runtime)

    async def describe_instance_infos_async(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfosRequest,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_infos_with_options_async(request, runtime)

    def describe_instance_spec_info_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceSpecInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse().from_map(
            self.do_rpcrequest('DescribeInstanceSpecInfo', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_spec_info_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceSpecInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceSpecInfo', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_spec_info(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceSpecInfoRequest,
    ) -> waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_spec_info_with_options(request, runtime)

    async def describe_instance_spec_info_async(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceSpecInfoRequest,
    ) -> waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_spec_info_with_options_async(request, runtime)

    def describe_protection_module_mode_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeProtectionModuleModeResponse().from_map(
            self.do_rpcrequest('DescribeProtectionModuleMode', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_protection_module_mode_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeProtectionModuleModeResponse().from_map(
            await self.do_rpcrequest_async('DescribeProtectionModuleMode', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_protection_module_mode(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleModeRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_mode_with_options(request, runtime)

    async def describe_protection_module_mode_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleModeRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_protection_module_mode_with_options_async(request, runtime)

    def describe_protection_module_rules_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse().from_map(
            self.do_rpcrequest('DescribeProtectionModuleRules', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_protection_module_rules_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeProtectionModuleRules', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_protection_module_rules(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleRulesRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_rules_with_options(request, runtime)

    async def describe_protection_module_rules_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleRulesRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_protection_module_rules_with_options_async(request, runtime)

    def describe_protection_module_status_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse().from_map(
            self.do_rpcrequest('DescribeProtectionModuleStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_protection_module_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeProtectionModuleStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_protection_module_status(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleStatusRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_status_with_options(request, runtime)

    async def describe_protection_module_status_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleStatusRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_protection_module_status_with_options_async(request, runtime)

    def describe_waf_source_ip_segment_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeWafSourceIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse().from_map(
            self.do_rpcrequest('DescribeWafSourceIpSegment', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_waf_source_ip_segment_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeWafSourceIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse().from_map(
            await self.do_rpcrequest_async('DescribeWafSourceIpSegment', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_waf_source_ip_segment(
        self,
        request: waf_openapi_20190910_models.DescribeWafSourceIpSegmentRequest,
    ) -> waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_source_ip_segment_with_options(request, runtime)

    async def describe_waf_source_ip_segment_async(
        self,
        request: waf_openapi_20190910_models.DescribeWafSourceIpSegmentRequest,
    ) -> waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_waf_source_ip_segment_with_options_async(request, runtime)

    def modify_domain_cluster_type_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyDomainClusterTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyDomainClusterTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyDomainClusterTypeResponse().from_map(
            self.do_rpcrequest('ModifyDomainClusterType', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_domain_cluster_type_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyDomainClusterTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyDomainClusterTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyDomainClusterTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDomainClusterType', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_domain_cluster_type(
        self,
        request: waf_openapi_20190910_models.ModifyDomainClusterTypeRequest,
    ) -> waf_openapi_20190910_models.ModifyDomainClusterTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_cluster_type_with_options(request, runtime)

    async def modify_domain_cluster_type_async(
        self,
        request: waf_openapi_20190910_models.ModifyDomainClusterTypeRequest,
    ) -> waf_openapi_20190910_models.ModifyDomainClusterTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_cluster_type_with_options_async(request, runtime)

    def modify_domain_ipv_6status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyDomainIpv6StatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse().from_map(
            self.do_rpcrequest('ModifyDomainIpv6Status', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_domain_ipv_6status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyDomainIpv6StatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyDomainIpv6Status', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_domain_ipv_6status(
        self,
        request: waf_openapi_20190910_models.ModifyDomainIpv6StatusRequest,
    ) -> waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_ipv_6status_with_options(request, runtime)

    async def modify_domain_ipv_6status_async(
        self,
        request: waf_openapi_20190910_models.ModifyDomainIpv6StatusRequest,
    ) -> waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_ipv_6status_with_options_async(request, runtime)

    def modify_log_retrieval_status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyLogRetrievalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse().from_map(
            self.do_rpcrequest('ModifyLogRetrievalStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_log_retrieval_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyLogRetrievalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyLogRetrievalStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_log_retrieval_status(
        self,
        request: waf_openapi_20190910_models.ModifyLogRetrievalStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_log_retrieval_status_with_options(request, runtime)

    async def modify_log_retrieval_status_async(
        self,
        request: waf_openapi_20190910_models.ModifyLogRetrievalStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_retrieval_status_with_options_async(request, runtime)

    def modify_log_service_status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyLogServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyLogServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyLogServiceStatusResponse().from_map(
            self.do_rpcrequest('ModifyLogServiceStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_log_service_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyLogServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyLogServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyLogServiceStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyLogServiceStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_log_service_status(
        self,
        request: waf_openapi_20190910_models.ModifyLogServiceStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyLogServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_log_service_status_with_options(request, runtime)

    async def modify_log_service_status_async(
        self,
        request: waf_openapi_20190910_models.ModifyLogServiceStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyLogServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_service_status_with_options_async(request, runtime)

    def modify_protection_module_mode_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyProtectionModuleModeResponse().from_map(
            self.do_rpcrequest('ModifyProtectionModuleMode', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_protection_module_mode_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyProtectionModuleModeResponse().from_map(
            await self.do_rpcrequest_async('ModifyProtectionModuleMode', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_module_mode(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleModeRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_mode_with_options(request, runtime)

    async def modify_protection_module_mode_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleModeRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_module_mode_with_options_async(request, runtime)

    def modify_protection_module_rule_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse().from_map(
            self.do_rpcrequest('ModifyProtectionModuleRule', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_protection_module_rule_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyProtectionModuleRule', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_module_rule(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_rule_with_options(request, runtime)

    async def modify_protection_module_rule_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_module_rule_with_options_async(request, runtime)

    def modify_protection_module_status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse().from_map(
            self.do_rpcrequest('ModifyProtectionModuleStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_protection_module_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyProtectionModuleStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_module_status(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_status_with_options(request, runtime)

    async def modify_protection_module_status_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_module_status_with_options_async(request, runtime)

    def modify_protection_rule_cache_status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse().from_map(
            self.do_rpcrequest('ModifyProtectionRuleCacheStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_protection_rule_cache_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyProtectionRuleCacheStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_rule_cache_status(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_cache_status_with_options(request, runtime)

    async def modify_protection_rule_cache_status_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_rule_cache_status_with_options_async(request, runtime)

    def modify_protection_rule_status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse().from_map(
            self.do_rpcrequest('ModifyProtectionRuleStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_protection_rule_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyProtectionRuleStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_rule_status(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_status_with_options(request, runtime)

    async def modify_protection_rule_status_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_rule_status_with_options_async(request, runtime)

    def set_domain_rule_group_with_options(
        self,
        request: waf_openapi_20190910_models.SetDomainRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.SetDomainRuleGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.SetDomainRuleGroupResponse().from_map(
            self.do_rpcrequest('SetDomainRuleGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_domain_rule_group_with_options_async(
        self,
        request: waf_openapi_20190910_models.SetDomainRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.SetDomainRuleGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20190910_models.SetDomainRuleGroupResponse().from_map(
            await self.do_rpcrequest_async('SetDomainRuleGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_domain_rule_group(
        self,
        request: waf_openapi_20190910_models.SetDomainRuleGroupRequest,
    ) -> waf_openapi_20190910_models.SetDomainRuleGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_rule_group_with_options(request, runtime)

    async def set_domain_rule_group_async(
        self,
        request: waf_openapi_20190910_models.SetDomainRuleGroupRequest,
    ) -> waf_openapi_20190910_models.SetDomainRuleGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_rule_group_with_options_async(request, runtime)
