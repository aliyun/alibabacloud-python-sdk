# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_clickhouse20230522 import models as clickhouse_20230522_models
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
            'ap-northeast-2-pop': 'clickhouse.aliyuncs.com',
            'ap-southeast-1': 'clickhouse.aliyuncs.com',
            'cn-beijing': 'clickhouse.aliyuncs.com',
            'cn-beijing-finance-1': 'clickhouse.aliyuncs.com',
            'cn-beijing-finance-pop': 'clickhouse.aliyuncs.com',
            'cn-beijing-gov-1': 'clickhouse.aliyuncs.com',
            'cn-beijing-nu16-b01': 'clickhouse.aliyuncs.com',
            'cn-edge-1': 'clickhouse.aliyuncs.com',
            'cn-fujian': 'clickhouse.aliyuncs.com',
            'cn-haidian-cm12-c01': 'clickhouse.aliyuncs.com',
            'cn-hangzhou': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-finance': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-test-306': 'clickhouse.aliyuncs.com',
            'cn-hongkong': 'clickhouse.aliyuncs.com',
            'cn-hongkong-finance-pop': 'clickhouse.aliyuncs.com',
            'cn-north-2-gov-1': 'clickhouse.aliyuncs.com',
            'cn-qingdao': 'clickhouse.aliyuncs.com',
            'cn-qingdao-nebula': 'clickhouse.aliyuncs.com',
            'cn-shanghai': 'clickhouse.aliyuncs.com',
            'cn-shanghai-et15-b01': 'clickhouse.aliyuncs.com',
            'cn-shanghai-et2-b01': 'clickhouse.aliyuncs.com',
            'cn-shanghai-finance-1': 'clickhouse.aliyuncs.com',
            'cn-shanghai-inner': 'clickhouse.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'clickhouse.aliyuncs.com',
            'cn-shenzhen': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-finance-1': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-inner': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'clickhouse.aliyuncs.com',
            'cn-wuhan': 'clickhouse.aliyuncs.com',
            'cn-yushanfang': 'clickhouse.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'clickhouse.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'clickhouse.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'clickhouse.aliyuncs.com',
            'eu-west-1-oxs': 'clickhouse.aliyuncs.com',
            'me-east-1': 'clickhouse.aliyuncs.com',
            'rus-west-1-pop': 'clickhouse.aliyuncs.com',
            'us-east-1': 'clickhouse.aliyuncs.com',
            'us-west-1': 'clickhouse.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('clickhouse', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_account_with_options(
        self,
        tmp_req: clickhouse_20230522_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateAccountResponse:
        """
        @summary 创建账号
        
        @param tmp_req: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.CreateAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dml_auth_setting):
            request.dml_auth_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dml_auth_setting, 'DmlAuthSetting', 'json')
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dml_auth_setting_shrink):
            query['DmlAuthSetting'] = request.dml_auth_setting_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        tmp_req: clickhouse_20230522_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateAccountResponse:
        """
        @summary 创建账号
        
        @param tmp_req: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.CreateAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dml_auth_setting):
            request.dml_auth_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dml_auth_setting, 'DmlAuthSetting', 'json')
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dml_auth_setting_shrink):
            query['DmlAuthSetting'] = request.dml_auth_setting_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: clickhouse_20230522_models.CreateAccountRequest,
    ) -> clickhouse_20230522_models.CreateAccountResponse:
        """
        @summary 创建账号
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: clickhouse_20230522_models.CreateAccountRequest,
    ) -> clickhouse_20230522_models.CreateAccountResponse:
        """
        @summary 创建账号
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_dbwith_options(
        self,
        request: clickhouse_20230522_models.CreateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateDBResponse:
        """
        @summary 创建数据库
        
        @param request: CreateDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDB',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbwith_options_async(
        self,
        request: clickhouse_20230522_models.CreateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateDBResponse:
        """
        @summary 创建数据库
        
        @param request: CreateDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDB',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_db(
        self,
        request: clickhouse_20230522_models.CreateDBRequest,
    ) -> clickhouse_20230522_models.CreateDBResponse:
        """
        @summary 创建数据库
        
        @param request: CreateDBRequest
        @return: CreateDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbwith_options(request, runtime)

    async def create_db_async(
        self,
        request: clickhouse_20230522_models.CreateDBRequest,
    ) -> clickhouse_20230522_models.CreateDBResponse:
        """
        @summary 创建数据库
        
        @param request: CreateDBRequest
        @return: CreateDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbwith_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        tmp_req: clickhouse_20230522_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateDBInstanceResponse:
        """
        @summary 创建企业版Clickhouse实例
        
        @param tmp_req: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.CreateDBInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.multi_zone):
            request.multi_zone_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.multi_zone, 'MultiZone', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.multi_zone_shrink):
            query['MultiZone'] = request.multi_zone_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        tmp_req: clickhouse_20230522_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateDBInstanceResponse:
        """
        @summary 创建企业版Clickhouse实例
        
        @param tmp_req: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.CreateDBInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.multi_zone):
            request.multi_zone_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.multi_zone, 'MultiZone', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.multi_zone_shrink):
            query['MultiZone'] = request.multi_zone_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: clickhouse_20230522_models.CreateDBInstanceRequest,
    ) -> clickhouse_20230522_models.CreateDBInstanceResponse:
        """
        @summary 创建企业版Clickhouse实例
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: clickhouse_20230522_models.CreateDBInstanceRequest,
    ) -> clickhouse_20230522_models.CreateDBInstanceResponse:
        """
        @summary 创建企业版Clickhouse实例
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_endpoint_with_options(
        self,
        request: clickhouse_20230522_models.CreateEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateEndpointResponse:
        """
        @summary 申请外网地址
        
        @param request: CreateEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_prefix):
            query['ConnectionPrefix'] = request.connection_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_endpoint_with_options_async(
        self,
        request: clickhouse_20230522_models.CreateEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateEndpointResponse:
        """
        @summary 申请外网地址
        
        @param request: CreateEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_prefix):
            query['ConnectionPrefix'] = request.connection_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_endpoint(
        self,
        request: clickhouse_20230522_models.CreateEndpointRequest,
    ) -> clickhouse_20230522_models.CreateEndpointResponse:
        """
        @summary 申请外网地址
        
        @param request: CreateEndpointRequest
        @return: CreateEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_endpoint_with_options(request, runtime)

    async def create_endpoint_async(
        self,
        request: clickhouse_20230522_models.CreateEndpointRequest,
    ) -> clickhouse_20230522_models.CreateEndpointResponse:
        """
        @summary 申请外网地址
        
        @param request: CreateEndpointRequest
        @return: CreateEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_endpoint_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: clickhouse_20230522_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteAccountResponse:
        """
        @summary 删除账号
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: clickhouse_20230522_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteAccountResponse:
        """
        @summary 删除账号
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: clickhouse_20230522_models.DeleteAccountRequest,
    ) -> clickhouse_20230522_models.DeleteAccountResponse:
        """
        @summary 删除账号
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: clickhouse_20230522_models.DeleteAccountRequest,
    ) -> clickhouse_20230522_models.DeleteAccountResponse:
        """
        @summary 删除账号
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_dbwith_options(
        self,
        request: clickhouse_20230522_models.DeleteDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteDBResponse:
        """
        @summary 删除数据库
        
        @param request: DeleteDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDB',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbwith_options_async(
        self,
        request: clickhouse_20230522_models.DeleteDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteDBResponse:
        """
        @summary 删除数据库
        
        @param request: DeleteDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDB',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_db(
        self,
        request: clickhouse_20230522_models.DeleteDBRequest,
    ) -> clickhouse_20230522_models.DeleteDBResponse:
        """
        @summary 删除数据库
        
        @param request: DeleteDBRequest
        @return: DeleteDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbwith_options(request, runtime)

    async def delete_db_async(
        self,
        request: clickhouse_20230522_models.DeleteDBRequest,
    ) -> clickhouse_20230522_models.DeleteDBResponse:
        """
        @summary 删除数据库
        
        @param request: DeleteDBRequest
        @return: DeleteDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbwith_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: clickhouse_20230522_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteDBInstanceResponse:
        """
        @summary 释放实例
        
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: clickhouse_20230522_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteDBInstanceResponse:
        """
        @summary 释放实例
        
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance(
        self,
        request: clickhouse_20230522_models.DeleteDBInstanceRequest,
    ) -> clickhouse_20230522_models.DeleteDBInstanceResponse:
        """
        @summary 释放实例
        
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: clickhouse_20230522_models.DeleteDBInstanceRequest,
    ) -> clickhouse_20230522_models.DeleteDBInstanceResponse:
        """
        @summary 释放实例
        
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_endpoint_with_options(
        self,
        request: clickhouse_20230522_models.DeleteEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteEndpointResponse:
        """
        @summary 删除链接地址
        
        @param request: DeleteEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEndpoint',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_endpoint_with_options_async(
        self,
        request: clickhouse_20230522_models.DeleteEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteEndpointResponse:
        """
        @summary 删除链接地址
        
        @param request: DeleteEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEndpoint',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_endpoint(
        self,
        request: clickhouse_20230522_models.DeleteEndpointRequest,
    ) -> clickhouse_20230522_models.DeleteEndpointResponse:
        """
        @summary 删除链接地址
        
        @param request: DeleteEndpointRequest
        @return: DeleteEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_endpoint_with_options(request, runtime)

    async def delete_endpoint_async(
        self,
        request: clickhouse_20230522_models.DeleteEndpointRequest,
    ) -> clickhouse_20230522_models.DeleteEndpointResponse:
        """
        @summary 删除链接地址
        
        @param request: DeleteEndpointRequest
        @return: DeleteEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_endpoint_with_options_async(request, runtime)

    def describe_account_authority_with_options(
        self,
        request: clickhouse_20230522_models.DescribeAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeAccountAuthorityResponse:
        """
        @summary 查询账号的授权信息
        
        @param request: DescribeAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountAuthorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAuthority',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_authority_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeAccountAuthorityResponse:
        """
        @summary 查询账号的授权信息
        
        @param request: DescribeAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountAuthorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAuthority',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeAccountAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_authority(
        self,
        request: clickhouse_20230522_models.DescribeAccountAuthorityRequest,
    ) -> clickhouse_20230522_models.DescribeAccountAuthorityResponse:
        """
        @summary 查询账号的授权信息
        
        @param request: DescribeAccountAuthorityRequest
        @return: DescribeAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_authority_with_options(request, runtime)

    async def describe_account_authority_async(
        self,
        request: clickhouse_20230522_models.DescribeAccountAuthorityRequest,
    ) -> clickhouse_20230522_models.DescribeAccountAuthorityResponse:
        """
        @summary 查询账号的授权信息
        
        @param request: DescribeAccountAuthorityRequest
        @return: DescribeAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_authority_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: clickhouse_20230522_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeAccountsResponse:
        """
        @summary 查询账号列表
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeAccountsResponse:
        """
        @summary 查询账号列表
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: clickhouse_20230522_models.DescribeAccountsRequest,
    ) -> clickhouse_20230522_models.DescribeAccountsResponse:
        """
        @summary 查询账号列表
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: clickhouse_20230522_models.DescribeAccountsRequest,
    ) -> clickhouse_20230522_models.DescribeAccountsResponse:
        """
        @summary 查询账号列表
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary 查询实例详情
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary 查询实例详情
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceAttributeRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary 查询实例详情
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceAttributeRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary 查询实例详情
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_data_sources_with_options(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse:
        """
        @summary 查询DB或者Table数据结构
        
        @param request: DescribeDBInstanceDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDataSources',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_data_sources_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse:
        """
        @summary 查询DB或者Table数据结构
        
        @param request: DescribeDBInstanceDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDataSources',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_data_sources(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceDataSourcesRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse:
        """
        @summary 查询DB或者Table数据结构
        
        @param request: DescribeDBInstanceDataSourcesRequest
        @return: DescribeDBInstanceDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_data_sources_with_options(request, runtime)

    async def describe_dbinstance_data_sources_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceDataSourcesRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse:
        """
        @summary 查询DB或者Table数据结构
        
        @param request: DescribeDBInstanceDataSourcesRequest
        @return: DescribeDBInstanceDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_data_sources_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: clickhouse_20230522_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstancesResponse:
        """
        @summary 查询实例列表
        
        @param request: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstancesResponse:
        """
        @summary 查询实例列表
        
        @param request: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances(
        self,
        request: clickhouse_20230522_models.DescribeDBInstancesRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstancesResponse:
        """
        @summary 查询实例列表
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstancesRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstancesResponse:
        """
        @summary 查询实例列表
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_endpoints_with_options(
        self,
        request: clickhouse_20230522_models.DescribeEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeEndpointsResponse:
        """
        @summary 查询实例访问地址
        
        @param request: DescribeEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpoints',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_endpoints_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeEndpointsResponse:
        """
        @summary 查询实例访问地址
        
        @param request: DescribeEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpoints',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_endpoints(
        self,
        request: clickhouse_20230522_models.DescribeEndpointsRequest,
    ) -> clickhouse_20230522_models.DescribeEndpointsResponse:
        """
        @summary 查询实例访问地址
        
        @param request: DescribeEndpointsRequest
        @return: DescribeEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoints_with_options(request, runtime)

    async def describe_endpoints_async(
        self,
        request: clickhouse_20230522_models.DescribeEndpointsRequest,
    ) -> clickhouse_20230522_models.DescribeEndpointsResponse:
        """
        @summary 查询实例访问地址
        
        @param request: DescribeEndpointsRequest
        @return: DescribeEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_endpoints_with_options_async(request, runtime)

    def describe_process_list_with_options(
        self,
        request: clickhouse_20230522_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeProcessListResponse:
        """
        @summary 查看正在运行的查询
        
        @param request: DescribeProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.initial_user):
            query['InitialUser'] = request.initial_user
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.query_order):
            query['QueryOrder'] = request.query_order
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_list_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeProcessListResponse:
        """
        @summary 查看正在运行的查询
        
        @param request: DescribeProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.initial_user):
            query['InitialUser'] = request.initial_user
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.query_order):
            query['QueryOrder'] = request.query_order
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeProcessListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_list(
        self,
        request: clickhouse_20230522_models.DescribeProcessListRequest,
    ) -> clickhouse_20230522_models.DescribeProcessListResponse:
        """
        @summary 查看正在运行的查询
        
        @param request: DescribeProcessListRequest
        @return: DescribeProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    async def describe_process_list_async(
        self,
        request: clickhouse_20230522_models.DescribeProcessListRequest,
    ) -> clickhouse_20230522_models.DescribeProcessListResponse:
        """
        @summary 查看正在运行的查询
        
        @param request: DescribeProcessListRequest
        @return: DescribeProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_list_with_options_async(request, runtime)

    def describe_security_iplist_with_options(
        self,
        request: clickhouse_20230522_models.DescribeSecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary 查询白名单
        
        @param request: DescribeSecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSecurityIPListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_iplist_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeSecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary 查询白名单
        
        @param request: DescribeSecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSecurityIPListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_iplist(
        self,
        request: clickhouse_20230522_models.DescribeSecurityIPListRequest,
    ) -> clickhouse_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary 查询白名单
        
        @param request: DescribeSecurityIPListRequest
        @return: DescribeSecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_iplist_with_options(request, runtime)

    async def describe_security_iplist_async(
        self,
        request: clickhouse_20230522_models.DescribeSecurityIPListRequest,
    ) -> clickhouse_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary 查询白名单
        
        @param request: DescribeSecurityIPListRequest
        @return: DescribeSecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_iplist_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSlowLogRecordsResponse:
        """
        @summary 查看慢日志明细
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSlowLogRecordsResponse:
        """
        @summary 查看慢日志明细
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogRecordsRequest,
    ) -> clickhouse_20230522_models.DescribeSlowLogRecordsResponse:
        """
        @summary 查看慢日志明细
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogRecordsRequest,
    ) -> clickhouse_20230522_models.DescribeSlowLogRecordsResponse:
        """
        @summary 查看慢日志明细
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_slow_log_trend_with_options(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSlowLogTrendResponse:
        """
        @summary 慢查询趋势
        
        @param request: DescribeSlowLogTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogTrend',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSlowLogTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_trend_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSlowLogTrendResponse:
        """
        @summary 慢查询趋势
        
        @param request: DescribeSlowLogTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogTrend',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSlowLogTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_trend(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogTrendRequest,
    ) -> clickhouse_20230522_models.DescribeSlowLogTrendResponse:
        """
        @summary 慢查询趋势
        
        @param request: DescribeSlowLogTrendRequest
        @return: DescribeSlowLogTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_trend_with_options(request, runtime)

    async def describe_slow_log_trend_async(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogTrendRequest,
    ) -> clickhouse_20230522_models.DescribeSlowLogTrendResponse:
        """
        @summary 慢查询趋势
        
        @param request: DescribeSlowLogTrendRequest
        @return: DescribeSlowLogTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_trend_with_options_async(request, runtime)

    def kill_process_with_options(
        self,
        request: clickhouse_20230522_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.KillProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_process_with_options_async(
        self,
        request: clickhouse_20230522_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.KillProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_process(
        self,
        request: clickhouse_20230522_models.KillProcessRequest,
    ) -> clickhouse_20230522_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @return: KillProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    async def kill_process_async(
        self,
        request: clickhouse_20230522_models.KillProcessRequest,
    ) -> clickhouse_20230522_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @return: KillProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_process_with_options_async(request, runtime)

    def modify_account_authority_with_options(
        self,
        tmp_req: clickhouse_20230522_models.ModifyAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyAccountAuthorityResponse:
        """
        @summary 修改账号的授权信息
        
        @param tmp_req: ModifyAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountAuthorityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.ModifyAccountAuthorityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dml_auth_setting):
            request.dml_auth_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dml_auth_setting, 'DmlAuthSetting', 'json')
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dml_auth_setting_shrink):
            query['DmlAuthSetting'] = request.dml_auth_setting_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountAuthority',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_authority_with_options_async(
        self,
        tmp_req: clickhouse_20230522_models.ModifyAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyAccountAuthorityResponse:
        """
        @summary 修改账号的授权信息
        
        @param tmp_req: ModifyAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountAuthorityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.ModifyAccountAuthorityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dml_auth_setting):
            request.dml_auth_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dml_auth_setting, 'DmlAuthSetting', 'json')
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dml_auth_setting_shrink):
            query['DmlAuthSetting'] = request.dml_auth_setting_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountAuthority',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyAccountAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_authority(
        self,
        request: clickhouse_20230522_models.ModifyAccountAuthorityRequest,
    ) -> clickhouse_20230522_models.ModifyAccountAuthorityResponse:
        """
        @summary 修改账号的授权信息
        
        @param request: ModifyAccountAuthorityRequest
        @return: ModifyAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_authority_with_options(request, runtime)

    async def modify_account_authority_async(
        self,
        request: clickhouse_20230522_models.ModifyAccountAuthorityRequest,
    ) -> clickhouse_20230522_models.ModifyAccountAuthorityResponse:
        """
        @summary 修改账号的授权信息
        
        @param request: ModifyAccountAuthorityRequest
        @return: ModifyAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_authority_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: clickhouse_20230522_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyAccountDescriptionResponse:
        """
        @summary 修改账号备注
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyAccountDescriptionResponse:
        """
        @summary 修改账号备注
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: clickhouse_20230522_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20230522_models.ModifyAccountDescriptionResponse:
        """
        @summary 修改账号备注
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: clickhouse_20230522_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20230522_models.ModifyAccountDescriptionResponse:
        """
        @summary 修改账号备注
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_dbinstance_attribute_with_options(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary 修改实例的配置属性，包括名称、运维时间等
        
        @param request: ModifyDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_type):
            query['AttributeType'] = request.attribute_type
        if not UtilClient.is_unset(request.attribute_value):
            query['AttributeValue'] = request.attribute_value
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_attribute_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary 修改实例的配置属性，包括名称、运维时间等
        
        @param request: ModifyDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_type):
            query['AttributeType'] = request.attribute_type
        if not UtilClient.is_unset(request.attribute_value):
            query['AttributeValue'] = request.attribute_value
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_attribute(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceAttributeRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary 修改实例的配置属性，包括名称、运维时间等
        
        @param request: ModifyDBInstanceAttributeRequest
        @return: ModifyDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_attribute_with_options(request, runtime)

    async def modify_dbinstance_attribute_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceAttributeRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary 修改实例的配置属性，包括名称、运维时间等
        
        @param request: ModifyDBInstanceAttributeRequest
        @return: ModifyDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_attribute_with_options_async(request, runtime)

    def modify_dbinstance_class_with_options(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceClassResponse:
        """
        @summary 修改实例弹性配置
        
        @param request: ModifyDBInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceClass',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_class_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceClassResponse:
        """
        @summary 修改实例弹性配置
        
        @param request: ModifyDBInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceClass',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_class(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceClassRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceClassResponse:
        """
        @summary 修改实例弹性配置
        
        @param request: ModifyDBInstanceClassRequest
        @return: ModifyDBInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_class_with_options(request, runtime)

    async def modify_dbinstance_class_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceClassRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceClassResponse:
        """
        @summary 修改实例弹性配置
        
        @param request: ModifyDBInstanceClassRequest
        @return: ModifyDBInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_class_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.disable_ports):
            query['DisablePorts'] = request.disable_ports
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.disable_ports):
            query['DisablePorts'] = request.disable_ports
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConnectionStringRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConnectionStringRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_security_iplist_with_options(
        self,
        request: clickhouse_20230522_models.ModifySecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifySecurityIPListResponse:
        """
        @summary 变更白名单
        
        @param request: ModifySecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifySecurityIPListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_iplist_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifySecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifySecurityIPListResponse:
        """
        @summary 变更白名单
        
        @param request: ModifySecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifySecurityIPListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_iplist(
        self,
        request: clickhouse_20230522_models.ModifySecurityIPListRequest,
    ) -> clickhouse_20230522_models.ModifySecurityIPListResponse:
        """
        @summary 变更白名单
        
        @param request: ModifySecurityIPListRequest
        @return: ModifySecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_iplist_with_options(request, runtime)

    async def modify_security_iplist_async(
        self,
        request: clickhouse_20230522_models.ModifySecurityIPListRequest,
    ) -> clickhouse_20230522_models.ModifySecurityIPListResponse:
        """
        @summary 变更白名单
        
        @param request: ModifySecurityIPListRequest
        @return: ModifySecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_iplist_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: clickhouse_20230522_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ResetAccountPasswordResponse:
        """
        @summary 重置账号密码
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: clickhouse_20230522_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ResetAccountPasswordResponse:
        """
        @summary 重置账号密码
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: clickhouse_20230522_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20230522_models.ResetAccountPasswordResponse:
        """
        @summary 重置账号密码
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: clickhouse_20230522_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20230522_models.ResetAccountPasswordResponse:
        """
        @summary 重置账号密码
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: clickhouse_20230522_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.RestartDBInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: clickhouse_20230522_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.RestartDBInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.RestartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbinstance(
        self,
        request: clickhouse_20230522_models.RestartDBInstanceRequest,
    ) -> clickhouse_20230522_models.RestartDBInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartDBInstanceRequest
        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: clickhouse_20230522_models.RestartDBInstanceRequest,
    ) -> clickhouse_20230522_models.RestartDBInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartDBInstanceRequest
        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def start_dbinstance_with_options(
        self,
        request: clickhouse_20230522_models.StartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.StartDBInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.StartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dbinstance_with_options_async(
        self,
        request: clickhouse_20230522_models.StartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.StartDBInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.StartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dbinstance(
        self,
        request: clickhouse_20230522_models.StartDBInstanceRequest,
    ) -> clickhouse_20230522_models.StartDBInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartDBInstanceRequest
        @return: StartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_dbinstance_with_options(request, runtime)

    async def start_dbinstance_async(
        self,
        request: clickhouse_20230522_models.StartDBInstanceRequest,
    ) -> clickhouse_20230522_models.StartDBInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartDBInstanceRequest
        @return: StartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_dbinstance_with_options_async(request, runtime)

    def stop_dbinstance_with_options(
        self,
        request: clickhouse_20230522_models.StopDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.StopDBInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.StopDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dbinstance_with_options_async(
        self,
        request: clickhouse_20230522_models.StopDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.StopDBInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.StopDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dbinstance(
        self,
        request: clickhouse_20230522_models.StopDBInstanceRequest,
    ) -> clickhouse_20230522_models.StopDBInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopDBInstanceRequest
        @return: StopDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_dbinstance_with_options(request, runtime)

    async def stop_dbinstance_async(
        self,
        request: clickhouse_20230522_models.StopDBInstanceRequest,
    ) -> clickhouse_20230522_models.StopDBInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopDBInstanceRequest
        @return: StopDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_dbinstance_with_options_async(request, runtime)

    def upgrade_minor_version_with_options(
        self,
        request: clickhouse_20230522_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.UpgradeMinorVersionResponse:
        """
        @summary 升级实例内核小版本
        
        @param request: UpgradeMinorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_minor_version):
            query['TargetMinorVersion'] = request.target_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMinorVersion',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.UpgradeMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_minor_version_with_options_async(
        self,
        request: clickhouse_20230522_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.UpgradeMinorVersionResponse:
        """
        @summary 升级实例内核小版本
        
        @param request: UpgradeMinorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_minor_version):
            query['TargetMinorVersion'] = request.target_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMinorVersion',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.UpgradeMinorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_minor_version(
        self,
        request: clickhouse_20230522_models.UpgradeMinorVersionRequest,
    ) -> clickhouse_20230522_models.UpgradeMinorVersionResponse:
        """
        @summary 升级实例内核小版本
        
        @param request: UpgradeMinorVersionRequest
        @return: UpgradeMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_minor_version_with_options(request, runtime)

    async def upgrade_minor_version_async(
        self,
        request: clickhouse_20230522_models.UpgradeMinorVersionRequest,
    ) -> clickhouse_20230522_models.UpgradeMinorVersionResponse:
        """
        @summary 升级实例内核小版本
        
        @param request: UpgradeMinorVersionRequest
        @return: UpgradeMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_minor_version_with_options_async(request, runtime)
