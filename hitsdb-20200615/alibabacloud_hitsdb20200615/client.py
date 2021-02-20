# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hitsdb20200615 import models as hitsdb_20200615_models
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
            'cn-qingdao': 'hitsdb.aliyuncs.com',
            'cn-beijing': 'hitsdb.aliyuncs.com',
            'cn-hangzhou': 'hitsdb.aliyuncs.com',
            'cn-shanghai': 'hitsdb.aliyuncs.com',
            'cn-shenzhen': 'hitsdb.aliyuncs.com',
            'cn-hongkong': 'hitsdb.aliyuncs.com',
            'ap-southeast-1': 'hitsdb.aliyuncs.com',
            'us-west-1': 'hitsdb.aliyuncs.com',
            'us-east-1': 'hitsdb.aliyuncs.com',
            'cn-shanghai-finance-1': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'hitsdb.aliyuncs.com',
            'ap-northeast-2-pop': 'hitsdb.aliyuncs.com',
            'cn-beijing-finance-1': 'hitsdb.aliyuncs.com',
            'cn-beijing-finance-pop': 'hitsdb.aliyuncs.com',
            'cn-beijing-gov-1': 'hitsdb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'hitsdb.aliyuncs.com',
            'cn-chengdu': 'hitsdb.aliyuncs.com',
            'cn-edge-1': 'hitsdb.aliyuncs.com',
            'cn-fujian': 'hitsdb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-finance': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-test-306': 'hitsdb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'hitsdb.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'hitsdb.aliyuncs.com',
            'cn-qingdao-nebula': 'hitsdb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'hitsdb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'hitsdb.aliyuncs.com',
            'cn-shanghai-inner': 'hitsdb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-inner': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'hitsdb.aliyuncs.com',
            'cn-wuhan': 'hitsdb.aliyuncs.com',
            'cn-wulanchabu': 'hitsdb.aliyuncs.com',
            'cn-yushanfang': 'hitsdb.aliyuncs.com',
            'cn-zhangbei': 'hitsdb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'hitsdb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'hitsdb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'hitsdb.aliyuncs.com',
            'eu-west-1-oxs': 'hitsdb.aliyuncs.com',
            'me-east-1': 'hitsdb.aliyuncs.com',
            'rus-west-1-pop': 'hitsdb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('hitsdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_regions_with_options(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def get_instance_ip_white_list_with_options(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.GetInstanceIpWhiteListResponse().from_map(
            self.do_rpcrequest('GetInstanceIpWhiteList', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_ip_white_list_with_options_async(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.GetInstanceIpWhiteListResponse().from_map(
            await self.do_rpcrequest_async('GetInstanceIpWhiteList', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_ip_white_list(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_ip_white_list_with_options(request, runtime)

    async def get_instance_ip_white_list_async(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_ip_white_list_with_options_async(request, runtime)

    def get_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.GetLindormInstanceResponse().from_map(
            self.do_rpcrequest('GetLindormInstance', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.GetLindormInstanceResponse().from_map(
            await self.do_rpcrequest_async('GetLindormInstance', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_lindorm_instance(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_instance_with_options(request, runtime)

    async def get_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_instance_with_options_async(request, runtime)

    def get_lindorm_instance_engine_list_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.GetLindormInstanceEngineListResponse().from_map(
            self.do_rpcrequest('GetLindormInstanceEngineList', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_lindorm_instance_engine_list_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.GetLindormInstanceEngineListResponse().from_map(
            await self.do_rpcrequest_async('GetLindormInstanceEngineList', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_lindorm_instance_engine_list(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_instance_engine_list_with_options(request, runtime)

    async def get_lindorm_instance_engine_list_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_instance_engine_list_with_options_async(request, runtime)

    def get_lindorm_instance_list_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.GetLindormInstanceListResponse().from_map(
            self.do_rpcrequest('GetLindormInstanceList', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_lindorm_instance_list_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.GetLindormInstanceListResponse().from_map(
            await self.do_rpcrequest_async('GetLindormInstanceList', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_lindorm_instance_list(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_instance_list_with_options(request, runtime)

    async def get_lindorm_instance_list_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_instance_list_with_options_async(request, runtime)

    def update_instance_ip_white_list_with_options(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse().from_map(
            self.do_rpcrequest('UpdateInstanceIpWhiteList', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_instance_ip_white_list_with_options_async(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse().from_map(
            await self.do_rpcrequest_async('UpdateInstanceIpWhiteList', '2020-06-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance_ip_white_list(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_ip_white_list_with_options(request, runtime)

    async def update_instance_ip_white_list_async(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_ip_white_list_with_options_async(request, runtime)
