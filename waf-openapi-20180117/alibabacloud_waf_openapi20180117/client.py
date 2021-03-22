# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_waf_openapi20180117 import models as waf_openapi_20180117_models
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

    def create_acl_rule_with_options(
        self,
        request: waf_openapi_20180117_models.CreateAclRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.CreateAclRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateAclRuleResponse().from_map(
            self.do_rpcrequest('CreateAclRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_acl_rule_with_options_async(
        self,
        request: waf_openapi_20180117_models.CreateAclRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.CreateAclRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateAclRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateAclRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_acl_rule(
        self,
        request: waf_openapi_20180117_models.CreateAclRuleRequest,
    ) -> waf_openapi_20180117_models.CreateAclRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_acl_rule_with_options(request, runtime)

    async def create_acl_rule_async(
        self,
        request: waf_openapi_20180117_models.CreateAclRuleRequest,
    ) -> waf_openapi_20180117_models.CreateAclRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_acl_rule_with_options_async(request, runtime)

    def create_cert_and_key_with_options(
        self,
        request: waf_openapi_20180117_models.CreateCertAndKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.CreateCertAndKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateCertAndKeyResponse().from_map(
            self.do_rpcrequest('CreateCertAndKey', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cert_and_key_with_options_async(
        self,
        request: waf_openapi_20180117_models.CreateCertAndKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.CreateCertAndKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateCertAndKeyResponse().from_map(
            await self.do_rpcrequest_async('CreateCertAndKey', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cert_and_key(
        self,
        request: waf_openapi_20180117_models.CreateCertAndKeyRequest,
    ) -> waf_openapi_20180117_models.CreateCertAndKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cert_and_key_with_options(request, runtime)

    async def create_cert_and_key_async(
        self,
        request: waf_openapi_20180117_models.CreateCertAndKeyRequest,
    ) -> waf_openapi_20180117_models.CreateCertAndKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cert_and_key_with_options_async(request, runtime)

    def create_domain_config_with_options(
        self,
        request: waf_openapi_20180117_models.CreateDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.CreateDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateDomainConfigResponse().from_map(
            self.do_rpcrequest('CreateDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_domain_config_with_options_async(
        self,
        request: waf_openapi_20180117_models.CreateDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.CreateDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateDomainConfigResponse().from_map(
            await self.do_rpcrequest_async('CreateDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_domain_config(
        self,
        request: waf_openapi_20180117_models.CreateDomainConfigRequest,
    ) -> waf_openapi_20180117_models.CreateDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_domain_config_with_options(request, runtime)

    async def create_domain_config_async(
        self,
        request: waf_openapi_20180117_models.CreateDomainConfigRequest,
    ) -> waf_openapi_20180117_models.CreateDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_config_with_options_async(request, runtime)

    def create_protection_module_rule_with_options(
        self,
        request: waf_openapi_20180117_models.CreateProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.CreateProtectionModuleRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateProtectionModuleRuleResponse().from_map(
            self.do_rpcrequest('CreateProtectionModuleRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_protection_module_rule_with_options_async(
        self,
        request: waf_openapi_20180117_models.CreateProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.CreateProtectionModuleRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateProtectionModuleRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateProtectionModuleRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_protection_module_rule(
        self,
        request: waf_openapi_20180117_models.CreateProtectionModuleRuleRequest,
    ) -> waf_openapi_20180117_models.CreateProtectionModuleRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_protection_module_rule_with_options(request, runtime)

    async def create_protection_module_rule_async(
        self,
        request: waf_openapi_20180117_models.CreateProtectionModuleRuleRequest,
    ) -> waf_openapi_20180117_models.CreateProtectionModuleRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_protection_module_rule_with_options_async(request, runtime)

    def delete_acl_rule_with_options(
        self,
        request: waf_openapi_20180117_models.DeleteAclRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DeleteAclRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DeleteAclRuleResponse().from_map(
            self.do_rpcrequest('DeleteAclRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_acl_rule_with_options_async(
        self,
        request: waf_openapi_20180117_models.DeleteAclRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DeleteAclRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DeleteAclRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteAclRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_acl_rule(
        self,
        request: waf_openapi_20180117_models.DeleteAclRuleRequest,
    ) -> waf_openapi_20180117_models.DeleteAclRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_rule_with_options(request, runtime)

    async def delete_acl_rule_async(
        self,
        request: waf_openapi_20180117_models.DeleteAclRuleRequest,
    ) -> waf_openapi_20180117_models.DeleteAclRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_acl_rule_with_options_async(request, runtime)

    def delete_domain_config_with_options(
        self,
        request: waf_openapi_20180117_models.DeleteDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DeleteDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DeleteDomainConfigResponse().from_map(
            self.do_rpcrequest('DeleteDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_domain_config_with_options_async(
        self,
        request: waf_openapi_20180117_models.DeleteDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DeleteDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DeleteDomainConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_domain_config(
        self,
        request: waf_openapi_20180117_models.DeleteDomainConfigRequest,
    ) -> waf_openapi_20180117_models.DeleteDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_config_with_options(request, runtime)

    async def delete_domain_config_async(
        self,
        request: waf_openapi_20180117_models.DeleteDomainConfigRequest,
    ) -> waf_openapi_20180117_models.DeleteDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_config_with_options_async(request, runtime)

    def describe_acl_rules_with_options(
        self,
        request: waf_openapi_20180117_models.DescribeAclRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeAclRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeAclRulesResponse().from_map(
            self.do_rpcrequest('DescribeAclRules', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_acl_rules_with_options_async(
        self,
        request: waf_openapi_20180117_models.DescribeAclRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeAclRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeAclRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAclRules', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_acl_rules(
        self,
        request: waf_openapi_20180117_models.DescribeAclRulesRequest,
    ) -> waf_openapi_20180117_models.DescribeAclRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_acl_rules_with_options(request, runtime)

    async def describe_acl_rules_async(
        self,
        request: waf_openapi_20180117_models.DescribeAclRulesRequest,
    ) -> waf_openapi_20180117_models.DescribeAclRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_acl_rules_with_options_async(request, runtime)

    def describe_async_task_status_with_options(
        self,
        request: waf_openapi_20180117_models.DescribeAsyncTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeAsyncTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeAsyncTaskStatusResponse().from_map(
            self.do_rpcrequest('DescribeAsyncTaskStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_async_task_status_with_options_async(
        self,
        request: waf_openapi_20180117_models.DescribeAsyncTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeAsyncTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeAsyncTaskStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeAsyncTaskStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_async_task_status(
        self,
        request: waf_openapi_20180117_models.DescribeAsyncTaskStatusRequest,
    ) -> waf_openapi_20180117_models.DescribeAsyncTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_async_task_status_with_options(request, runtime)

    async def describe_async_task_status_async(
        self,
        request: waf_openapi_20180117_models.DescribeAsyncTaskStatusRequest,
    ) -> waf_openapi_20180117_models.DescribeAsyncTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_async_task_status_with_options_async(request, runtime)

    def describe_domain_config_with_options(
        self,
        request: waf_openapi_20180117_models.DescribeDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeDomainConfigResponse().from_map(
            self.do_rpcrequest('DescribeDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_config_with_options_async(
        self,
        request: waf_openapi_20180117_models.DescribeDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeDomainConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_config(
        self,
        request: waf_openapi_20180117_models.DescribeDomainConfigRequest,
    ) -> waf_openapi_20180117_models.DescribeDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_config_with_options(request, runtime)

    async def describe_domain_config_async(
        self,
        request: waf_openapi_20180117_models.DescribeDomainConfigRequest,
    ) -> waf_openapi_20180117_models.DescribeDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_config_with_options_async(request, runtime)

    def describe_domain_config_status_with_options(
        self,
        request: waf_openapi_20180117_models.DescribeDomainConfigStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeDomainConfigStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeDomainConfigStatusResponse().from_map(
            self.do_rpcrequest('DescribeDomainConfigStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_config_status_with_options_async(
        self,
        request: waf_openapi_20180117_models.DescribeDomainConfigStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeDomainConfigStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeDomainConfigStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainConfigStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_config_status(
        self,
        request: waf_openapi_20180117_models.DescribeDomainConfigStatusRequest,
    ) -> waf_openapi_20180117_models.DescribeDomainConfigStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_config_status_with_options(request, runtime)

    async def describe_domain_config_status_async(
        self,
        request: waf_openapi_20180117_models.DescribeDomainConfigStatusRequest,
    ) -> waf_openapi_20180117_models.DescribeDomainConfigStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_config_status_with_options_async(request, runtime)

    def describe_domain_names_with_options(
        self,
        request: waf_openapi_20180117_models.DescribeDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeDomainNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeDomainNamesResponse().from_map(
            self.do_rpcrequest('DescribeDomainNames', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_names_with_options_async(
        self,
        request: waf_openapi_20180117_models.DescribeDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeDomainNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeDomainNamesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainNames', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_names(
        self,
        request: waf_openapi_20180117_models.DescribeDomainNamesRequest,
    ) -> waf_openapi_20180117_models.DescribeDomainNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_names_with_options(request, runtime)

    async def describe_domain_names_async(
        self,
        request: waf_openapi_20180117_models.DescribeDomainNamesRequest,
    ) -> waf_openapi_20180117_models.DescribeDomainNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_names_with_options_async(request, runtime)

    def describe_pay_info_with_options(
        self,
        request: waf_openapi_20180117_models.DescribePayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribePayInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribePayInfoResponse().from_map(
            self.do_rpcrequest('DescribePayInfo', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_pay_info_with_options_async(
        self,
        request: waf_openapi_20180117_models.DescribePayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribePayInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribePayInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribePayInfo', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_pay_info(
        self,
        request: waf_openapi_20180117_models.DescribePayInfoRequest,
    ) -> waf_openapi_20180117_models.DescribePayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pay_info_with_options(request, runtime)

    async def describe_pay_info_async(
        self,
        request: waf_openapi_20180117_models.DescribePayInfoRequest,
    ) -> waf_openapi_20180117_models.DescribePayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pay_info_with_options_async(request, runtime)

    def describe_protection_module_rules_with_options(
        self,
        request: waf_openapi_20180117_models.DescribeProtectionModuleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeProtectionModuleRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeProtectionModuleRulesResponse().from_map(
            self.do_rpcrequest('DescribeProtectionModuleRules', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_protection_module_rules_with_options_async(
        self,
        request: waf_openapi_20180117_models.DescribeProtectionModuleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeProtectionModuleRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeProtectionModuleRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeProtectionModuleRules', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_protection_module_rules(
        self,
        request: waf_openapi_20180117_models.DescribeProtectionModuleRulesRequest,
    ) -> waf_openapi_20180117_models.DescribeProtectionModuleRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_rules_with_options(request, runtime)

    async def describe_protection_module_rules_async(
        self,
        request: waf_openapi_20180117_models.DescribeProtectionModuleRulesRequest,
    ) -> waf_openapi_20180117_models.DescribeProtectionModuleRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_protection_module_rules_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: waf_openapi_20180117_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: waf_openapi_20180117_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: waf_openapi_20180117_models.DescribeRegionsRequest,
    ) -> waf_openapi_20180117_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: waf_openapi_20180117_models.DescribeRegionsRequest,
    ) -> waf_openapi_20180117_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_waf_source_ip_segment_with_options(
        self,
        request: waf_openapi_20180117_models.DescribeWafSourceIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeWafSourceIpSegmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeWafSourceIpSegmentResponse().from_map(
            self.do_rpcrequest('DescribeWafSourceIpSegment', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_waf_source_ip_segment_with_options_async(
        self,
        request: waf_openapi_20180117_models.DescribeWafSourceIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.DescribeWafSourceIpSegmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeWafSourceIpSegmentResponse().from_map(
            await self.do_rpcrequest_async('DescribeWafSourceIpSegment', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_waf_source_ip_segment(
        self,
        request: waf_openapi_20180117_models.DescribeWafSourceIpSegmentRequest,
    ) -> waf_openapi_20180117_models.DescribeWafSourceIpSegmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_source_ip_segment_with_options(request, runtime)

    async def describe_waf_source_ip_segment_async(
        self,
        request: waf_openapi_20180117_models.DescribeWafSourceIpSegmentRequest,
    ) -> waf_openapi_20180117_models.DescribeWafSourceIpSegmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_waf_source_ip_segment_with_options_async(request, runtime)

    def modify_acl_rule_with_options(
        self,
        request: waf_openapi_20180117_models.ModifyAclRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.ModifyAclRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyAclRuleResponse().from_map(
            self.do_rpcrequest('ModifyAclRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_acl_rule_with_options_async(
        self,
        request: waf_openapi_20180117_models.ModifyAclRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.ModifyAclRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyAclRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyAclRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_acl_rule(
        self,
        request: waf_openapi_20180117_models.ModifyAclRuleRequest,
    ) -> waf_openapi_20180117_models.ModifyAclRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_acl_rule_with_options(request, runtime)

    async def modify_acl_rule_async(
        self,
        request: waf_openapi_20180117_models.ModifyAclRuleRequest,
    ) -> waf_openapi_20180117_models.ModifyAclRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_acl_rule_with_options_async(request, runtime)

    def modify_domain_config_with_options(
        self,
        request: waf_openapi_20180117_models.ModifyDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.ModifyDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyDomainConfigResponse().from_map(
            self.do_rpcrequest('ModifyDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_domain_config_with_options_async(
        self,
        request: waf_openapi_20180117_models.ModifyDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.ModifyDomainConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyDomainConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_domain_config(
        self,
        request: waf_openapi_20180117_models.ModifyDomainConfigRequest,
    ) -> waf_openapi_20180117_models.ModifyDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_config_with_options(request, runtime)

    async def modify_domain_config_async(
        self,
        request: waf_openapi_20180117_models.ModifyDomainConfigRequest,
    ) -> waf_openapi_20180117_models.ModifyDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_config_with_options_async(request, runtime)

    def modify_protection_rule_cache_status_with_options(
        self,
        request: waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusResponse().from_map(
            self.do_rpcrequest('ModifyProtectionRuleCacheStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_protection_rule_cache_status_with_options_async(
        self,
        request: waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyProtectionRuleCacheStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_rule_cache_status(
        self,
        request: waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusRequest,
    ) -> waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_cache_status_with_options(request, runtime)

    async def modify_protection_rule_cache_status_async(
        self,
        request: waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusRequest,
    ) -> waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_rule_cache_status_with_options_async(request, runtime)

    def modify_protection_rule_status_with_options(
        self,
        request: waf_openapi_20180117_models.ModifyProtectionRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.ModifyProtectionRuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyProtectionRuleStatusResponse().from_map(
            self.do_rpcrequest('ModifyProtectionRuleStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_protection_rule_status_with_options_async(
        self,
        request: waf_openapi_20180117_models.ModifyProtectionRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.ModifyProtectionRuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyProtectionRuleStatusResponse().from_map(
            await self.do_rpcrequest_async('ModifyProtectionRuleStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_rule_status(
        self,
        request: waf_openapi_20180117_models.ModifyProtectionRuleStatusRequest,
    ) -> waf_openapi_20180117_models.ModifyProtectionRuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_status_with_options(request, runtime)

    async def modify_protection_rule_status_async(
        self,
        request: waf_openapi_20180117_models.ModifyProtectionRuleStatusRequest,
    ) -> waf_openapi_20180117_models.ModifyProtectionRuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_rule_status_with_options_async(request, runtime)

    def modify_waf_switch_with_options(
        self,
        request: waf_openapi_20180117_models.ModifyWafSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.ModifyWafSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyWafSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWafSwitch', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_waf_switch_with_options_async(
        self,
        request: waf_openapi_20180117_models.ModifyWafSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20180117_models.ModifyWafSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyWafSwitchResponse().from_map(
            await self.do_rpcrequest_async('ModifyWafSwitch', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_waf_switch(
        self,
        request: waf_openapi_20180117_models.ModifyWafSwitchRequest,
    ) -> waf_openapi_20180117_models.ModifyWafSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_waf_switch_with_options(request, runtime)

    async def modify_waf_switch_async(
        self,
        request: waf_openapi_20180117_models.ModifyWafSwitchRequest,
    ) -> waf_openapi_20180117_models.ModifyWafSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_waf_switch_with_options_async(request, runtime)
