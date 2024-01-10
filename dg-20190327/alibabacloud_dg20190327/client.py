# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dg20190327 import models as dg_20190327_models
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
            'ap-northeast-1': 'dg.aliyuncs.com',
            'ap-northeast-2-pop': 'dg.aliyuncs.com',
            'ap-south-1': 'dg.aliyuncs.com',
            'ap-southeast-1': 'dg.aliyuncs.com',
            'ap-southeast-2': 'dg.aliyuncs.com',
            'ap-southeast-3': 'dg.aliyuncs.com',
            'ap-southeast-5': 'dg.aliyuncs.com',
            'cn-beijing': 'dg.aliyuncs.com',
            'cn-beijing-finance-1': 'dg.aliyuncs.com',
            'cn-beijing-finance-pop': 'dg.aliyuncs.com',
            'cn-beijing-gov-1': 'dg.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dg.aliyuncs.com',
            'cn-chengdu': 'dg.aliyuncs.com',
            'cn-edge-1': 'dg.aliyuncs.com',
            'cn-fujian': 'dg.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dg.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dg.aliyuncs.com',
            'cn-hangzhou-finance': 'dg.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dg.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dg.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dg.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dg.aliyuncs.com',
            'cn-hangzhou-test-306': 'dg.aliyuncs.com',
            'cn-hongkong': 'dg.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dg.aliyuncs.com',
            'cn-huhehaote': 'dg.aliyuncs.com',
            'cn-north-2-gov-1': 'dg.aliyuncs.com',
            'cn-qingdao': 'dg.aliyuncs.com',
            'cn-qingdao-nebula': 'dg.aliyuncs.com',
            'cn-shanghai': 'dg.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dg.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dg.aliyuncs.com',
            'cn-shanghai-finance-1': 'dg.aliyuncs.com',
            'cn-shanghai-inner': 'dg.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dg.aliyuncs.com',
            'cn-shenzhen': 'dg.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dg.aliyuncs.com',
            'cn-shenzhen-inner': 'dg.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dg.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dg.aliyuncs.com',
            'cn-wuhan': 'dg.aliyuncs.com',
            'cn-yushanfang': 'dg.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dg.aliyuncs.com',
            'cn-zhangjiakou': 'dg.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dg.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dg.aliyuncs.com',
            'eu-central-1': 'dg.aliyuncs.com',
            'eu-west-1': 'dg.aliyuncs.com',
            'eu-west-1-oxs': 'dg.aliyuncs.com',
            'me-east-1': 'dg.aliyuncs.com',
            'rus-west-1-pop': 'dg.aliyuncs.com',
            'us-east-1': 'dg.aliyuncs.com',
            'us-west-1': 'dg.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dg', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_database_with_options(
        self,
        request: dg_20190327_models.AddDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.AddDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.db_description):
            body['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_password):
            body['DbPassword'] = request.db_password
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.db_user_name):
            body['DbUserName'] = request.db_user_name
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDatabase',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.AddDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_database_with_options_async(
        self,
        request: dg_20190327_models.AddDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.AddDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.db_description):
            body['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_password):
            body['DbPassword'] = request.db_password
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.db_user_name):
            body['DbUserName'] = request.db_user_name
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDatabase',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.AddDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_database(
        self,
        request: dg_20190327_models.AddDatabaseRequest,
    ) -> dg_20190327_models.AddDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_database_with_options(request, runtime)

    async def add_database_async(
        self,
        request: dg_20190327_models.AddDatabaseRequest,
    ) -> dg_20190327_models.AddDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_database_with_options_async(request, runtime)

    def add_database_list_with_options(
        self,
        request: dg_20190327_models.AddDatabaseListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.AddDatabaseListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_string):
            body['DatabaseString'] = request.database_string
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDatabaseList',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.AddDatabaseListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_database_list_with_options_async(
        self,
        request: dg_20190327_models.AddDatabaseListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.AddDatabaseListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_string):
            body['DatabaseString'] = request.database_string
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDatabaseList',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.AddDatabaseListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_database_list(
        self,
        request: dg_20190327_models.AddDatabaseListRequest,
    ) -> dg_20190327_models.AddDatabaseListResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_database_list_with_options(request, runtime)

    async def add_database_list_async(
        self,
        request: dg_20190327_models.AddDatabaseListRequest,
    ) -> dg_20190327_models.AddDatabaseListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_database_list_with_options_async(request, runtime)

    def connect_database_with_options(
        self,
        request: dg_20190327_models.ConnectDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.ConnectDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_password):
            body['DbPassword'] = request.db_password
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.db_user_name):
            body['DbUserName'] = request.db_user_name
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConnectDatabase',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.ConnectDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def connect_database_with_options_async(
        self,
        request: dg_20190327_models.ConnectDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.ConnectDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_password):
            body['DbPassword'] = request.db_password
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.db_user_name):
            body['DbUserName'] = request.db_user_name
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConnectDatabase',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.ConnectDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def connect_database(
        self,
        request: dg_20190327_models.ConnectDatabaseRequest,
    ) -> dg_20190327_models.ConnectDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.connect_database_with_options(request, runtime)

    async def connect_database_async(
        self,
        request: dg_20190327_models.ConnectDatabaseRequest,
    ) -> dg_20190327_models.ConnectDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.connect_database_with_options_async(request, runtime)

    def create_database_access_point_with_options(
        self,
        request: dg_20190327_models.CreateDatabaseAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.CreateDatabaseAccessPointResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_azone):
            body['VpcAZone'] = request.vpc_azone
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            body['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatabaseAccessPoint',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.CreateDatabaseAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_access_point_with_options_async(
        self,
        request: dg_20190327_models.CreateDatabaseAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.CreateDatabaseAccessPointResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_azone):
            body['VpcAZone'] = request.vpc_azone
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            body['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatabaseAccessPoint',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.CreateDatabaseAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database_access_point(
        self,
        request: dg_20190327_models.CreateDatabaseAccessPointRequest,
    ) -> dg_20190327_models.CreateDatabaseAccessPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_database_access_point_with_options(request, runtime)

    async def create_database_access_point_async(
        self,
        request: dg_20190327_models.CreateDatabaseAccessPointRequest,
    ) -> dg_20190327_models.CreateDatabaseAccessPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_database_access_point_with_options_async(request, runtime)

    def create_gateway_with_options(
        self,
        request: dg_20190327_models.CreateGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.CreateGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_desc):
            body['GatewayDesc'] = request.gateway_desc
        if not UtilClient.is_unset(request.gateway_name):
            body['GatewayName'] = request.gateway_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGateway',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.CreateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_with_options_async(
        self,
        request: dg_20190327_models.CreateGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.CreateGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_desc):
            body['GatewayDesc'] = request.gateway_desc
        if not UtilClient.is_unset(request.gateway_name):
            body['GatewayName'] = request.gateway_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGateway',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.CreateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway(
        self,
        request: dg_20190327_models.CreateGatewayRequest,
    ) -> dg_20190327_models.CreateGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_with_options(request, runtime)

    async def create_gateway_async(
        self,
        request: dg_20190327_models.CreateGatewayRequest,
    ) -> dg_20190327_models.CreateGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_with_options_async(request, runtime)

    def create_gateway_verify_code_with_options(
        self,
        request: dg_20190327_models.CreateGatewayVerifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.CreateGatewayVerifyCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewayVerifyCode',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.CreateGatewayVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_verify_code_with_options_async(
        self,
        request: dg_20190327_models.CreateGatewayVerifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.CreateGatewayVerifyCodeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewayVerifyCode',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.CreateGatewayVerifyCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_verify_code(
        self,
        request: dg_20190327_models.CreateGatewayVerifyCodeRequest,
    ) -> dg_20190327_models.CreateGatewayVerifyCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_verify_code_with_options(request, runtime)

    async def create_gateway_verify_code_async(
        self,
        request: dg_20190327_models.CreateGatewayVerifyCodeRequest,
    ) -> dg_20190327_models.CreateGatewayVerifyCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_verify_code_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: dg_20190327_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: dg_20190327_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DeleteDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database(
        self,
        request: dg_20190327_models.DeleteDatabaseRequest,
    ) -> dg_20190327_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: dg_20190327_models.DeleteDatabaseRequest,
    ) -> dg_20190327_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_database_access_point_with_options(
        self,
        request: dg_20190327_models.DeleteDatabaseAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DeleteDatabaseAccessPointResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_azone):
            body['VpcAZone'] = request.vpc_azone
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            body['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatabaseAccessPoint',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DeleteDatabaseAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_access_point_with_options_async(
        self,
        request: dg_20190327_models.DeleteDatabaseAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DeleteDatabaseAccessPointResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_azone):
            body['VpcAZone'] = request.vpc_azone
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            body['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatabaseAccessPoint',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DeleteDatabaseAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database_access_point(
        self,
        request: dg_20190327_models.DeleteDatabaseAccessPointRequest,
    ) -> dg_20190327_models.DeleteDatabaseAccessPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_database_access_point_with_options(request, runtime)

    async def delete_database_access_point_async(
        self,
        request: dg_20190327_models.DeleteDatabaseAccessPointRequest,
    ) -> dg_20190327_models.DeleteDatabaseAccessPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_access_point_with_options_async(request, runtime)

    def delete_gateway_with_options(
        self,
        request: dg_20190327_models.DeleteGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DeleteGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        request: dg_20190327_models.DeleteGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DeleteGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        request: dg_20190327_models.DeleteGatewayRequest,
    ) -> dg_20190327_models.DeleteGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_with_options(request, runtime)

    async def delete_gateway_async(
        self,
        request: dg_20190327_models.DeleteGatewayRequest,
    ) -> dg_20190327_models.DeleteGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_with_options_async(request, runtime)

    def delete_gateway_instance_with_options(
        self,
        request: dg_20190327_models.DeleteGatewayInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DeleteGatewayInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_instance_id):
            body['GatewayInstanceId'] = request.gateway_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGatewayInstance',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DeleteGatewayInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_instance_with_options_async(
        self,
        request: dg_20190327_models.DeleteGatewayInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DeleteGatewayInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_instance_id):
            body['GatewayInstanceId'] = request.gateway_instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGatewayInstance',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DeleteGatewayInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_instance(
        self,
        request: dg_20190327_models.DeleteGatewayInstanceRequest,
    ) -> dg_20190327_models.DeleteGatewayInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_instance_with_options(request, runtime)

    async def delete_gateway_instance_async(
        self,
        request: dg_20190327_models.DeleteGatewayInstanceRequest,
    ) -> dg_20190327_models.DeleteGatewayInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_instance_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: dg_20190327_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: dg_20190327_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: dg_20190327_models.DescribeRegionsRequest,
    ) -> dg_20190327_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: dg_20190327_models.DescribeRegionsRequest,
    ) -> dg_20190327_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def download_gateway_program_with_options(
        self,
        request: dg_20190327_models.DownloadGatewayProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DownloadGatewayProgramResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dg_version):
            body['DgVersion'] = request.dg_version
        if not UtilClient.is_unset(request.user_os):
            body['UserOS'] = request.user_os
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadGatewayProgram',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DownloadGatewayProgramResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_gateway_program_with_options_async(
        self,
        request: dg_20190327_models.DownloadGatewayProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.DownloadGatewayProgramResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dg_version):
            body['DgVersion'] = request.dg_version
        if not UtilClient.is_unset(request.user_os):
            body['UserOS'] = request.user_os
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadGatewayProgram',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.DownloadGatewayProgramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_gateway_program(
        self,
        request: dg_20190327_models.DownloadGatewayProgramRequest,
    ) -> dg_20190327_models.DownloadGatewayProgramResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_gateway_program_with_options(request, runtime)

    async def download_gateway_program_async(
        self,
        request: dg_20190327_models.DownloadGatewayProgramRequest,
    ) -> dg_20190327_models.DownloadGatewayProgramResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_gateway_program_with_options_async(request, runtime)

    def find_user_gateway_by_id_with_options(
        self,
        request: dg_20190327_models.FindUserGatewayByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.FindUserGatewayByIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FindUserGatewayById',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.FindUserGatewayByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_user_gateway_by_id_with_options_async(
        self,
        request: dg_20190327_models.FindUserGatewayByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.FindUserGatewayByIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FindUserGatewayById',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.FindUserGatewayByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_user_gateway_by_id(
        self,
        request: dg_20190327_models.FindUserGatewayByIdRequest,
    ) -> dg_20190327_models.FindUserGatewayByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_user_gateway_by_id_with_options(request, runtime)

    async def find_user_gateway_by_id_async(
        self,
        request: dg_20190327_models.FindUserGatewayByIdRequest,
    ) -> dg_20190327_models.FindUserGatewayByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_user_gateway_by_id_with_options_async(request, runtime)

    def get_user_databases_with_options(
        self,
        request: dg_20190327_models.GetUserDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.GetUserDatabasesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserDatabases',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.GetUserDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_databases_with_options_async(
        self,
        request: dg_20190327_models.GetUserDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.GetUserDatabasesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserDatabases',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.GetUserDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_databases(
        self,
        request: dg_20190327_models.GetUserDatabasesRequest,
    ) -> dg_20190327_models.GetUserDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_databases_with_options(request, runtime)

    async def get_user_databases_async(
        self,
        request: dg_20190327_models.GetUserDatabasesRequest,
    ) -> dg_20190327_models.GetUserDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_databases_with_options_async(request, runtime)

    def get_user_gateway_instances_with_options(
        self,
        request: dg_20190327_models.GetUserGatewayInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.GetUserGatewayInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserGatewayInstances',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.GetUserGatewayInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_gateway_instances_with_options_async(
        self,
        request: dg_20190327_models.GetUserGatewayInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.GetUserGatewayInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserGatewayInstances',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.GetUserGatewayInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_gateway_instances(
        self,
        request: dg_20190327_models.GetUserGatewayInstancesRequest,
    ) -> dg_20190327_models.GetUserGatewayInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_gateway_instances_with_options(request, runtime)

    async def get_user_gateway_instances_async(
        self,
        request: dg_20190327_models.GetUserGatewayInstancesRequest,
    ) -> dg_20190327_models.GetUserGatewayInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_gateway_instances_with_options_async(request, runtime)

    def get_user_gateways_with_options(
        self,
        request: dg_20190327_models.GetUserGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.GetUserGatewaysResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserGateways',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.GetUserGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_gateways_with_options_async(
        self,
        request: dg_20190327_models.GetUserGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.GetUserGatewaysResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserGateways',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.GetUserGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_gateways(
        self,
        request: dg_20190327_models.GetUserGatewaysRequest,
    ) -> dg_20190327_models.GetUserGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_gateways_with_options(request, runtime)

    async def get_user_gateways_async(
        self,
        request: dg_20190327_models.GetUserGatewaysRequest,
    ) -> dg_20190327_models.GetUserGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_gateways_with_options_async(request, runtime)

    def list_database_access_point_with_options(
        self,
        request: dg_20190327_models.ListDatabaseAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.ListDatabaseAccessPointResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatabaseAccessPoint',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.ListDatabaseAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_access_point_with_options_async(
        self,
        request: dg_20190327_models.ListDatabaseAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.ListDatabaseAccessPointResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatabaseAccessPoint',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.ListDatabaseAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_database_access_point(
        self,
        request: dg_20190327_models.ListDatabaseAccessPointRequest,
    ) -> dg_20190327_models.ListDatabaseAccessPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_database_access_point_with_options(request, runtime)

    async def list_database_access_point_async(
        self,
        request: dg_20190327_models.ListDatabaseAccessPointRequest,
    ) -> dg_20190327_models.ListDatabaseAccessPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_database_access_point_with_options_async(request, runtime)

    def modify_database_with_options(
        self,
        request: dg_20190327_models.ModifyDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.ModifyDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_description):
            body['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_password):
            body['DbPassword'] = request.db_password
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.db_user_name):
            body['DbUserName'] = request.db_user_name
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDatabase',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.ModifyDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_with_options_async(
        self,
        request: dg_20190327_models.ModifyDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.ModifyDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_description):
            body['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_password):
            body['DbPassword'] = request.db_password
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.db_user_name):
            body['DbUserName'] = request.db_user_name
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDatabase',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.ModifyDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database(
        self,
        request: dg_20190327_models.ModifyDatabaseRequest,
    ) -> dg_20190327_models.ModifyDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_database_with_options(request, runtime)

    async def modify_database_async(
        self,
        request: dg_20190327_models.ModifyDatabaseRequest,
    ) -> dg_20190327_models.ModifyDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_with_options_async(request, runtime)

    def modify_gateway_with_options(
        self,
        request: dg_20190327_models.ModifyGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.ModifyGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_desc):
            body['GatewayDesc'] = request.gateway_desc
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_name):
            body['GatewayName'] = request.gateway_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyGateway',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.ModifyGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_gateway_with_options_async(
        self,
        request: dg_20190327_models.ModifyGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.ModifyGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_desc):
            body['GatewayDesc'] = request.gateway_desc
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_name):
            body['GatewayName'] = request.gateway_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyGateway',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.ModifyGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_gateway(
        self,
        request: dg_20190327_models.ModifyGatewayRequest,
    ) -> dg_20190327_models.ModifyGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_gateway_with_options(request, runtime)

    async def modify_gateway_async(
        self,
        request: dg_20190327_models.ModifyGatewayRequest,
    ) -> dg_20190327_models.ModifyGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_gateway_with_options_async(request, runtime)

    def retry_database_with_options(
        self,
        request: dg_20190327_models.RetryDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.RetryDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.db_description):
            body['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_password):
            body['DbPassword'] = request.db_password
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.db_user_name):
            body['DbUserName'] = request.db_user_name
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryDatabase',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.RetryDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_database_with_options_async(
        self,
        request: dg_20190327_models.RetryDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.RetryDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.db_description):
            body['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_password):
            body['DbPassword'] = request.db_password
        if not UtilClient.is_unset(request.db_type):
            body['DbType'] = request.db_type
        if not UtilClient.is_unset(request.db_user_name):
            body['DbUserName'] = request.db_user_name
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryDatabase',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.RetryDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_database(
        self,
        request: dg_20190327_models.RetryDatabaseRequest,
    ) -> dg_20190327_models.RetryDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_database_with_options(request, runtime)

    async def retry_database_async(
        self,
        request: dg_20190327_models.RetryDatabaseRequest,
    ) -> dg_20190327_models.RetryDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_database_with_options_async(request, runtime)

    def stop_gateway_with_options(
        self,
        request: dg_20190327_models.StopGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.StopGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_instance_id):
            body['GatewayInstanceId'] = request.gateway_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopGateway',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.StopGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_gateway_with_options_async(
        self,
        request: dg_20190327_models.StopGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dg_20190327_models.StopGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_instance_id):
            body['GatewayInstanceId'] = request.gateway_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopGateway',
            version='2019-03-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dg_20190327_models.StopGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_gateway(
        self,
        request: dg_20190327_models.StopGatewayRequest,
    ) -> dg_20190327_models.StopGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_gateway_with_options(request, runtime)

    async def stop_gateway_async(
        self,
        request: dg_20190327_models.StopGatewayRequest,
    ) -> dg_20190327_models.StopGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_gateway_with_options_async(request, runtime)
