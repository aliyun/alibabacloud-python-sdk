# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dms_dg20230914 import models as dms_dg_20230914_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('dms-dg', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: dms_dg_20230914_models.AddDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.AddDatabaseResponse:
        """
        @param request: AddDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDatabaseResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.AddDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_database_with_options_async(
        self,
        request: dms_dg_20230914_models.AddDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.AddDatabaseResponse:
        """
        @param request: AddDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDatabaseResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.AddDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_database(
        self,
        request: dms_dg_20230914_models.AddDatabaseRequest,
    ) -> dms_dg_20230914_models.AddDatabaseResponse:
        """
        @param request: AddDatabaseRequest
        @return: AddDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_database_with_options(request, runtime)

    async def add_database_async(
        self,
        request: dms_dg_20230914_models.AddDatabaseRequest,
    ) -> dms_dg_20230914_models.AddDatabaseResponse:
        """
        @param request: AddDatabaseRequest
        @return: AddDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_database_with_options_async(request, runtime)

    def add_database_list_with_options(
        self,
        request: dms_dg_20230914_models.AddDatabaseListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.AddDatabaseListResponse:
        """
        @param request: AddDatabaseListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDatabaseListResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.AddDatabaseListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_database_list_with_options_async(
        self,
        request: dms_dg_20230914_models.AddDatabaseListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.AddDatabaseListResponse:
        """
        @param request: AddDatabaseListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDatabaseListResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.AddDatabaseListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_database_list(
        self,
        request: dms_dg_20230914_models.AddDatabaseListRequest,
    ) -> dms_dg_20230914_models.AddDatabaseListResponse:
        """
        @param request: AddDatabaseListRequest
        @return: AddDatabaseListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_database_list_with_options(request, runtime)

    async def add_database_list_async(
        self,
        request: dms_dg_20230914_models.AddDatabaseListRequest,
    ) -> dms_dg_20230914_models.AddDatabaseListResponse:
        """
        @param request: AddDatabaseListRequest
        @return: AddDatabaseListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_database_list_with_options_async(request, runtime)

    def check_dgenabled_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.CheckDGEnabledResponse:
        """
        @param request: CheckDGEnabledRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDGEnabledResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckDGEnabled',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.CheckDGEnabledResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_dgenabled_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.CheckDGEnabledResponse:
        """
        @param request: CheckDGEnabledRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDGEnabledResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckDGEnabled',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.CheckDGEnabledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_dgenabled(self) -> dms_dg_20230914_models.CheckDGEnabledResponse:
        """
        @return: CheckDGEnabledResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_dgenabled_with_options(runtime)

    async def check_dgenabled_async(self) -> dms_dg_20230914_models.CheckDGEnabledResponse:
        """
        @return: CheckDGEnabledResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_dgenabled_with_options_async(runtime)

    def connect_database_with_options(
        self,
        request: dms_dg_20230914_models.ConnectDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.ConnectDatabaseResponse:
        """
        @param request: ConnectDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConnectDatabaseResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.ConnectDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def connect_database_with_options_async(
        self,
        request: dms_dg_20230914_models.ConnectDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.ConnectDatabaseResponse:
        """
        @param request: ConnectDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConnectDatabaseResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.ConnectDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def connect_database(
        self,
        request: dms_dg_20230914_models.ConnectDatabaseRequest,
    ) -> dms_dg_20230914_models.ConnectDatabaseResponse:
        """
        @param request: ConnectDatabaseRequest
        @return: ConnectDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.connect_database_with_options(request, runtime)

    async def connect_database_async(
        self,
        request: dms_dg_20230914_models.ConnectDatabaseRequest,
    ) -> dms_dg_20230914_models.ConnectDatabaseResponse:
        """
        @param request: ConnectDatabaseRequest
        @return: ConnectDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.connect_database_with_options_async(request, runtime)

    def create_gateway_with_options(
        self,
        request: dms_dg_20230914_models.CreateGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.CreateGatewayResponse:
        """
        @summary 创建网关
        
        @param request: CreateGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.CreateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_with_options_async(
        self,
        request: dms_dg_20230914_models.CreateGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.CreateGatewayResponse:
        """
        @summary 创建网关
        
        @param request: CreateGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.CreateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway(
        self,
        request: dms_dg_20230914_models.CreateGatewayRequest,
    ) -> dms_dg_20230914_models.CreateGatewayResponse:
        """
        @summary 创建网关
        
        @param request: CreateGatewayRequest
        @return: CreateGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_with_options(request, runtime)

    async def create_gateway_async(
        self,
        request: dms_dg_20230914_models.CreateGatewayRequest,
    ) -> dms_dg_20230914_models.CreateGatewayResponse:
        """
        @summary 创建网关
        
        @param request: CreateGatewayRequest
        @return: CreateGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_with_options_async(request, runtime)

    def create_gateway_verify_code_with_options(
        self,
        request: dms_dg_20230914_models.CreateGatewayVerifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.CreateGatewayVerifyCodeResponse:
        """
        @summary 创建网关的随机验证码
        
        @param request: CreateGatewayVerifyCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayVerifyCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewayVerifyCode',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.CreateGatewayVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_verify_code_with_options_async(
        self,
        request: dms_dg_20230914_models.CreateGatewayVerifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.CreateGatewayVerifyCodeResponse:
        """
        @summary 创建网关的随机验证码
        
        @param request: CreateGatewayVerifyCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewayVerifyCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewayVerifyCode',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.CreateGatewayVerifyCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_verify_code(
        self,
        request: dms_dg_20230914_models.CreateGatewayVerifyCodeRequest,
    ) -> dms_dg_20230914_models.CreateGatewayVerifyCodeResponse:
        """
        @summary 创建网关的随机验证码
        
        @param request: CreateGatewayVerifyCodeRequest
        @return: CreateGatewayVerifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_verify_code_with_options(request, runtime)

    async def create_gateway_verify_code_async(
        self,
        request: dms_dg_20230914_models.CreateGatewayVerifyCodeRequest,
    ) -> dms_dg_20230914_models.CreateGatewayVerifyCodeResponse:
        """
        @summary 创建网关的随机验证码
        
        @param request: CreateGatewayVerifyCodeRequest
        @return: CreateGatewayVerifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_verify_code_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: dms_dg_20230914_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.DeleteDatabaseResponse:
        """
        @param request: DeleteDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatabaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: dms_dg_20230914_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.DeleteDatabaseResponse:
        """
        @param request: DeleteDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatabaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.DeleteDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database(
        self,
        request: dms_dg_20230914_models.DeleteDatabaseRequest,
    ) -> dms_dg_20230914_models.DeleteDatabaseResponse:
        """
        @param request: DeleteDatabaseRequest
        @return: DeleteDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: dms_dg_20230914_models.DeleteDatabaseRequest,
    ) -> dms_dg_20230914_models.DeleteDatabaseResponse:
        """
        @param request: DeleteDatabaseRequest
        @return: DeleteDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_gateway_with_options(
        self,
        request: dms_dg_20230914_models.DeleteGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.DeleteGatewayResponse:
        """
        @summary 删除网关
        
        @param request: DeleteGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        request: dms_dg_20230914_models.DeleteGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.DeleteGatewayResponse:
        """
        @summary 删除网关
        
        @param request: DeleteGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        request: dms_dg_20230914_models.DeleteGatewayRequest,
    ) -> dms_dg_20230914_models.DeleteGatewayResponse:
        """
        @summary 删除网关
        
        @param request: DeleteGatewayRequest
        @return: DeleteGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_with_options(request, runtime)

    async def delete_gateway_async(
        self,
        request: dms_dg_20230914_models.DeleteGatewayRequest,
    ) -> dms_dg_20230914_models.DeleteGatewayResponse:
        """
        @summary 删除网关
        
        @param request: DeleteGatewayRequest
        @return: DeleteGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_with_options_async(request, runtime)

    def delete_gateway_instance_with_options(
        self,
        request: dms_dg_20230914_models.DeleteGatewayInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.DeleteGatewayInstanceResponse:
        """
        @param request: DeleteGatewayInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayInstanceResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.DeleteGatewayInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_instance_with_options_async(
        self,
        request: dms_dg_20230914_models.DeleteGatewayInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.DeleteGatewayInstanceResponse:
        """
        @param request: DeleteGatewayInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayInstanceResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.DeleteGatewayInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_instance(
        self,
        request: dms_dg_20230914_models.DeleteGatewayInstanceRequest,
    ) -> dms_dg_20230914_models.DeleteGatewayInstanceResponse:
        """
        @param request: DeleteGatewayInstanceRequest
        @return: DeleteGatewayInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_instance_with_options(request, runtime)

    async def delete_gateway_instance_async(
        self,
        request: dms_dg_20230914_models.DeleteGatewayInstanceRequest,
    ) -> dms_dg_20230914_models.DeleteGatewayInstanceResponse:
        """
        @param request: DeleteGatewayInstanceRequest
        @return: DeleteGatewayInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_instance_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: dms_dg_20230914_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: dms_dg_20230914_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: dms_dg_20230914_models.DescribeRegionsRequest,
    ) -> dms_dg_20230914_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: dms_dg_20230914_models.DescribeRegionsRequest,
    ) -> dms_dg_20230914_models.DescribeRegionsResponse:
        """
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def download_gateway_program_with_options(
        self,
        request: dms_dg_20230914_models.DownloadGatewayProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.DownloadGatewayProgramResponse:
        """
        @param request: DownloadGatewayProgramRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadGatewayProgramResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.DownloadGatewayProgramResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_gateway_program_with_options_async(
        self,
        request: dms_dg_20230914_models.DownloadGatewayProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.DownloadGatewayProgramResponse:
        """
        @param request: DownloadGatewayProgramRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadGatewayProgramResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.DownloadGatewayProgramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_gateway_program(
        self,
        request: dms_dg_20230914_models.DownloadGatewayProgramRequest,
    ) -> dms_dg_20230914_models.DownloadGatewayProgramResponse:
        """
        @param request: DownloadGatewayProgramRequest
        @return: DownloadGatewayProgramResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.download_gateway_program_with_options(request, runtime)

    async def download_gateway_program_async(
        self,
        request: dms_dg_20230914_models.DownloadGatewayProgramRequest,
    ) -> dms_dg_20230914_models.DownloadGatewayProgramResponse:
        """
        @param request: DownloadGatewayProgramRequest
        @return: DownloadGatewayProgramResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.download_gateway_program_with_options_async(request, runtime)

    def find_user_gateway_by_id_with_options(
        self,
        request: dms_dg_20230914_models.FindUserGatewayByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.FindUserGatewayByIdResponse:
        """
        @summary 根据GatewayId查找网关详情
        
        @param request: FindUserGatewayByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindUserGatewayByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FindUserGatewayById',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.FindUserGatewayByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_user_gateway_by_id_with_options_async(
        self,
        request: dms_dg_20230914_models.FindUserGatewayByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.FindUserGatewayByIdResponse:
        """
        @summary 根据GatewayId查找网关详情
        
        @param request: FindUserGatewayByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FindUserGatewayByIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FindUserGatewayById',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.FindUserGatewayByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_user_gateway_by_id(
        self,
        request: dms_dg_20230914_models.FindUserGatewayByIdRequest,
    ) -> dms_dg_20230914_models.FindUserGatewayByIdResponse:
        """
        @summary 根据GatewayId查找网关详情
        
        @param request: FindUserGatewayByIdRequest
        @return: FindUserGatewayByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.find_user_gateway_by_id_with_options(request, runtime)

    async def find_user_gateway_by_id_async(
        self,
        request: dms_dg_20230914_models.FindUserGatewayByIdRequest,
    ) -> dms_dg_20230914_models.FindUserGatewayByIdResponse:
        """
        @summary 根据GatewayId查找网关详情
        
        @param request: FindUserGatewayByIdRequest
        @return: FindUserGatewayByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.find_user_gateway_by_id_with_options_async(request, runtime)

    def get_user_databases_with_options(
        self,
        request: dms_dg_20230914_models.GetUserDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.GetUserDatabasesResponse:
        """
        @param request: GetUserDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserDatabasesResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.GetUserDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_databases_with_options_async(
        self,
        request: dms_dg_20230914_models.GetUserDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.GetUserDatabasesResponse:
        """
        @param request: GetUserDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserDatabasesResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.GetUserDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_databases(
        self,
        request: dms_dg_20230914_models.GetUserDatabasesRequest,
    ) -> dms_dg_20230914_models.GetUserDatabasesResponse:
        """
        @param request: GetUserDatabasesRequest
        @return: GetUserDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_databases_with_options(request, runtime)

    async def get_user_databases_async(
        self,
        request: dms_dg_20230914_models.GetUserDatabasesRequest,
    ) -> dms_dg_20230914_models.GetUserDatabasesResponse:
        """
        @param request: GetUserDatabasesRequest
        @return: GetUserDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_databases_with_options_async(request, runtime)

    def get_user_gateway_instances_with_options(
        self,
        request: dms_dg_20230914_models.GetUserGatewayInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.GetUserGatewayInstancesResponse:
        """
        @param request: GetUserGatewayInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGatewayInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserGatewayInstances',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.GetUserGatewayInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_gateway_instances_with_options_async(
        self,
        request: dms_dg_20230914_models.GetUserGatewayInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.GetUserGatewayInstancesResponse:
        """
        @param request: GetUserGatewayInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGatewayInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gateway_id):
            body['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserGatewayInstances',
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.GetUserGatewayInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_gateway_instances(
        self,
        request: dms_dg_20230914_models.GetUserGatewayInstancesRequest,
    ) -> dms_dg_20230914_models.GetUserGatewayInstancesResponse:
        """
        @param request: GetUserGatewayInstancesRequest
        @return: GetUserGatewayInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_gateway_instances_with_options(request, runtime)

    async def get_user_gateway_instances_async(
        self,
        request: dms_dg_20230914_models.GetUserGatewayInstancesRequest,
    ) -> dms_dg_20230914_models.GetUserGatewayInstancesResponse:
        """
        @param request: GetUserGatewayInstancesRequest
        @return: GetUserGatewayInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_gateway_instances_with_options_async(request, runtime)

    def get_user_gateways_with_options(
        self,
        request: dms_dg_20230914_models.GetUserGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.GetUserGatewaysResponse:
        """
        @summary 获取用户DG网关列表
        
        @param request: GetUserGatewaysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGatewaysResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.GetUserGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_gateways_with_options_async(
        self,
        request: dms_dg_20230914_models.GetUserGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.GetUserGatewaysResponse:
        """
        @summary 获取用户DG网关列表
        
        @param request: GetUserGatewaysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGatewaysResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.GetUserGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_gateways(
        self,
        request: dms_dg_20230914_models.GetUserGatewaysRequest,
    ) -> dms_dg_20230914_models.GetUserGatewaysResponse:
        """
        @summary 获取用户DG网关列表
        
        @param request: GetUserGatewaysRequest
        @return: GetUserGatewaysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_gateways_with_options(request, runtime)

    async def get_user_gateways_async(
        self,
        request: dms_dg_20230914_models.GetUserGatewaysRequest,
    ) -> dms_dg_20230914_models.GetUserGatewaysResponse:
        """
        @summary 获取用户DG网关列表
        
        @param request: GetUserGatewaysRequest
        @return: GetUserGatewaysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_gateways_with_options_async(request, runtime)

    def list_database_access_point_with_options(
        self,
        request: dms_dg_20230914_models.ListDatabaseAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.ListDatabaseAccessPointResponse:
        """
        @param request: ListDatabaseAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabaseAccessPointResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.ListDatabaseAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_access_point_with_options_async(
        self,
        request: dms_dg_20230914_models.ListDatabaseAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.ListDatabaseAccessPointResponse:
        """
        @param request: ListDatabaseAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabaseAccessPointResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.ListDatabaseAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_database_access_point(
        self,
        request: dms_dg_20230914_models.ListDatabaseAccessPointRequest,
    ) -> dms_dg_20230914_models.ListDatabaseAccessPointResponse:
        """
        @param request: ListDatabaseAccessPointRequest
        @return: ListDatabaseAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_database_access_point_with_options(request, runtime)

    async def list_database_access_point_async(
        self,
        request: dms_dg_20230914_models.ListDatabaseAccessPointRequest,
    ) -> dms_dg_20230914_models.ListDatabaseAccessPointResponse:
        """
        @param request: ListDatabaseAccessPointRequest
        @return: ListDatabaseAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_database_access_point_with_options_async(request, runtime)

    def modify_database_with_options(
        self,
        request: dms_dg_20230914_models.ModifyDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.ModifyDatabaseResponse:
        """
        @param request: ModifyDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.ModifyDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_with_options_async(
        self,
        request: dms_dg_20230914_models.ModifyDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.ModifyDatabaseResponse:
        """
        @param request: ModifyDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.ModifyDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database(
        self,
        request: dms_dg_20230914_models.ModifyDatabaseRequest,
    ) -> dms_dg_20230914_models.ModifyDatabaseResponse:
        """
        @param request: ModifyDatabaseRequest
        @return: ModifyDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_database_with_options(request, runtime)

    async def modify_database_async(
        self,
        request: dms_dg_20230914_models.ModifyDatabaseRequest,
    ) -> dms_dg_20230914_models.ModifyDatabaseResponse:
        """
        @param request: ModifyDatabaseRequest
        @return: ModifyDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_with_options_async(request, runtime)

    def modify_gateway_with_options(
        self,
        request: dms_dg_20230914_models.ModifyGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.ModifyGatewayResponse:
        """
        @summary 修改网关信息
        
        @param request: ModifyGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGatewayResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.ModifyGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_gateway_with_options_async(
        self,
        request: dms_dg_20230914_models.ModifyGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.ModifyGatewayResponse:
        """
        @summary 修改网关信息
        
        @param request: ModifyGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGatewayResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.ModifyGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_gateway(
        self,
        request: dms_dg_20230914_models.ModifyGatewayRequest,
    ) -> dms_dg_20230914_models.ModifyGatewayResponse:
        """
        @summary 修改网关信息
        
        @param request: ModifyGatewayRequest
        @return: ModifyGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_gateway_with_options(request, runtime)

    async def modify_gateway_async(
        self,
        request: dms_dg_20230914_models.ModifyGatewayRequest,
    ) -> dms_dg_20230914_models.ModifyGatewayResponse:
        """
        @summary 修改网关信息
        
        @param request: ModifyGatewayRequest
        @return: ModifyGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_gateway_with_options_async(request, runtime)

    def retry_database_with_options(
        self,
        request: dms_dg_20230914_models.RetryDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.RetryDatabaseResponse:
        """
        @param request: RetryDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryDatabaseResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.RetryDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_database_with_options_async(
        self,
        request: dms_dg_20230914_models.RetryDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.RetryDatabaseResponse:
        """
        @param request: RetryDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryDatabaseResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.RetryDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_database(
        self,
        request: dms_dg_20230914_models.RetryDatabaseRequest,
    ) -> dms_dg_20230914_models.RetryDatabaseResponse:
        """
        @param request: RetryDatabaseRequest
        @return: RetryDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retry_database_with_options(request, runtime)

    async def retry_database_async(
        self,
        request: dms_dg_20230914_models.RetryDatabaseRequest,
    ) -> dms_dg_20230914_models.RetryDatabaseResponse:
        """
        @param request: RetryDatabaseRequest
        @return: RetryDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.retry_database_with_options_async(request, runtime)

    def stop_gateway_with_options(
        self,
        request: dms_dg_20230914_models.StopGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.StopGatewayResponse:
        """
        @summary 停止网关实例
        
        @param request: StopGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopGatewayResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.StopGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_gateway_with_options_async(
        self,
        request: dms_dg_20230914_models.StopGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_dg_20230914_models.StopGatewayResponse:
        """
        @summary 停止网关实例
        
        @param request: StopGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopGatewayResponse
        """
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
            version='2023-09-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_dg_20230914_models.StopGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_gateway(
        self,
        request: dms_dg_20230914_models.StopGatewayRequest,
    ) -> dms_dg_20230914_models.StopGatewayResponse:
        """
        @summary 停止网关实例
        
        @param request: StopGatewayRequest
        @return: StopGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_gateway_with_options(request, runtime)

    async def stop_gateway_async(
        self,
        request: dms_dg_20230914_models.StopGatewayRequest,
    ) -> dms_dg_20230914_models.StopGatewayResponse:
        """
        @summary 停止网关实例
        
        @param request: StopGatewayRequest
        @return: StopGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_gateway_with_options_async(request, runtime)
