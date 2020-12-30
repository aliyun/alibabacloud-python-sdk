# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sts20150401 import models as sts_20150401_models
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
            'ap-northeast-2-pop': 'sts.aliyuncs.com',
            'cn-beijing-finance-1': 'sts.aliyuncs.com',
            'cn-beijing-finance-pop': 'sts.aliyuncs.com',
            'cn-beijing-gov-1': 'sts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'sts.aliyuncs.com',
            'cn-edge-1': 'sts.aliyuncs.com',
            'cn-fujian': 'sts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'sts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'sts.aliyuncs.com',
            'cn-hangzhou-finance': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'sts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'sts.aliyuncs.com',
            'cn-hangzhou-test-306': 'sts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'sts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'sts.aliyuncs.com',
            'cn-north-2-gov-1': 'sts-vpc.cn-north-2-gov-1.aliyuncs.com',
            'cn-qingdao-nebula': 'sts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'sts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'sts.aliyuncs.com',
            'cn-shanghai-inner': 'sts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'sts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'sts.aliyuncs.com',
            'cn-shenzhen-inner': 'sts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'sts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'sts.aliyuncs.com',
            'cn-wuhan': 'sts.aliyuncs.com',
            'cn-yushanfang': 'sts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'sts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'sts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'sts.aliyuncs.com',
            'eu-west-1-oxs': 'sts.aliyuncs.com',
            'rus-west-1-pop': 'sts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('sts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def assume_role_with_options(
        self,
        request: sts_20150401_models.AssumeRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.AssumeRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sts_20150401_models.AssumeRoleResponse().from_map(
            self.do_rpcrequest('AssumeRole', '2015-04-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assume_role_with_options_async(
        self,
        request: sts_20150401_models.AssumeRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.AssumeRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sts_20150401_models.AssumeRoleResponse().from_map(
            await self.do_rpcrequest_async('AssumeRole', '2015-04-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assume_role(
        self,
        request: sts_20150401_models.AssumeRoleRequest,
    ) -> sts_20150401_models.AssumeRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.assume_role_with_options(request, runtime)

    async def assume_role_async(
        self,
        request: sts_20150401_models.AssumeRoleRequest,
    ) -> sts_20150401_models.AssumeRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assume_role_with_options_async(request, runtime)

    def assume_role_with_samlwith_options(
        self,
        request: sts_20150401_models.AssumeRoleWithSAMLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.AssumeRoleWithSAMLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sts_20150401_models.AssumeRoleWithSAMLResponse().from_map(
            self.do_rpcrequest('AssumeRoleWithSAML', '2015-04-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assume_role_with_samlwith_options_async(
        self,
        request: sts_20150401_models.AssumeRoleWithSAMLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.AssumeRoleWithSAMLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return sts_20150401_models.AssumeRoleWithSAMLResponse().from_map(
            await self.do_rpcrequest_async('AssumeRoleWithSAML', '2015-04-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assume_role_with_saml(
        self,
        request: sts_20150401_models.AssumeRoleWithSAMLRequest,
    ) -> sts_20150401_models.AssumeRoleWithSAMLResponse:
        runtime = util_models.RuntimeOptions()
        return self.assume_role_with_samlwith_options(request, runtime)

    async def assume_role_with_saml_async(
        self,
        request: sts_20150401_models.AssumeRoleWithSAMLRequest,
    ) -> sts_20150401_models.AssumeRoleWithSAMLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assume_role_with_samlwith_options_async(request, runtime)

    def get_caller_identity_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.GetCallerIdentityResponse:
        req = open_api_models.OpenApiRequest()
        return sts_20150401_models.GetCallerIdentityResponse().from_map(
            self.do_rpcrequest('GetCallerIdentity', '2015-04-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_caller_identity_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> sts_20150401_models.GetCallerIdentityResponse:
        req = open_api_models.OpenApiRequest()
        return sts_20150401_models.GetCallerIdentityResponse().from_map(
            await self.do_rpcrequest_async('GetCallerIdentity', '2015-04-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_caller_identity(self) -> sts_20150401_models.GetCallerIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_caller_identity_with_options(runtime)

    async def get_caller_identity_async(self) -> sts_20150401_models.GetCallerIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_caller_identity_with_options_async(runtime)
