# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eais20190624 import models as eais_20190624_models
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
            'ap-northeast-1': 'eais.aliyuncs.com',
            'ap-northeast-2-pop': 'eais.aliyuncs.com',
            'ap-south-1': 'eais.aliyuncs.com',
            'ap-southeast-1': 'eais.aliyuncs.com',
            'ap-southeast-2': 'eais.aliyuncs.com',
            'ap-southeast-3': 'eais.aliyuncs.com',
            'ap-southeast-5': 'eais.aliyuncs.com',
            'cn-beijing-finance-1': 'eais.aliyuncs.com',
            'cn-beijing-finance-pop': 'eais.aliyuncs.com',
            'cn-beijing-gov-1': 'eais.aliyuncs.com',
            'cn-beijing-nu16-b01': 'eais.aliyuncs.com',
            'cn-edge-1': 'eais.aliyuncs.com',
            'cn-fujian': 'eais.aliyuncs.com',
            'cn-haidian-cm12-c01': 'eais.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'eais.aliyuncs.com',
            'cn-hangzhou-finance': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'eais.aliyuncs.com',
            'cn-hangzhou-test-306': 'eais.aliyuncs.com',
            'cn-hongkong': 'eais.aliyuncs.com',
            'cn-hongkong-finance-pop': 'eais.aliyuncs.com',
            'cn-huhehaote': 'eais.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'eais.aliyuncs.com',
            'cn-north-2-gov-1': 'eais.aliyuncs.com',
            'cn-qingdao': 'eais.aliyuncs.com',
            'cn-qingdao-nebula': 'eais.aliyuncs.com',
            'cn-shanghai-et15-b01': 'eais.aliyuncs.com',
            'cn-shanghai-et2-b01': 'eais.aliyuncs.com',
            'cn-shanghai-finance-1': 'eais.aliyuncs.com',
            'cn-shanghai-inner': 'eais.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'eais.aliyuncs.com',
            'cn-shenzhen-finance-1': 'eais.aliyuncs.com',
            'cn-shenzhen-inner': 'eais.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'eais.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'eais.aliyuncs.com',
            'cn-wuhan': 'eais.aliyuncs.com',
            'cn-wulanchabu': 'eais.aliyuncs.com',
            'cn-yushanfang': 'eais.aliyuncs.com',
            'cn-zhangbei': 'eais.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'eais.aliyuncs.com',
            'cn-zhangjiakou': 'eais.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'eais.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'eais.aliyuncs.com',
            'eu-central-1': 'eais.aliyuncs.com',
            'eu-west-1': 'eais.aliyuncs.com',
            'eu-west-1-oxs': 'eais.aliyuncs.com',
            'me-east-1': 'eais.aliyuncs.com',
            'rus-west-1-pop': 'eais.aliyuncs.com',
            'us-east-1': 'eais.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('eais', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_eai_with_options(
        self,
        request: eais_20190624_models.AttachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.AttachEaiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.AttachEaiResponse().from_map(
            self.do_rpcrequest('AttachEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_eai_with_options_async(
        self,
        request: eais_20190624_models.AttachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.AttachEaiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.AttachEaiResponse().from_map(
            await self.do_rpcrequest_async('AttachEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_eai(
        self,
        request: eais_20190624_models.AttachEaiRequest,
    ) -> eais_20190624_models.AttachEaiResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_eai_with_options(request, runtime)

    async def attach_eai_async(
        self,
        request: eais_20190624_models.AttachEaiRequest,
    ) -> eais_20190624_models.AttachEaiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_eai_with_options_async(request, runtime)

    def create_eai_with_options(
        self,
        request: eais_20190624_models.CreateEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.CreateEaiResponse().from_map(
            self.do_rpcrequest('CreateEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_eai_with_options_async(
        self,
        request: eais_20190624_models.CreateEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.CreateEaiResponse().from_map(
            await self.do_rpcrequest_async('CreateEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_eai(
        self,
        request: eais_20190624_models.CreateEaiRequest,
    ) -> eais_20190624_models.CreateEaiResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_eai_with_options(request, runtime)

    async def create_eai_async(
        self,
        request: eais_20190624_models.CreateEaiRequest,
    ) -> eais_20190624_models.CreateEaiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_eai_with_options_async(request, runtime)

    def create_eai_all_with_options(
        self,
        request: eais_20190624_models.CreateEaiAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.CreateEaiAllResponse().from_map(
            self.do_rpcrequest('CreateEaiAll', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_eai_all_with_options_async(
        self,
        request: eais_20190624_models.CreateEaiAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.CreateEaiAllResponse().from_map(
            await self.do_rpcrequest_async('CreateEaiAll', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_eai_all(
        self,
        request: eais_20190624_models.CreateEaiAllRequest,
    ) -> eais_20190624_models.CreateEaiAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_eai_all_with_options(request, runtime)

    async def create_eai_all_async(
        self,
        request: eais_20190624_models.CreateEaiAllRequest,
    ) -> eais_20190624_models.CreateEaiAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_eai_all_with_options_async(request, runtime)

    def delete_eai_with_options(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DeleteEaiResponse().from_map(
            self.do_rpcrequest('DeleteEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_eai_with_options_async(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DeleteEaiResponse().from_map(
            await self.do_rpcrequest_async('DeleteEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_eai(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
    ) -> eais_20190624_models.DeleteEaiResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_eai_with_options(request, runtime)

    async def delete_eai_async(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
    ) -> eais_20190624_models.DeleteEaiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_eai_with_options_async(request, runtime)

    def delete_eai_all_with_options(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DeleteEaiAllResponse().from_map(
            self.do_rpcrequest('DeleteEaiAll', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_eai_all_with_options_async(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DeleteEaiAllResponse().from_map(
            await self.do_rpcrequest_async('DeleteEaiAll', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_eai_all(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_eai_all_with_options(request, runtime)

    async def delete_eai_all_async(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_eai_all_with_options_async(request, runtime)

    def describe_eais_with_options(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeEaisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DescribeEaisResponse().from_map(
            self.do_rpcrequest('DescribeEais', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_eais_with_options_async(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeEaisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DescribeEaisResponse().from_map(
            await self.do_rpcrequest_async('DescribeEais', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eais(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
    ) -> eais_20190624_models.DescribeEaisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eais_with_options(request, runtime)

    async def describe_eais_async(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
    ) -> eais_20190624_models.DescribeEaisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eais_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return eais_20190624_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return eais_20190624_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self) -> eais_20190624_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> eais_20190624_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def detach_eai_with_options(
        self,
        request: eais_20190624_models.DetachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DetachEaiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DetachEaiResponse().from_map(
            self.do_rpcrequest('DetachEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_eai_with_options_async(
        self,
        request: eais_20190624_models.DetachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DetachEaiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.DetachEaiResponse().from_map(
            await self.do_rpcrequest_async('DetachEai', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_eai(
        self,
        request: eais_20190624_models.DetachEaiRequest,
    ) -> eais_20190624_models.DetachEaiResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_eai_with_options(request, runtime)

    async def detach_eai_async(
        self,
        request: eais_20190624_models.DetachEaiRequest,
    ) -> eais_20190624_models.DetachEaiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_eai_with_options_async(request, runtime)

    def get_private_ip_with_options(
        self,
        request: eais_20190624_models.GetPrivateIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.GetPrivateIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.GetPrivateIpResponse().from_map(
            self.do_rpcrequest('GetPrivateIp', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_private_ip_with_options_async(
        self,
        request: eais_20190624_models.GetPrivateIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.GetPrivateIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return eais_20190624_models.GetPrivateIpResponse().from_map(
            await self.do_rpcrequest_async('GetPrivateIp', '2019-06-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_private_ip(
        self,
        request: eais_20190624_models.GetPrivateIpRequest,
    ) -> eais_20190624_models.GetPrivateIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_private_ip_with_options(request, runtime)

    async def get_private_ip_async(
        self,
        request: eais_20190624_models.GetPrivateIpRequest,
    ) -> eais_20190624_models.GetPrivateIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_private_ip_with_options_async(request, runtime)
