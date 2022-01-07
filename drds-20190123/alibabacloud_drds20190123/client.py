# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_drds20190123 import models as drds_20190123_models
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
            'ap-northeast-1': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2-pop': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'drds.ap-southeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'drds.aliyuncs.com',
            'cn-beijing-finance-pop': 'drds.aliyuncs.com',
            'cn-beijing-gov-1': 'drds.aliyuncs.com',
            'cn-beijing-nu16-b01': 'drds.aliyuncs.com',
            'cn-chengdu': 'drds.aliyuncs.com',
            'cn-edge-1': 'drds.aliyuncs.com',
            'cn-fujian': 'drds.aliyuncs.com',
            'cn-haidian-cm12-c01': 'drds.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'drds.aliyuncs.com',
            'cn-hangzhou-finance': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'drds.aliyuncs.com',
            'cn-hangzhou-test-306': 'drds.aliyuncs.com',
            'cn-hongkong-finance-pop': 'drds.aliyuncs.com',
            'cn-qingdao-nebula': 'drds.aliyuncs.com',
            'cn-shanghai-et15-b01': 'drds.aliyuncs.com',
            'cn-shanghai-et2-b01': 'drds.aliyuncs.com',
            'cn-shanghai-inner': 'drds.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'drds.aliyuncs.com',
            'cn-shenzhen-inner': 'drds.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'drds.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'drds.aliyuncs.com',
            'cn-wuhan': 'drds.aliyuncs.com',
            'cn-yushanfang': 'drds.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'drds.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'drds.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'drds.aliyuncs.com',
            'eu-central-1': 'drds.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'drds.ap-southeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'drds.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'drds.ap-southeast-1.aliyuncs.com',
            'rus-west-1-pop': 'drds.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'drds.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('drds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_account_password_with_options(
        self,
        request: drds_20190123_models.ChangeAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ChangeAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeAccountPassword',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_account_password_with_options_async(
        self,
        request: drds_20190123_models.ChangeAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ChangeAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeAccountPassword',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_account_password(
        self,
        request: drds_20190123_models.ChangeAccountPasswordRequest,
    ) -> drds_20190123_models.ChangeAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_account_password_with_options(request, runtime)

    async def change_account_password_async(
        self,
        request: drds_20190123_models.ChangeAccountPasswordRequest,
    ) -> drds_20190123_models.ChangeAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_account_password_with_options_async(request, runtime)

    def change_instance_azone_with_options(
        self,
        request: drds_20190123_models.ChangeInstanceAzoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ChangeInstanceAzoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.drds_region_id):
            query['DrdsRegionId'] = request.drds_region_id
        if not UtilClient.is_unset(request.origin_azone_id):
            query['OriginAzoneId'] = request.origin_azone_id
        if not UtilClient.is_unset(request.target_azone_id):
            query['TargetAzoneId'] = request.target_azone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeInstanceAzone',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeInstanceAzoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_instance_azone_with_options_async(
        self,
        request: drds_20190123_models.ChangeInstanceAzoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ChangeInstanceAzoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.drds_region_id):
            query['DrdsRegionId'] = request.drds_region_id
        if not UtilClient.is_unset(request.origin_azone_id):
            query['OriginAzoneId'] = request.origin_azone_id
        if not UtilClient.is_unset(request.target_azone_id):
            query['TargetAzoneId'] = request.target_azone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeInstanceAzone',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeInstanceAzoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_instance_azone(
        self,
        request: drds_20190123_models.ChangeInstanceAzoneRequest,
    ) -> drds_20190123_models.ChangeInstanceAzoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_instance_azone_with_options(request, runtime)

    async def change_instance_azone_async(
        self,
        request: drds_20190123_models.ChangeInstanceAzoneRequest,
    ) -> drds_20190123_models.ChangeInstanceAzoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_instance_azone_with_options_async(request, runtime)

    def check_drds_db_name_with_options(
        self,
        request: drds_20190123_models.CheckDrdsDbNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckDrdsDbNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDrdsDbName',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckDrdsDbNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_drds_db_name_with_options_async(
        self,
        request: drds_20190123_models.CheckDrdsDbNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckDrdsDbNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDrdsDbName',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckDrdsDbNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_drds_db_name(
        self,
        request: drds_20190123_models.CheckDrdsDbNameRequest,
    ) -> drds_20190123_models.CheckDrdsDbNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_drds_db_name_with_options(request, runtime)

    async def check_drds_db_name_async(
        self,
        request: drds_20190123_models.CheckDrdsDbNameRequest,
    ) -> drds_20190123_models.CheckDrdsDbNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_drds_db_name_with_options_async(request, runtime)

    def check_expand_status_with_options(
        self,
        request: drds_20190123_models.CheckExpandStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckExpandStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckExpandStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckExpandStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_expand_status_with_options_async(
        self,
        request: drds_20190123_models.CheckExpandStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckExpandStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckExpandStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckExpandStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_expand_status(
        self,
        request: drds_20190123_models.CheckExpandStatusRequest,
    ) -> drds_20190123_models.CheckExpandStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_expand_status_with_options(request, runtime)

    async def check_expand_status_async(
        self,
        request: drds_20190123_models.CheckExpandStatusRequest,
    ) -> drds_20190123_models.CheckExpandStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_expand_status_with_options_async(request, runtime)

    def check_sql_audit_enable_status_with_options(
        self,
        request: drds_20190123_models.CheckSqlAuditEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckSqlAuditEnableStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSqlAuditEnableStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckSqlAuditEnableStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_sql_audit_enable_status_with_options_async(
        self,
        request: drds_20190123_models.CheckSqlAuditEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckSqlAuditEnableStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSqlAuditEnableStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckSqlAuditEnableStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_sql_audit_enable_status(
        self,
        request: drds_20190123_models.CheckSqlAuditEnableStatusRequest,
    ) -> drds_20190123_models.CheckSqlAuditEnableStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_sql_audit_enable_status_with_options(request, runtime)

    async def check_sql_audit_enable_status_async(
        self,
        request: drds_20190123_models.CheckSqlAuditEnableStatusRequest,
    ) -> drds_20190123_models.CheckSqlAuditEnableStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_sql_audit_enable_status_with_options_async(request, runtime)

    def create_drds_dbwith_options(
        self,
        request: drds_20190123_models.CreateDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.db_instance_is_creating):
            query['DbInstanceIsCreating'] = request.db_instance_is_creating
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.encode):
            query['Encode'] = request.encode
        if not UtilClient.is_unset(request.inst_db_name):
            query['InstDbName'] = request.inst_db_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.rds_instance):
            query['RdsInstance'] = request.rds_instance
        if not UtilClient.is_unset(request.rds_super_account):
            query['RdsSuperAccount'] = request.rds_super_account
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDrdsDB',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_drds_dbwith_options_async(
        self,
        request: drds_20190123_models.CreateDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.db_instance_is_creating):
            query['DbInstanceIsCreating'] = request.db_instance_is_creating
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.encode):
            query['Encode'] = request.encode
        if not UtilClient.is_unset(request.inst_db_name):
            query['InstDbName'] = request.inst_db_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.rds_instance):
            query['RdsInstance'] = request.rds_instance
        if not UtilClient.is_unset(request.rds_super_account):
            query['RdsSuperAccount'] = request.rds_super_account
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDrdsDB',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_drds_db(
        self,
        request: drds_20190123_models.CreateDrdsDBRequest,
    ) -> drds_20190123_models.CreateDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbwith_options(request, runtime)

    async def create_drds_db_async(
        self,
        request: drds_20190123_models.CreateDrdsDBRequest,
    ) -> drds_20190123_models.CreateDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_drds_dbwith_options_async(request, runtime)

    def create_drds_instance_with_options(
        self,
        request: drds_20190123_models.CreateDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_series):
            query['InstanceSeries'] = request.instance_series
        if not UtilClient.is_unset(request.is_auto_renew):
            query['IsAutoRenew'] = request.is_auto_renew
        if not UtilClient.is_unset(request.master_inst_id):
            query['MasterInstId'] = request.master_inst_id
        if not UtilClient.is_unset(request.my_sqlversion):
            query['MySQLVersion'] = request.my_sqlversion
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.is_ha):
            query['isHa'] = request.is_ha
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_drds_instance_with_options_async(
        self,
        request: drds_20190123_models.CreateDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_series):
            query['InstanceSeries'] = request.instance_series
        if not UtilClient.is_unset(request.is_auto_renew):
            query['IsAutoRenew'] = request.is_auto_renew
        if not UtilClient.is_unset(request.master_inst_id):
            query['MasterInstId'] = request.master_inst_id
        if not UtilClient.is_unset(request.my_sqlversion):
            query['MySQLVersion'] = request.my_sqlversion
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.is_ha):
            query['isHa'] = request.is_ha
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_drds_instance(
        self,
        request: drds_20190123_models.CreateDrdsInstanceRequest,
    ) -> drds_20190123_models.CreateDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_drds_instance_with_options(request, runtime)

    async def create_drds_instance_async(
        self,
        request: drds_20190123_models.CreateDrdsInstanceRequest,
    ) -> drds_20190123_models.CreateDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_drds_instance_with_options_async(request, runtime)

    def create_instance_account_with_options(
        self,
        request: drds_20190123_models.CreateInstanceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateInstanceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.db_privilege):
            query['DbPrivilege'] = request.db_privilege
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceAccount',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_account_with_options_async(
        self,
        request: drds_20190123_models.CreateInstanceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateInstanceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.db_privilege):
            query['DbPrivilege'] = request.db_privilege
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceAccount',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_account(
        self,
        request: drds_20190123_models.CreateInstanceAccountRequest,
    ) -> drds_20190123_models.CreateInstanceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_account_with_options(request, runtime)

    async def create_instance_account_async(
        self,
        request: drds_20190123_models.CreateInstanceAccountRequest,
    ) -> drds_20190123_models.CreateInstanceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_account_with_options_async(request, runtime)

    def create_instance_internet_address_with_options(
        self,
        request: drds_20190123_models.CreateInstanceInternetAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateInstanceInternetAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceInternetAddress',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceInternetAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_internet_address_with_options_async(
        self,
        request: drds_20190123_models.CreateInstanceInternetAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateInstanceInternetAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceInternetAddress',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceInternetAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_internet_address(
        self,
        request: drds_20190123_models.CreateInstanceInternetAddressRequest,
    ) -> drds_20190123_models.CreateInstanceInternetAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_internet_address_with_options(request, runtime)

    async def create_instance_internet_address_async(
        self,
        request: drds_20190123_models.CreateInstanceInternetAddressRequest,
    ) -> drds_20190123_models.CreateInstanceInternetAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_internet_address_with_options_async(request, runtime)

    def create_order_for_rds_with_options(
        self,
        request: drds_20190123_models.CreateOrderForRdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateOrderForRdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrderForRds',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateOrderForRdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_for_rds_with_options_async(
        self,
        request: drds_20190123_models.CreateOrderForRdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateOrderForRdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrderForRds',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateOrderForRdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order_for_rds(
        self,
        request: drds_20190123_models.CreateOrderForRdsRequest,
    ) -> drds_20190123_models.CreateOrderForRdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_for_rds_with_options(request, runtime)

    async def create_order_for_rds_async(
        self,
        request: drds_20190123_models.CreateOrderForRdsRequest,
    ) -> drds_20190123_models.CreateOrderForRdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_for_rds_with_options_async(request, runtime)

    def create_shard_task_with_options(
        self,
        request: drds_20190123_models.CreateShardTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateShardTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_table_name):
            query['SourceTableName'] = request.source_table_name
        if not UtilClient.is_unset(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateShardTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateShardTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_shard_task_with_options_async(
        self,
        request: drds_20190123_models.CreateShardTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateShardTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_table_name):
            query['SourceTableName'] = request.source_table_name
        if not UtilClient.is_unset(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateShardTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateShardTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_shard_task(
        self,
        request: drds_20190123_models.CreateShardTaskRequest,
    ) -> drds_20190123_models.CreateShardTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_shard_task_with_options(request, runtime)

    async def create_shard_task_async(
        self,
        request: drds_20190123_models.CreateShardTaskRequest,
    ) -> drds_20190123_models.CreateShardTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_shard_task_with_options_async(request, runtime)

    def describe_back_menu_with_options(
        self,
        request: drds_20190123_models.DescribeBackMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackMenuResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackMenu',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackMenuResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_back_menu_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackMenuResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackMenu',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackMenuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_back_menu(
        self,
        request: drds_20190123_models.DescribeBackMenuRequest,
    ) -> drds_20190123_models.DescribeBackMenuResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_back_menu_with_options(request, runtime)

    async def describe_back_menu_async(
        self,
        request: drds_20190123_models.DescribeBackMenuRequest,
    ) -> drds_20190123_models.DescribeBackMenuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_back_menu_with_options_async(request, runtime)

    def describe_backup_dbs_with_options(
        self,
        request: drds_20190123_models.DescribeBackupDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupDbsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.preferred_restore_time):
            query['PreferredRestoreTime'] = request.preferred_restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupDbs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_dbs_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackupDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupDbsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.preferred_restore_time):
            query['PreferredRestoreTime'] = request.preferred_restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupDbs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_dbs(
        self,
        request: drds_20190123_models.DescribeBackupDbsRequest,
    ) -> drds_20190123_models.DescribeBackupDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_dbs_with_options(request, runtime)

    async def describe_backup_dbs_async(
        self,
        request: drds_20190123_models.DescribeBackupDbsRequest,
    ) -> drds_20190123_models.DescribeBackupDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_dbs_with_options_async(request, runtime)

    def describe_backup_local_with_options(
        self,
        request: drds_20190123_models.DescribeBackupLocalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupLocalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupLocal',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupLocalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_local_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackupLocalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupLocalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupLocal',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupLocalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_local(
        self,
        request: drds_20190123_models.DescribeBackupLocalRequest,
    ) -> drds_20190123_models.DescribeBackupLocalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_local_with_options(request, runtime)

    async def describe_backup_local_async(
        self,
        request: drds_20190123_models.DescribeBackupLocalRequest,
    ) -> drds_20190123_models.DescribeBackupLocalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_local_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: drds_20190123_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: drds_20190123_models.DescribeBackupPolicyRequest,
    ) -> drds_20190123_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: drds_20190123_models.DescribeBackupPolicyRequest,
    ) -> drds_20190123_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backup_sets_with_options(
        self,
        request: drds_20190123_models.DescribeBackupSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSets',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_sets_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackupSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSets',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_sets(
        self,
        request: drds_20190123_models.DescribeBackupSetsRequest,
    ) -> drds_20190123_models.DescribeBackupSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_sets_with_options(request, runtime)

    async def describe_backup_sets_async(
        self,
        request: drds_20190123_models.DescribeBackupSetsRequest,
    ) -> drds_20190123_models.DescribeBackupSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_sets_with_options_async(request, runtime)

    def describe_backup_times_with_options(
        self,
        request: drds_20190123_models.DescribeBackupTimesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupTimesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupTimes',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupTimesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_times_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackupTimesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupTimesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupTimes',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupTimesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_times(
        self,
        request: drds_20190123_models.DescribeBackupTimesRequest,
    ) -> drds_20190123_models.DescribeBackupTimesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_times_with_options(request, runtime)

    async def describe_backup_times_async(
        self,
        request: drds_20190123_models.DescribeBackupTimesRequest,
    ) -> drds_20190123_models.DescribeBackupTimesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_times_with_options_async(request, runtime)

    def describe_broadcast_tables_with_options(
        self,
        request: drds_20190123_models.DescribeBroadcastTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBroadcastTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBroadcastTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBroadcastTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_broadcast_tables_with_options_async(
        self,
        request: drds_20190123_models.DescribeBroadcastTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBroadcastTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBroadcastTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBroadcastTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_broadcast_tables(
        self,
        request: drds_20190123_models.DescribeBroadcastTablesRequest,
    ) -> drds_20190123_models.DescribeBroadcastTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_broadcast_tables_with_options(request, runtime)

    async def describe_broadcast_tables_async(
        self,
        request: drds_20190123_models.DescribeBroadcastTablesRequest,
    ) -> drds_20190123_models.DescribeBroadcastTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_broadcast_tables_with_options_async(request, runtime)

    def describe_db_instance_dbs_with_options(
        self,
        request: drds_20190123_models.DescribeDbInstanceDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDbInstanceDbsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbInstanceDbs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstanceDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_db_instance_dbs_with_options_async(
        self,
        request: drds_20190123_models.DescribeDbInstanceDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDbInstanceDbsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbInstanceDbs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstanceDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_db_instance_dbs(
        self,
        request: drds_20190123_models.DescribeDbInstanceDbsRequest,
    ) -> drds_20190123_models.DescribeDbInstanceDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_db_instance_dbs_with_options(request, runtime)

    async def describe_db_instance_dbs_async(
        self,
        request: drds_20190123_models.DescribeDbInstanceDbsRequest,
    ) -> drds_20190123_models.DescribeDbInstanceDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_db_instance_dbs_with_options_async(request, runtime)

    def describe_db_instances_with_options(
        self,
        request: drds_20190123_models.DescribeDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDbInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_db_instances_with_options_async(
        self,
        request: drds_20190123_models.DescribeDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDbInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_db_instances(
        self,
        request: drds_20190123_models.DescribeDbInstancesRequest,
    ) -> drds_20190123_models.DescribeDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_db_instances_with_options(request, runtime)

    async def describe_db_instances_async(
        self,
        request: drds_20190123_models.DescribeDbInstancesRequest,
    ) -> drds_20190123_models.DescribeDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_db_instances_with_options_async(request, runtime)

    def describe_drds_dbwith_options(
        self,
        request: drds_20190123_models.DescribeDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDB',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_dbwith_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDB',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_db(
        self,
        request: drds_20190123_models.DescribeDrdsDBRequest,
    ) -> drds_20190123_models.DescribeDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbwith_options(request, runtime)

    async def describe_drds_db_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBRequest,
    ) -> drds_20190123_models.DescribeDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbwith_options_async(request, runtime)

    def describe_drds_dbcluster_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBCluster',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_dbcluster_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBCluster',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_dbcluster(
        self,
        request: drds_20190123_models.DescribeDrdsDBClusterRequest,
    ) -> drds_20190123_models.DescribeDrdsDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbcluster_with_options(request, runtime)

    async def describe_drds_dbcluster_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBClusterRequest,
    ) -> drds_20190123_models.DescribeDrdsDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbcluster_with_options_async(request, runtime)

    def describe_drds_dbip_white_list_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDBIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBIpWhiteList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_dbip_white_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBIpWhiteList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_dbip_white_list(
        self,
        request: drds_20190123_models.DescribeDrdsDBIpWhiteListRequest,
    ) -> drds_20190123_models.DescribeDrdsDBIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbip_white_list_with_options(request, runtime)

    async def describe_drds_dbip_white_list_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBIpWhiteListRequest,
    ) -> drds_20190123_models.DescribeDrdsDBIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbip_white_list_with_options_async(request, runtime)

    def describe_drds_dbs_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_dbs_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_dbs(
        self,
        request: drds_20190123_models.DescribeDrdsDBsRequest,
    ) -> drds_20190123_models.DescribeDrdsDBsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbs_with_options(request, runtime)

    async def describe_drds_dbs_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBsRequest,
    ) -> drds_20190123_models.DescribeDrdsDBsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbs_with_options_async(request, runtime)

    def describe_drds_db_instance_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_db_instance_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_db_instance(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstanceRequest,
    ) -> drds_20190123_models.DescribeDrdsDbInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_instance_with_options(request, runtime)

    async def describe_drds_db_instance_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstanceRequest,
    ) -> drds_20190123_models.DescribeDrdsDbInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_db_instance_with_options_async(request, runtime)

    def describe_drds_db_instances_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_db_instances_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_db_instances(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_instances_with_options(request, runtime)

    async def describe_drds_db_instances_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_db_instances_with_options_async(request, runtime)

    def describe_drds_db_rds_name_list_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDbRdsNameListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbRdsNameListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbRdsNameList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbRdsNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_db_rds_name_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbRdsNameListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbRdsNameListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbRdsNameList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbRdsNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_db_rds_name_list(
        self,
        request: drds_20190123_models.DescribeDrdsDbRdsNameListRequest,
    ) -> drds_20190123_models.DescribeDrdsDbRdsNameListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_rds_name_list_with_options(request, runtime)

    async def describe_drds_db_rds_name_list_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbRdsNameListRequest,
    ) -> drds_20190123_models.DescribeDrdsDbRdsNameListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_db_rds_name_list_with_options_async(request, runtime)

    def describe_drds_db_tasks_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDbTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbTasks',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_db_tasks_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDbTasks',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_db_tasks(
        self,
        request: drds_20190123_models.DescribeDrdsDbTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsDbTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_tasks_with_options(request, runtime)

    async def describe_drds_db_tasks_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsDbTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_db_tasks_with_options_async(request, runtime)

    def describe_drds_instance_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instance_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instance(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_with_options(request, runtime)

    async def describe_drds_instance_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_with_options_async(request, runtime)

    def describe_drds_instance_db_monitor_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceDbMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceDbMonitor',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instance_db_monitor_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceDbMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceDbMonitor',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instance_db_monitor(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceDbMonitorRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_db_monitor_with_options(request, runtime)

    async def describe_drds_instance_db_monitor_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceDbMonitorRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_db_monitor_with_options_async(request, runtime)

    def describe_drds_instance_level_tasks_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceLevelTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceLevelTasks',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instance_level_tasks_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceLevelTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceLevelTasks',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instance_level_tasks(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceLevelTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_level_tasks_with_options(request, runtime)

    async def describe_drds_instance_level_tasks_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceLevelTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_level_tasks_with_options_async(request, runtime)

    def describe_drds_instance_monitor_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.period_multiple):
            query['PeriodMultiple'] = request.period_multiple
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceMonitor',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instance_monitor_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.period_multiple):
            query['PeriodMultiple'] = request.period_multiple
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceMonitor',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instance_monitor(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceMonitorRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_monitor_with_options(request, runtime)

    async def describe_drds_instance_monitor_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceMonitorRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_monitor_with_options_async(request, runtime)

    def describe_drds_instance_version_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceVersion',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instance_version_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceVersion',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instance_version(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceVersionRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_version_with_options(request, runtime)

    async def describe_drds_instance_version_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceVersionRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_version_with_options_async(request, runtime)

    def describe_drds_instances_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.mix):
            query['Mix'] = request.mix
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_version):
            query['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instances_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.mix):
            query['Mix'] = request.mix
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_version):
            query['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instances(
        self,
        request: drds_20190123_models.DescribeDrdsInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instances_with_options(request, runtime)

    async def describe_drds_instances_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instances_with_options_async(request, runtime)

    def describe_drds_params_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.param_level):
            query['ParamLevel'] = request.param_level
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsParams',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_params_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.param_level):
            query['ParamLevel'] = request.param_level
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsParams',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_params(
        self,
        request: drds_20190123_models.DescribeDrdsParamsRequest,
    ) -> drds_20190123_models.DescribeDrdsParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_params_with_options(request, runtime)

    async def describe_drds_params_async(
        self,
        request: drds_20190123_models.DescribeDrdsParamsRequest,
    ) -> drds_20190123_models.DescribeDrdsParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_params_with_options_async(request, runtime)

    def describe_drds_rds_instances_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsRdsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsRdsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsRdsInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsRdsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_rds_instances_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsRdsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsRdsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsRdsInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsRdsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_rds_instances(
        self,
        request: drds_20190123_models.DescribeDrdsRdsInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsRdsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_rds_instances_with_options(request, runtime)

    async def describe_drds_rds_instances_async(
        self,
        request: drds_20190123_models.DescribeDrdsRdsInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsRdsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_rds_instances_with_options_async(request, runtime)

    def describe_drds_sharding_dbs_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsShardingDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsShardingDbsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_name_pattern):
            query['DbNamePattern'] = request.db_name_pattern
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsShardingDbs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsShardingDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_sharding_dbs_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsShardingDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsShardingDbsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_name_pattern):
            query['DbNamePattern'] = request.db_name_pattern
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsShardingDbs',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsShardingDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_sharding_dbs(
        self,
        request: drds_20190123_models.DescribeDrdsShardingDbsRequest,
    ) -> drds_20190123_models.DescribeDrdsShardingDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_sharding_dbs_with_options(request, runtime)

    async def describe_drds_sharding_dbs_async(
        self,
        request: drds_20190123_models.DescribeDrdsShardingDbsRequest,
    ) -> drds_20190123_models.DescribeDrdsShardingDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_sharding_dbs_with_options_async(request, runtime)

    def describe_drds_slow_sqls_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsSlowSqlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsSlowSqlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exe_time):
            query['ExeTime'] = request.exe_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsSlowSqls',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSlowSqlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_slow_sqls_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsSlowSqlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsSlowSqlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exe_time):
            query['ExeTime'] = request.exe_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsSlowSqls',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSlowSqlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_slow_sqls(
        self,
        request: drds_20190123_models.DescribeDrdsSlowSqlsRequest,
    ) -> drds_20190123_models.DescribeDrdsSlowSqlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_slow_sqls_with_options(request, runtime)

    async def describe_drds_slow_sqls_async(
        self,
        request: drds_20190123_models.DescribeDrdsSlowSqlsRequest,
    ) -> drds_20190123_models.DescribeDrdsSlowSqlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_slow_sqls_with_options_async(request, runtime)

    def describe_drds_sql_audit_status_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsSqlAuditStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsSqlAuditStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsSqlAuditStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSqlAuditStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_sql_audit_status_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsSqlAuditStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsSqlAuditStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsSqlAuditStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSqlAuditStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_sql_audit_status(
        self,
        request: drds_20190123_models.DescribeDrdsSqlAuditStatusRequest,
    ) -> drds_20190123_models.DescribeDrdsSqlAuditStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_sql_audit_status_with_options(request, runtime)

    async def describe_drds_sql_audit_status_async(
        self,
        request: drds_20190123_models.DescribeDrdsSqlAuditStatusRequest,
    ) -> drds_20190123_models.DescribeDrdsSqlAuditStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_sql_audit_status_with_options_async(request, runtime)

    def describe_drds_tasks_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsTasks',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_tasks_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrdsTasks',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_tasks(
        self,
        request: drds_20190123_models.DescribeDrdsTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_tasks_with_options(request, runtime)

    async def describe_drds_tasks_async(
        self,
        request: drds_20190123_models.DescribeDrdsTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_tasks_with_options_async(request, runtime)

    def describe_expand_logic_table_info_list_with_options(
        self,
        request: drds_20190123_models.DescribeExpandLogicTableInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeExpandLogicTableInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpandLogicTableInfoList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeExpandLogicTableInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_expand_logic_table_info_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeExpandLogicTableInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeExpandLogicTableInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpandLogicTableInfoList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeExpandLogicTableInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_expand_logic_table_info_list(
        self,
        request: drds_20190123_models.DescribeExpandLogicTableInfoListRequest,
    ) -> drds_20190123_models.DescribeExpandLogicTableInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_expand_logic_table_info_list_with_options(request, runtime)

    async def describe_expand_logic_table_info_list_async(
        self,
        request: drds_20190123_models.DescribeExpandLogicTableInfoListRequest,
    ) -> drds_20190123_models.DescribeExpandLogicTableInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_expand_logic_table_info_list_with_options_async(request, runtime)

    def describe_hot_db_list_with_options(
        self,
        request: drds_20190123_models.DescribeHotDbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeHotDbListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHotDbList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeHotDbListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hot_db_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeHotDbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeHotDbListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHotDbList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeHotDbListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hot_db_list(
        self,
        request: drds_20190123_models.DescribeHotDbListRequest,
    ) -> drds_20190123_models.DescribeHotDbListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_db_list_with_options(request, runtime)

    async def describe_hot_db_list_async(
        self,
        request: drds_20190123_models.DescribeHotDbListRequest,
    ) -> drds_20190123_models.DescribeHotDbListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hot_db_list_with_options_async(request, runtime)

    def describe_inst_db_log_info_with_options(
        self,
        request: drds_20190123_models.DescribeInstDbLogInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstDbLogInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstDbLogInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbLogInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inst_db_log_info_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstDbLogInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstDbLogInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstDbLogInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbLogInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inst_db_log_info(
        self,
        request: drds_20190123_models.DescribeInstDbLogInfoRequest,
    ) -> drds_20190123_models.DescribeInstDbLogInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_inst_db_log_info_with_options(request, runtime)

    async def describe_inst_db_log_info_async(
        self,
        request: drds_20190123_models.DescribeInstDbLogInfoRequest,
    ) -> drds_20190123_models.DescribeInstDbLogInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_inst_db_log_info_with_options_async(request, runtime)

    def describe_inst_db_sls_info_with_options(
        self,
        request: drds_20190123_models.DescribeInstDbSlsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstDbSlsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstDbSlsInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbSlsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inst_db_sls_info_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstDbSlsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstDbSlsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstDbSlsInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbSlsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inst_db_sls_info(
        self,
        request: drds_20190123_models.DescribeInstDbSlsInfoRequest,
    ) -> drds_20190123_models.DescribeInstDbSlsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_inst_db_sls_info_with_options(request, runtime)

    async def describe_inst_db_sls_info_async(
        self,
        request: drds_20190123_models.DescribeInstDbSlsInfoRequest,
    ) -> drds_20190123_models.DescribeInstDbSlsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_inst_db_sls_info_with_options_async(request, runtime)

    def describe_instance_accounts_with_options(
        self,
        request: drds_20190123_models.DescribeInstanceAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAccounts',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_accounts_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstanceAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAccounts',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_accounts(
        self,
        request: drds_20190123_models.DescribeInstanceAccountsRequest,
    ) -> drds_20190123_models.DescribeInstanceAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_accounts_with_options(request, runtime)

    async def describe_instance_accounts_async(
        self,
        request: drds_20190123_models.DescribeInstanceAccountsRequest,
    ) -> drds_20190123_models.DescribeInstanceAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_accounts_with_options_async(request, runtime)

    def describe_instance_switch_azone_with_options(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchAzoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceSwitchAzoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSwitchAzone',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchAzoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_switch_azone_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchAzoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceSwitchAzoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSwitchAzone',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchAzoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_switch_azone(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchAzoneRequest,
    ) -> drds_20190123_models.DescribeInstanceSwitchAzoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_switch_azone_with_options(request, runtime)

    async def describe_instance_switch_azone_async(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchAzoneRequest,
    ) -> drds_20190123_models.DescribeInstanceSwitchAzoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_switch_azone_with_options_async(request, runtime)

    def describe_instance_switch_network_with_options(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceSwitchNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSwitchNetwork',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_switch_network_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceSwitchNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSwitchNetwork',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_switch_network(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchNetworkRequest,
    ) -> drds_20190123_models.DescribeInstanceSwitchNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_switch_network_with_options(request, runtime)

    async def describe_instance_switch_network_async(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchNetworkRequest,
    ) -> drds_20190123_models.DescribeInstanceSwitchNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_switch_network_with_options_async(request, runtime)

    def describe_pre_check_result_with_options(
        self,
        request: drds_20190123_models.DescribePreCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribePreCheckResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckResult',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribePreCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pre_check_result_with_options_async(
        self,
        request: drds_20190123_models.DescribePreCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribePreCheckResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckResult',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribePreCheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pre_check_result(
        self,
        request: drds_20190123_models.DescribePreCheckResultRequest,
    ) -> drds_20190123_models.DescribePreCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_result_with_options(request, runtime)

    async def describe_pre_check_result_async(
        self,
        request: drds_20190123_models.DescribePreCheckResultRequest,
    ) -> drds_20190123_models.DescribePreCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pre_check_result_with_options_async(request, runtime)

    def describe_rdsperformance_with_options(
        self,
        request: drds_20190123_models.DescribeRDSPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRDSPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keys):
            query['Keys'] = request.keys
        if not UtilClient.is_unset(request.rds_instance_id):
            query['RdsInstanceId'] = request.rds_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRDSPerformance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRDSPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rdsperformance_with_options_async(
        self,
        request: drds_20190123_models.DescribeRDSPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRDSPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keys):
            query['Keys'] = request.keys
        if not UtilClient.is_unset(request.rds_instance_id):
            query['RdsInstanceId'] = request.rds_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRDSPerformance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRDSPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rdsperformance(
        self,
        request: drds_20190123_models.DescribeRDSPerformanceRequest,
    ) -> drds_20190123_models.DescribeRDSPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rdsperformance_with_options(request, runtime)

    async def describe_rdsperformance_async(
        self,
        request: drds_20190123_models.DescribeRDSPerformanceRequest,
    ) -> drds_20190123_models.DescribeRDSPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rdsperformance_with_options_async(request, runtime)

    def describe_rds_commodity_with_options(
        self,
        request: drds_20190123_models.DescribeRdsCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsCommodityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsCommodity',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_commodity_with_options_async(
        self,
        request: drds_20190123_models.DescribeRdsCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsCommodityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsCommodity',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsCommodityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_commodity(
        self,
        request: drds_20190123_models.DescribeRdsCommodityRequest,
    ) -> drds_20190123_models.DescribeRdsCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_commodity_with_options(request, runtime)

    async def describe_rds_commodity_async(
        self,
        request: drds_20190123_models.DescribeRdsCommodityRequest,
    ) -> drds_20190123_models.DescribeRdsCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_commodity_with_options_async(request, runtime)

    def describe_rds_performance_summary_with_options(
        self,
        request: drds_20190123_models.DescribeRdsPerformanceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsPerformanceSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.rds_instance_id):
            query['RdsInstanceId'] = request.rds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsPerformanceSummary',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsPerformanceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_performance_summary_with_options_async(
        self,
        request: drds_20190123_models.DescribeRdsPerformanceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsPerformanceSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.rds_instance_id):
            query['RdsInstanceId'] = request.rds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsPerformanceSummary',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsPerformanceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_performance_summary(
        self,
        request: drds_20190123_models.DescribeRdsPerformanceSummaryRequest,
    ) -> drds_20190123_models.DescribeRdsPerformanceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_performance_summary_with_options(request, runtime)

    async def describe_rds_performance_summary_async(
        self,
        request: drds_20190123_models.DescribeRdsPerformanceSummaryRequest,
    ) -> drds_20190123_models.DescribeRdsPerformanceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_performance_summary_with_options_async(request, runtime)

    def describe_rds_super_account_instances_with_options(
        self,
        request: drds_20190123_models.DescribeRdsSuperAccountInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsSuperAccountInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.rds_instance):
            query['RdsInstance'] = request.rds_instance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsSuperAccountInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsSuperAccountInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_super_account_instances_with_options_async(
        self,
        request: drds_20190123_models.DescribeRdsSuperAccountInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsSuperAccountInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.rds_instance):
            query['RdsInstance'] = request.rds_instance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsSuperAccountInstances',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsSuperAccountInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_super_account_instances(
        self,
        request: drds_20190123_models.DescribeRdsSuperAccountInstancesRequest,
    ) -> drds_20190123_models.DescribeRdsSuperAccountInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_super_account_instances_with_options(request, runtime)

    async def describe_rds_super_account_instances_async(
        self,
        request: drds_20190123_models.DescribeRdsSuperAccountInstancesRequest,
    ) -> drds_20190123_models.DescribeRdsSuperAccountInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_super_account_instances_with_options_async(request, runtime)

    def describe_recycle_bin_status_with_options(
        self,
        request: drds_20190123_models.DescribeRecycleBinStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRecycleBinStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecycleBinStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recycle_bin_status_with_options_async(
        self,
        request: drds_20190123_models.DescribeRecycleBinStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRecycleBinStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecycleBinStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recycle_bin_status(
        self,
        request: drds_20190123_models.DescribeRecycleBinStatusRequest,
    ) -> drds_20190123_models.DescribeRecycleBinStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_recycle_bin_status_with_options(request, runtime)

    async def describe_recycle_bin_status_async(
        self,
        request: drds_20190123_models.DescribeRecycleBinStatusRequest,
    ) -> drds_20190123_models.DescribeRecycleBinStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_recycle_bin_status_with_options_async(request, runtime)

    def describe_recycle_bin_tables_with_options(
        self,
        request: drds_20190123_models.DescribeRecycleBinTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRecycleBinTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecycleBinTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recycle_bin_tables_with_options_async(
        self,
        request: drds_20190123_models.DescribeRecycleBinTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRecycleBinTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecycleBinTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recycle_bin_tables(
        self,
        request: drds_20190123_models.DescribeRecycleBinTablesRequest,
    ) -> drds_20190123_models.DescribeRecycleBinTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_recycle_bin_tables_with_options(request, runtime)

    async def describe_recycle_bin_tables_async(
        self,
        request: drds_20190123_models.DescribeRecycleBinTablesRequest,
    ) -> drds_20190123_models.DescribeRecycleBinTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_recycle_bin_tables_with_options_async(request, runtime)

    def describe_restore_order_with_options(
        self,
        request: drds_20190123_models.DescribeRestoreOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRestoreOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_db_names):
            query['BackupDbNames'] = request.backup_db_names
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_level):
            query['BackupLevel'] = request.backup_level
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreOrder',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRestoreOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_order_with_options_async(
        self,
        request: drds_20190123_models.DescribeRestoreOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRestoreOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_db_names):
            query['BackupDbNames'] = request.backup_db_names
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_level):
            query['BackupLevel'] = request.backup_level
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreOrder',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRestoreOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_order(
        self,
        request: drds_20190123_models.DescribeRestoreOrderRequest,
    ) -> drds_20190123_models.DescribeRestoreOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_order_with_options(request, runtime)

    async def describe_restore_order_async(
        self,
        request: drds_20190123_models.DescribeRestoreOrderRequest,
    ) -> drds_20190123_models.DescribeRestoreOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_order_with_options_async(request, runtime)

    def describe_shard_task_info_with_options(
        self,
        request: drds_20190123_models.DescribeShardTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeShardTaskInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_table_name):
            query['SourceTableName'] = request.source_table_name
        if not UtilClient.is_unset(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShardTaskInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_shard_task_info_with_options_async(
        self,
        request: drds_20190123_models.DescribeShardTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeShardTaskInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_table_name):
            query['SourceTableName'] = request.source_table_name
        if not UtilClient.is_unset(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShardTaskInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_shard_task_info(
        self,
        request: drds_20190123_models.DescribeShardTaskInfoRequest,
    ) -> drds_20190123_models.DescribeShardTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_shard_task_info_with_options(request, runtime)

    async def describe_shard_task_info_async(
        self,
        request: drds_20190123_models.DescribeShardTaskInfoRequest,
    ) -> drds_20190123_models.DescribeShardTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_shard_task_info_with_options_async(request, runtime)

    def describe_shard_task_list_with_options(
        self,
        request: drds_20190123_models.DescribeShardTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeShardTaskListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShardTaskList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_shard_task_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeShardTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeShardTaskListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShardTaskList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_shard_task_list(
        self,
        request: drds_20190123_models.DescribeShardTaskListRequest,
    ) -> drds_20190123_models.DescribeShardTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_shard_task_list_with_options(request, runtime)

    async def describe_shard_task_list_async(
        self,
        request: drds_20190123_models.DescribeShardTaskListRequest,
    ) -> drds_20190123_models.DescribeShardTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_shard_task_list_with_options_async(request, runtime)

    def describe_sql_flashbak_task_with_options(
        self,
        request: drds_20190123_models.DescribeSqlFlashbakTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeSqlFlashbakTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSqlFlashbakTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeSqlFlashbakTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_flashbak_task_with_options_async(
        self,
        request: drds_20190123_models.DescribeSqlFlashbakTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeSqlFlashbakTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSqlFlashbakTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeSqlFlashbakTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_flashbak_task(
        self,
        request: drds_20190123_models.DescribeSqlFlashbakTaskRequest,
    ) -> drds_20190123_models.DescribeSqlFlashbakTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_flashbak_task_with_options(request, runtime)

    async def describe_sql_flashbak_task_async(
        self,
        request: drds_20190123_models.DescribeSqlFlashbakTaskRequest,
    ) -> drds_20190123_models.DescribeSqlFlashbakTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_flashbak_task_with_options_async(request, runtime)

    def describe_table_with_options(
        self,
        request: drds_20190123_models.DescribeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_with_options_async(
        self,
        request: drds_20190123_models.DescribeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table(
        self,
        request: drds_20190123_models.DescribeTableRequest,
    ) -> drds_20190123_models.DescribeTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_table_with_options(request, runtime)

    async def describe_table_async(
        self,
        request: drds_20190123_models.DescribeTableRequest,
    ) -> drds_20190123_models.DescribeTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_with_options_async(request, runtime)

    def describe_table_list_by_type_with_options(
        self,
        request: drds_20190123_models.DescribeTableListByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTableListByTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTableListByType',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableListByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_list_by_type_with_options_async(
        self,
        request: drds_20190123_models.DescribeTableListByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTableListByTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTableListByType',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableListByTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_list_by_type(
        self,
        request: drds_20190123_models.DescribeTableListByTypeRequest,
    ) -> drds_20190123_models.DescribeTableListByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_table_list_by_type_with_options(request, runtime)

    async def describe_table_list_by_type_async(
        self,
        request: drds_20190123_models.DescribeTableListByTypeRequest,
    ) -> drds_20190123_models.DescribeTableListByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_list_by_type_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: drds_20190123_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: drds_20190123_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tables(
        self,
        request: drds_20190123_models.DescribeTablesRequest,
    ) -> drds_20190123_models.DescribeTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: drds_20190123_models.DescribeTablesRequest,
    ) -> drds_20190123_models.DescribeTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def disable_sql_audit_with_options(
        self,
        request: drds_20190123_models.DisableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DisableSqlAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSqlAudit',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DisableSqlAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_sql_audit_with_options_async(
        self,
        request: drds_20190123_models.DisableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DisableSqlAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSqlAudit',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.DisableSqlAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_sql_audit(
        self,
        request: drds_20190123_models.DisableSqlAuditRequest,
    ) -> drds_20190123_models.DisableSqlAuditResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_sql_audit_with_options(request, runtime)

    async def disable_sql_audit_async(
        self,
        request: drds_20190123_models.DisableSqlAuditRequest,
    ) -> drds_20190123_models.DisableSqlAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_sql_audit_with_options_async(request, runtime)

    def enable_instance_ipv_6address_with_options(
        self,
        request: drds_20190123_models.EnableInstanceIpv6AddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableInstanceIpv6AddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInstanceIpv6Address',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableInstanceIpv6AddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_instance_ipv_6address_with_options_async(
        self,
        request: drds_20190123_models.EnableInstanceIpv6AddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableInstanceIpv6AddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInstanceIpv6Address',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableInstanceIpv6AddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_instance_ipv_6address(
        self,
        request: drds_20190123_models.EnableInstanceIpv6AddressRequest,
    ) -> drds_20190123_models.EnableInstanceIpv6AddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_ipv_6address_with_options(request, runtime)

    async def enable_instance_ipv_6address_async(
        self,
        request: drds_20190123_models.EnableInstanceIpv6AddressRequest,
    ) -> drds_20190123_models.EnableInstanceIpv6AddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_instance_ipv_6address_with_options_async(request, runtime)

    def enable_sql_audit_with_options(
        self,
        request: drds_20190123_models.EnableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableSqlAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.is_recall):
            query['IsRecall'] = request.is_recall
        if not UtilClient.is_unset(request.recall_end_timestamp):
            query['RecallEndTimestamp'] = request.recall_end_timestamp
        if not UtilClient.is_unset(request.recall_start_timestamp):
            query['RecallStartTimestamp'] = request.recall_start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSqlAudit',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sql_audit_with_options_async(
        self,
        request: drds_20190123_models.EnableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableSqlAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.is_recall):
            query['IsRecall'] = request.is_recall
        if not UtilClient.is_unset(request.recall_end_timestamp):
            query['RecallEndTimestamp'] = request.recall_end_timestamp
        if not UtilClient.is_unset(request.recall_start_timestamp):
            query['RecallStartTimestamp'] = request.recall_start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSqlAudit',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_sql_audit(
        self,
        request: drds_20190123_models.EnableSqlAuditRequest,
    ) -> drds_20190123_models.EnableSqlAuditResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_audit_with_options(request, runtime)

    async def enable_sql_audit_async(
        self,
        request: drds_20190123_models.EnableSqlAuditRequest,
    ) -> drds_20190123_models.EnableSqlAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_sql_audit_with_options_async(request, runtime)

    def enable_sql_flashback_match_switch_with_options(
        self,
        request: drds_20190123_models.EnableSqlFlashbackMatchSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSqlFlashbackMatchSwitch',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sql_flashback_match_switch_with_options_async(
        self,
        request: drds_20190123_models.EnableSqlFlashbackMatchSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSqlFlashbackMatchSwitch',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_sql_flashback_match_switch(
        self,
        request: drds_20190123_models.EnableSqlFlashbackMatchSwitchRequest,
    ) -> drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_flashback_match_switch_with_options(request, runtime)

    async def enable_sql_flashback_match_switch_async(
        self,
        request: drds_20190123_models.EnableSqlFlashbackMatchSwitchRequest,
    ) -> drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_sql_flashback_match_switch_with_options_async(request, runtime)

    def flashback_recycle_bin_table_with_options(
        self,
        request: drds_20190123_models.FlashbackRecycleBinTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.FlashbackRecycleBinTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlashbackRecycleBinTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.FlashbackRecycleBinTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def flashback_recycle_bin_table_with_options_async(
        self,
        request: drds_20190123_models.FlashbackRecycleBinTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.FlashbackRecycleBinTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlashbackRecycleBinTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.FlashbackRecycleBinTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def flashback_recycle_bin_table(
        self,
        request: drds_20190123_models.FlashbackRecycleBinTableRequest,
    ) -> drds_20190123_models.FlashbackRecycleBinTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.flashback_recycle_bin_table_with_options(request, runtime)

    async def flashback_recycle_bin_table_async(
        self,
        request: drds_20190123_models.FlashbackRecycleBinTableRequest,
    ) -> drds_20190123_models.FlashbackRecycleBinTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.flashback_recycle_bin_table_with_options_async(request, runtime)

    def get_drds_db_rds_relation_info_with_options(
        self,
        request: drds_20190123_models.GetDrdsDbRdsRelationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.GetDrdsDbRdsRelationInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDrdsDbRdsRelationInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.GetDrdsDbRdsRelationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_drds_db_rds_relation_info_with_options_async(
        self,
        request: drds_20190123_models.GetDrdsDbRdsRelationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.GetDrdsDbRdsRelationInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDrdsDbRdsRelationInfo',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.GetDrdsDbRdsRelationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_drds_db_rds_relation_info(
        self,
        request: drds_20190123_models.GetDrdsDbRdsRelationInfoRequest,
    ) -> drds_20190123_models.GetDrdsDbRdsRelationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_drds_db_rds_relation_info_with_options(request, runtime)

    async def get_drds_db_rds_relation_info_async(
        self,
        request: drds_20190123_models.GetDrdsDbRdsRelationInfoRequest,
    ) -> drds_20190123_models.GetDrdsDbRdsRelationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_drds_db_rds_relation_info_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: drds_20190123_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: drds_20190123_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: drds_20190123_models.ListTagResourcesRequest,
    ) -> drds_20190123_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: drds_20190123_models.ListTagResourcesRequest,
    ) -> drds_20190123_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def manage_private_rds_with_options(
        self,
        request: drds_20190123_models.ManagePrivateRdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ManagePrivateRdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.rds_action):
            query['RdsAction'] = request.rds_action
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManagePrivateRds',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ManagePrivateRdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_private_rds_with_options_async(
        self,
        request: drds_20190123_models.ManagePrivateRdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ManagePrivateRdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.rds_action):
            query['RdsAction'] = request.rds_action
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManagePrivateRds',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ManagePrivateRdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_private_rds(
        self,
        request: drds_20190123_models.ManagePrivateRdsRequest,
    ) -> drds_20190123_models.ManagePrivateRdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.manage_private_rds_with_options(request, runtime)

    async def manage_private_rds_async(
        self,
        request: drds_20190123_models.ManagePrivateRdsRequest,
    ) -> drds_20190123_models.ManagePrivateRdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.manage_private_rds_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: drds_20190123_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: drds_20190123_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: drds_20190123_models.ModifyAccountDescriptionRequest,
    ) -> drds_20190123_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: drds_20190123_models.ModifyAccountDescriptionRequest,
    ) -> drds_20190123_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_account_privilege_with_options(
        self,
        request: drds_20190123_models.ModifyAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.db_privilege):
            query['DbPrivilege'] = request.db_privilege
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPrivilege',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_privilege_with_options_async(
        self,
        request: drds_20190123_models.ModifyAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.db_privilege):
            query['DbPrivilege'] = request.db_privilege
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPrivilege',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountPrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_privilege(
        self,
        request: drds_20190123_models.ModifyAccountPrivilegeRequest,
    ) -> drds_20190123_models.ModifyAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_privilege_with_options(request, runtime)

    async def modify_account_privilege_async(
        self,
        request: drds_20190123_models.ModifyAccountPrivilegeRequest,
    ) -> drds_20190123_models.ModifyAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_privilege_with_options_async(request, runtime)

    def modify_drds_instance_description_with_options(
        self,
        request: drds_20190123_models.ModifyDrdsInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyDrdsInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDrdsInstanceDescription',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_drds_instance_description_with_options_async(
        self,
        request: drds_20190123_models.ModifyDrdsInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyDrdsInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDrdsInstanceDescription',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_drds_instance_description(
        self,
        request: drds_20190123_models.ModifyDrdsInstanceDescriptionRequest,
    ) -> drds_20190123_models.ModifyDrdsInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_instance_description_with_options(request, runtime)

    async def modify_drds_instance_description_async(
        self,
        request: drds_20190123_models.ModifyDrdsInstanceDescriptionRequest,
    ) -> drds_20190123_models.ModifyDrdsInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_drds_instance_description_with_options_async(request, runtime)

    def modify_drds_ip_white_list_with_options(
        self,
        request: drds_20190123_models.ModifyDrdsIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyDrdsIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.group_attribute):
            query['GroupAttribute'] = request.group_attribute
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ip_white_list):
            query['IpWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDrdsIpWhiteList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_drds_ip_white_list_with_options_async(
        self,
        request: drds_20190123_models.ModifyDrdsIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyDrdsIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.group_attribute):
            query['GroupAttribute'] = request.group_attribute
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ip_white_list):
            query['IpWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDrdsIpWhiteList',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_drds_ip_white_list(
        self,
        request: drds_20190123_models.ModifyDrdsIpWhiteListRequest,
    ) -> drds_20190123_models.ModifyDrdsIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_ip_white_list_with_options(request, runtime)

    async def modify_drds_ip_white_list_async(
        self,
        request: drds_20190123_models.ModifyDrdsIpWhiteListRequest,
    ) -> drds_20190123_models.ModifyDrdsIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_drds_ip_white_list_with_options_async(request, runtime)

    def modify_polar_db_read_weight_with_options(
        self,
        request: drds_20190123_models.ModifyPolarDbReadWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyPolarDbReadWeightResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_node_ids):
            query['DbNodeIds'] = request.db_node_ids
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.weights):
            query['Weights'] = request.weights
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolarDbReadWeight',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyPolarDbReadWeightResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_polar_db_read_weight_with_options_async(
        self,
        request: drds_20190123_models.ModifyPolarDbReadWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyPolarDbReadWeightResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_node_ids):
            query['DbNodeIds'] = request.db_node_ids
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.weights):
            query['Weights'] = request.weights
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolarDbReadWeight',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyPolarDbReadWeightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_polar_db_read_weight(
        self,
        request: drds_20190123_models.ModifyPolarDbReadWeightRequest,
    ) -> drds_20190123_models.ModifyPolarDbReadWeightResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_polar_db_read_weight_with_options(request, runtime)

    async def modify_polar_db_read_weight_async(
        self,
        request: drds_20190123_models.ModifyPolarDbReadWeightRequest,
    ) -> drds_20190123_models.ModifyPolarDbReadWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_polar_db_read_weight_with_options_async(request, runtime)

    def modify_rds_read_weight_with_options(
        self,
        request: drds_20190123_models.ModifyRdsReadWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyRdsReadWeightResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.instance_names):
            query['InstanceNames'] = request.instance_names
        if not UtilClient.is_unset(request.weights):
            query['Weights'] = request.weights
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRdsReadWeight',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyRdsReadWeightResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rds_read_weight_with_options_async(
        self,
        request: drds_20190123_models.ModifyRdsReadWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyRdsReadWeightResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.instance_names):
            query['InstanceNames'] = request.instance_names
        if not UtilClient.is_unset(request.weights):
            query['Weights'] = request.weights
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRdsReadWeight',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyRdsReadWeightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rds_read_weight(
        self,
        request: drds_20190123_models.ModifyRdsReadWeightRequest,
    ) -> drds_20190123_models.ModifyRdsReadWeightResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_rds_read_weight_with_options(request, runtime)

    async def modify_rds_read_weight_async(
        self,
        request: drds_20190123_models.ModifyRdsReadWeightRequest,
    ) -> drds_20190123_models.ModifyRdsReadWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_rds_read_weight_with_options_async(request, runtime)

    def put_start_backup_with_options(
        self,
        request: drds_20190123_models.PutStartBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PutStartBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_db_names):
            query['BackupDbNames'] = request.backup_db_names
        if not UtilClient.is_unset(request.backup_level):
            query['BackupLevel'] = request.backup_level
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutStartBackup',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.PutStartBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_start_backup_with_options_async(
        self,
        request: drds_20190123_models.PutStartBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PutStartBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_db_names):
            query['BackupDbNames'] = request.backup_db_names
        if not UtilClient.is_unset(request.backup_level):
            query['BackupLevel'] = request.backup_level
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutStartBackup',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.PutStartBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_start_backup(
        self,
        request: drds_20190123_models.PutStartBackupRequest,
    ) -> drds_20190123_models.PutStartBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_start_backup_with_options(request, runtime)

    async def put_start_backup_async(
        self,
        request: drds_20190123_models.PutStartBackupRequest,
    ) -> drds_20190123_models.PutStartBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_start_backup_with_options_async(request, runtime)

    def refresh_drds_atom_url_with_options(
        self,
        request: drds_20190123_models.RefreshDrdsAtomUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RefreshDrdsAtomUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDrdsAtomUrl',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RefreshDrdsAtomUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_drds_atom_url_with_options_async(
        self,
        request: drds_20190123_models.RefreshDrdsAtomUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RefreshDrdsAtomUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDrdsAtomUrl',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RefreshDrdsAtomUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_drds_atom_url(
        self,
        request: drds_20190123_models.RefreshDrdsAtomUrlRequest,
    ) -> drds_20190123_models.RefreshDrdsAtomUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_drds_atom_url_with_options(request, runtime)

    async def refresh_drds_atom_url_async(
        self,
        request: drds_20190123_models.RefreshDrdsAtomUrlRequest,
    ) -> drds_20190123_models.RefreshDrdsAtomUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_drds_atom_url_with_options_async(request, runtime)

    def release_instance_internet_address_with_options(
        self,
        request: drds_20190123_models.ReleaseInstanceInternetAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ReleaseInstanceInternetAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstanceInternetAddress',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ReleaseInstanceInternetAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_internet_address_with_options_async(
        self,
        request: drds_20190123_models.ReleaseInstanceInternetAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ReleaseInstanceInternetAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstanceInternetAddress',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ReleaseInstanceInternetAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance_internet_address(
        self,
        request: drds_20190123_models.ReleaseInstanceInternetAddressRequest,
    ) -> drds_20190123_models.ReleaseInstanceInternetAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_internet_address_with_options(request, runtime)

    async def release_instance_internet_address_async(
        self,
        request: drds_20190123_models.ReleaseInstanceInternetAddressRequest,
    ) -> drds_20190123_models.ReleaseInstanceInternetAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_internet_address_with_options_async(request, runtime)

    def remove_backups_set_with_options(
        self,
        request: drds_20190123_models.RemoveBackupsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveBackupsSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBackupsSet',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveBackupsSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_backups_set_with_options_async(
        self,
        request: drds_20190123_models.RemoveBackupsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveBackupsSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBackupsSet',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveBackupsSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_backups_set(
        self,
        request: drds_20190123_models.RemoveBackupsSetRequest,
    ) -> drds_20190123_models.RemoveBackupsSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_backups_set_with_options(request, runtime)

    async def remove_backups_set_async(
        self,
        request: drds_20190123_models.RemoveBackupsSetRequest,
    ) -> drds_20190123_models.RemoveBackupsSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_backups_set_with_options_async(request, runtime)

    def remove_drds_db_with_options(
        self,
        request: drds_20190123_models.RemoveDrdsDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsDbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDrdsDb',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_drds_db_with_options_async(
        self,
        request: drds_20190123_models.RemoveDrdsDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsDbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDrdsDb',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_drds_db(
        self,
        request: drds_20190123_models.RemoveDrdsDbRequest,
    ) -> drds_20190123_models.RemoveDrdsDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_db_with_options(request, runtime)

    async def remove_drds_db_async(
        self,
        request: drds_20190123_models.RemoveDrdsDbRequest,
    ) -> drds_20190123_models.RemoveDrdsDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_drds_db_with_options_async(request, runtime)

    def remove_drds_db_failed_record_with_options(
        self,
        request: drds_20190123_models.RemoveDrdsDbFailedRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsDbFailedRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDrdsDbFailedRecord',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbFailedRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_drds_db_failed_record_with_options_async(
        self,
        request: drds_20190123_models.RemoveDrdsDbFailedRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsDbFailedRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDrdsDbFailedRecord',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbFailedRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_drds_db_failed_record(
        self,
        request: drds_20190123_models.RemoveDrdsDbFailedRecordRequest,
    ) -> drds_20190123_models.RemoveDrdsDbFailedRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_db_failed_record_with_options(request, runtime)

    async def remove_drds_db_failed_record_async(
        self,
        request: drds_20190123_models.RemoveDrdsDbFailedRecordRequest,
    ) -> drds_20190123_models.RemoveDrdsDbFailedRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_drds_db_failed_record_with_options_async(request, runtime)

    def remove_drds_instance_with_options(
        self,
        request: drds_20190123_models.RemoveDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_drds_instance_with_options_async(
        self,
        request: drds_20190123_models.RemoveDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_drds_instance(
        self,
        request: drds_20190123_models.RemoveDrdsInstanceRequest,
    ) -> drds_20190123_models.RemoveDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_instance_with_options(request, runtime)

    async def remove_drds_instance_async(
        self,
        request: drds_20190123_models.RemoveDrdsInstanceRequest,
    ) -> drds_20190123_models.RemoveDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_drds_instance_with_options_async(request, runtime)

    def remove_instance_account_with_options(
        self,
        request: drds_20190123_models.RemoveInstanceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveInstanceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveInstanceAccount',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_instance_account_with_options_async(
        self,
        request: drds_20190123_models.RemoveInstanceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveInstanceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveInstanceAccount',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_instance_account(
        self,
        request: drds_20190123_models.RemoveInstanceAccountRequest,
    ) -> drds_20190123_models.RemoveInstanceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_instance_account_with_options(request, runtime)

    async def remove_instance_account_async(
        self,
        request: drds_20190123_models.RemoveInstanceAccountRequest,
    ) -> drds_20190123_models.RemoveInstanceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_instance_account_with_options_async(request, runtime)

    def remove_recycle_bin_table_with_options(
        self,
        request: drds_20190123_models.RemoveRecycleBinTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveRecycleBinTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveRecycleBinTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveRecycleBinTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_recycle_bin_table_with_options_async(
        self,
        request: drds_20190123_models.RemoveRecycleBinTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveRecycleBinTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveRecycleBinTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveRecycleBinTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_recycle_bin_table(
        self,
        request: drds_20190123_models.RemoveRecycleBinTableRequest,
    ) -> drds_20190123_models.RemoveRecycleBinTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_recycle_bin_table_with_options(request, runtime)

    async def remove_recycle_bin_table_async(
        self,
        request: drds_20190123_models.RemoveRecycleBinTableRequest,
    ) -> drds_20190123_models.RemoveRecycleBinTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_recycle_bin_table_with_options_async(request, runtime)

    def restart_drds_instance_with_options(
        self,
        request: drds_20190123_models.RestartDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RestartDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RestartDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_drds_instance_with_options_async(
        self,
        request: drds_20190123_models.RestartDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RestartDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDrdsInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RestartDrdsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_drds_instance(
        self,
        request: drds_20190123_models.RestartDrdsInstanceRequest,
    ) -> drds_20190123_models.RestartDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_drds_instance_with_options(request, runtime)

    async def restart_drds_instance_async(
        self,
        request: drds_20190123_models.RestartDrdsInstanceRequest,
    ) -> drds_20190123_models.RestartDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_drds_instance_with_options_async(request, runtime)

    def rollback_instance_version_with_options(
        self,
        request: drds_20190123_models.RollbackInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RollbackInstanceVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackInstanceVersion',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RollbackInstanceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_instance_version_with_options_async(
        self,
        request: drds_20190123_models.RollbackInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RollbackInstanceVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackInstanceVersion',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.RollbackInstanceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_instance_version(
        self,
        request: drds_20190123_models.RollbackInstanceVersionRequest,
    ) -> drds_20190123_models.RollbackInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_instance_version_with_options(request, runtime)

    async def rollback_instance_version_async(
        self,
        request: drds_20190123_models.RollbackInstanceVersionRequest,
    ) -> drds_20190123_models.RollbackInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_instance_version_with_options_async(request, runtime)

    def set_backup_local_with_options(
        self,
        request: drds_20190123_models.SetBackupLocalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetBackupLocalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.high_space_usage_protection):
            query['HighSpaceUsageProtection'] = request.high_space_usage_protection
        if not UtilClient.is_unset(request.local_log_retention_hours):
            query['LocalLogRetentionHours'] = request.local_log_retention_hours
        if not UtilClient.is_unset(request.local_log_retention_space):
            query['LocalLogRetentionSpace'] = request.local_log_retention_space
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBackupLocal',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupLocalResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_backup_local_with_options_async(
        self,
        request: drds_20190123_models.SetBackupLocalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetBackupLocalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.high_space_usage_protection):
            query['HighSpaceUsageProtection'] = request.high_space_usage_protection
        if not UtilClient.is_unset(request.local_log_retention_hours):
            query['LocalLogRetentionHours'] = request.local_log_retention_hours
        if not UtilClient.is_unset(request.local_log_retention_space):
            query['LocalLogRetentionSpace'] = request.local_log_retention_space
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBackupLocal',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupLocalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_backup_local(
        self,
        request: drds_20190123_models.SetBackupLocalRequest,
    ) -> drds_20190123_models.SetBackupLocalResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_backup_local_with_options(request, runtime)

    async def set_backup_local_async(
        self,
        request: drds_20190123_models.SetBackupLocalRequest,
    ) -> drds_20190123_models.SetBackupLocalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_backup_local_with_options_async(request, runtime)

    def set_backup_policy_with_options(
        self,
        request: drds_20190123_models.SetBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_db_names):
            query['BackupDbNames'] = request.backup_db_names
        if not UtilClient.is_unset(request.backup_level):
            query['BackupLevel'] = request.backup_level
        if not UtilClient.is_unset(request.backup_log):
            query['BackupLog'] = request.backup_log
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.data_backup_retention_period):
            query['DataBackupRetentionPeriod'] = request.data_backup_retention_period
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.preferred_backup_end_time):
            query['PreferredBackupEndTime'] = request.preferred_backup_end_time
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_start_time):
            query['PreferredBackupStartTime'] = request.preferred_backup_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBackupPolicy',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_backup_policy_with_options_async(
        self,
        request: drds_20190123_models.SetBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_db_names):
            query['BackupDbNames'] = request.backup_db_names
        if not UtilClient.is_unset(request.backup_level):
            query['BackupLevel'] = request.backup_level
        if not UtilClient.is_unset(request.backup_log):
            query['BackupLog'] = request.backup_log
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.data_backup_retention_period):
            query['DataBackupRetentionPeriod'] = request.data_backup_retention_period
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.preferred_backup_end_time):
            query['PreferredBackupEndTime'] = request.preferred_backup_end_time
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_start_time):
            query['PreferredBackupStartTime'] = request.preferred_backup_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBackupPolicy',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_backup_policy(
        self,
        request: drds_20190123_models.SetBackupPolicyRequest,
    ) -> drds_20190123_models.SetBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_backup_policy_with_options(request, runtime)

    async def set_backup_policy_async(
        self,
        request: drds_20190123_models.SetBackupPolicyRequest,
    ) -> drds_20190123_models.SetBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_backup_policy_with_options_async(request, runtime)

    def setup_broadcast_tables_with_options(
        self,
        request: drds_20190123_models.SetupBroadcastTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupBroadcastTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetupBroadcastTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupBroadcastTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def setup_broadcast_tables_with_options_async(
        self,
        request: drds_20190123_models.SetupBroadcastTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupBroadcastTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetupBroadcastTables',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupBroadcastTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def setup_broadcast_tables(
        self,
        request: drds_20190123_models.SetupBroadcastTablesRequest,
    ) -> drds_20190123_models.SetupBroadcastTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.setup_broadcast_tables_with_options(request, runtime)

    async def setup_broadcast_tables_async(
        self,
        request: drds_20190123_models.SetupBroadcastTablesRequest,
    ) -> drds_20190123_models.SetupBroadcastTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.setup_broadcast_tables_with_options_async(request, runtime)

    def setup_drds_params_with_options(
        self,
        request: drds_20190123_models.SetupDrdsParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupDrdsParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.param_level):
            query['ParamLevel'] = request.param_level
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetupDrdsParams',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupDrdsParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def setup_drds_params_with_options_async(
        self,
        request: drds_20190123_models.SetupDrdsParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupDrdsParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.param_level):
            query['ParamLevel'] = request.param_level
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetupDrdsParams',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupDrdsParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def setup_drds_params(
        self,
        request: drds_20190123_models.SetupDrdsParamsRequest,
    ) -> drds_20190123_models.SetupDrdsParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.setup_drds_params_with_options(request, runtime)

    async def setup_drds_params_async(
        self,
        request: drds_20190123_models.SetupDrdsParamsRequest,
    ) -> drds_20190123_models.SetupDrdsParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.setup_drds_params_with_options_async(request, runtime)

    def setup_recycle_bin_status_with_options(
        self,
        request: drds_20190123_models.SetupRecycleBinStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupRecycleBinStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status_action):
            query['StatusAction'] = request.status_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetupRecycleBinStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupRecycleBinStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def setup_recycle_bin_status_with_options_async(
        self,
        request: drds_20190123_models.SetupRecycleBinStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupRecycleBinStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status_action):
            query['StatusAction'] = request.status_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetupRecycleBinStatus',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupRecycleBinStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def setup_recycle_bin_status(
        self,
        request: drds_20190123_models.SetupRecycleBinStatusRequest,
    ) -> drds_20190123_models.SetupRecycleBinStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.setup_recycle_bin_status_with_options(request, runtime)

    async def setup_recycle_bin_status_async(
        self,
        request: drds_20190123_models.SetupRecycleBinStatusRequest,
    ) -> drds_20190123_models.SetupRecycleBinStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.setup_recycle_bin_status_with_options_async(request, runtime)

    def setup_table_with_options(
        self,
        request: drds_20190123_models.SetupTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_full_table_scan):
            query['AllowFullTableScan'] = request.allow_full_table_scan
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetupTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def setup_table_with_options_async(
        self,
        request: drds_20190123_models.SetupTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_full_table_scan):
            query['AllowFullTableScan'] = request.allow_full_table_scan
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetupTable',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def setup_table(
        self,
        request: drds_20190123_models.SetupTableRequest,
    ) -> drds_20190123_models.SetupTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.setup_table_with_options(request, runtime)

    async def setup_table_async(
        self,
        request: drds_20190123_models.SetupTableRequest,
    ) -> drds_20190123_models.SetupTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.setup_table_with_options_async(request, runtime)

    def start_restore_with_options(
        self,
        request: drds_20190123_models.StartRestoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StartRestoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_db_names):
            query['BackupDbNames'] = request.backup_db_names
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_level):
            query['BackupLevel'] = request.backup_level
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRestore',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.StartRestoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_restore_with_options_async(
        self,
        request: drds_20190123_models.StartRestoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StartRestoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_db_names):
            query['BackupDbNames'] = request.backup_db_names
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_level):
            query['BackupLevel'] = request.backup_level
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRestore',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.StartRestoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_restore(
        self,
        request: drds_20190123_models.StartRestoreRequest,
    ) -> drds_20190123_models.StartRestoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_restore_with_options(request, runtime)

    async def start_restore_async(
        self,
        request: drds_20190123_models.StartRestoreRequest,
    ) -> drds_20190123_models.StartRestoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_restore_with_options_async(request, runtime)

    def submit_clean_task_with_options(
        self,
        request: drds_20190123_models.SubmitCleanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitCleanTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.expand_type):
            query['ExpandType'] = request.expand_type
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.parent_job_id):
            query['ParentJobId'] = request.parent_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCleanTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitCleanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_clean_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitCleanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitCleanTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.expand_type):
            query['ExpandType'] = request.expand_type
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.parent_job_id):
            query['ParentJobId'] = request.parent_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCleanTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitCleanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_clean_task(
        self,
        request: drds_20190123_models.SubmitCleanTaskRequest,
    ) -> drds_20190123_models.SubmitCleanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_clean_task_with_options(request, runtime)

    async def submit_clean_task_async(
        self,
        request: drds_20190123_models.SubmitCleanTaskRequest,
    ) -> drds_20190123_models.SubmitCleanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_clean_task_with_options_async(request, runtime)

    def submit_hot_expand_pre_check_task_with_options(
        self,
        request: drds_20190123_models.SubmitHotExpandPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitHotExpandPreCheckTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.table_list):
            query['TableList'] = request.table_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitHotExpandPreCheckTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandPreCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_hot_expand_pre_check_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitHotExpandPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitHotExpandPreCheckTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.table_list):
            query['TableList'] = request.table_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitHotExpandPreCheckTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandPreCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_hot_expand_pre_check_task(
        self,
        request: drds_20190123_models.SubmitHotExpandPreCheckTaskRequest,
    ) -> drds_20190123_models.SubmitHotExpandPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_hot_expand_pre_check_task_with_options(request, runtime)

    async def submit_hot_expand_pre_check_task_async(
        self,
        request: drds_20190123_models.SubmitHotExpandPreCheckTaskRequest,
    ) -> drds_20190123_models.SubmitHotExpandPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_hot_expand_pre_check_task_with_options_async(request, runtime)

    def submit_hot_expand_task_with_options(
        self,
        request: drds_20190123_models.SubmitHotExpandTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitHotExpandTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.extended_mapping):
            query['ExtendedMapping'] = request.extended_mapping
        if not UtilClient.is_unset(request.instance_db_mapping):
            query['InstanceDbMapping'] = request.instance_db_mapping
        if not UtilClient.is_unset(request.mapping):
            query['Mapping'] = request.mapping
        if not UtilClient.is_unset(request.supper_account_mapping):
            query['SupperAccountMapping'] = request.supper_account_mapping
        if not UtilClient.is_unset(request.task_desc):
            query['TaskDesc'] = request.task_desc
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitHotExpandTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_hot_expand_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitHotExpandTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitHotExpandTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.extended_mapping):
            query['ExtendedMapping'] = request.extended_mapping
        if not UtilClient.is_unset(request.instance_db_mapping):
            query['InstanceDbMapping'] = request.instance_db_mapping
        if not UtilClient.is_unset(request.mapping):
            query['Mapping'] = request.mapping
        if not UtilClient.is_unset(request.supper_account_mapping):
            query['SupperAccountMapping'] = request.supper_account_mapping
        if not UtilClient.is_unset(request.task_desc):
            query['TaskDesc'] = request.task_desc
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitHotExpandTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_hot_expand_task(
        self,
        request: drds_20190123_models.SubmitHotExpandTaskRequest,
    ) -> drds_20190123_models.SubmitHotExpandTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_hot_expand_task_with_options(request, runtime)

    async def submit_hot_expand_task_async(
        self,
        request: drds_20190123_models.SubmitHotExpandTaskRequest,
    ) -> drds_20190123_models.SubmitHotExpandTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_hot_expand_task_with_options_async(request, runtime)

    def submit_smooth_expand_pre_check_with_options(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmoothExpandPreCheck',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_smooth_expand_pre_check_with_options_async(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_inst_type):
            query['DbInstType'] = request.db_inst_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmoothExpandPreCheck',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_smooth_expand_pre_check(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckRequest,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_smooth_expand_pre_check_with_options(request, runtime)

    async def submit_smooth_expand_pre_check_async(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckRequest,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_smooth_expand_pre_check_with_options_async(request, runtime)

    def submit_smooth_expand_pre_check_task_with_options(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmoothExpandPreCheckTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_smooth_expand_pre_check_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmoothExpandPreCheckTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_smooth_expand_pre_check_task(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckTaskRequest,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_smooth_expand_pre_check_task_with_options(request, runtime)

    async def submit_smooth_expand_pre_check_task_async(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckTaskRequest,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_smooth_expand_pre_check_task_with_options_async(request, runtime)

    def submit_sql_flashback_task_with_options(
        self,
        request: drds_20190123_models.SubmitSqlFlashbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSqlFlashbackTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.recall_restore_type):
            query['RecallRestoreType'] = request.recall_restore_type
        if not UtilClient.is_unset(request.recall_type):
            query['RecallType'] = request.recall_type
        if not UtilClient.is_unset(request.sql_pk):
            query['SqlPk'] = request.sql_pk
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSqlFlashbackTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSqlFlashbackTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sql_flashback_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitSqlFlashbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSqlFlashbackTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.recall_restore_type):
            query['RecallRestoreType'] = request.recall_restore_type
        if not UtilClient.is_unset(request.recall_type):
            query['RecallType'] = request.recall_type
        if not UtilClient.is_unset(request.sql_pk):
            query['SqlPk'] = request.sql_pk
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSqlFlashbackTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSqlFlashbackTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sql_flashback_task(
        self,
        request: drds_20190123_models.SubmitSqlFlashbackTaskRequest,
    ) -> drds_20190123_models.SubmitSqlFlashbackTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_sql_flashback_task_with_options(request, runtime)

    async def submit_sql_flashback_task_async(
        self,
        request: drds_20190123_models.SubmitSqlFlashbackTaskRequest,
    ) -> drds_20190123_models.SubmitSqlFlashbackTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_sql_flashback_task_with_options_async(request, runtime)

    def switch_global_broadcast_type_with_options(
        self,
        request: drds_20190123_models.SwitchGlobalBroadcastTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SwitchGlobalBroadcastTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchGlobalBroadcastType',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SwitchGlobalBroadcastTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_global_broadcast_type_with_options_async(
        self,
        request: drds_20190123_models.SwitchGlobalBroadcastTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SwitchGlobalBroadcastTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchGlobalBroadcastType',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.SwitchGlobalBroadcastTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_global_broadcast_type(
        self,
        request: drds_20190123_models.SwitchGlobalBroadcastTypeRequest,
    ) -> drds_20190123_models.SwitchGlobalBroadcastTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_global_broadcast_type_with_options(request, runtime)

    async def switch_global_broadcast_type_async(
        self,
        request: drds_20190123_models.SwitchGlobalBroadcastTypeRequest,
    ) -> drds_20190123_models.SwitchGlobalBroadcastTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_global_broadcast_type_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: drds_20190123_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: drds_20190123_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: drds_20190123_models.TagResourcesRequest,
    ) -> drds_20190123_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: drds_20190123_models.TagResourcesRequest,
    ) -> drds_20190123_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: drds_20190123_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: drds_20190123_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: drds_20190123_models.UntagResourcesRequest,
    ) -> drds_20190123_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: drds_20190123_models.UntagResourcesRequest,
    ) -> drds_20190123_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_instance_network_with_options(
        self,
        request: drds_20190123_models.UpdateInstanceNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdateInstanceNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
        if not UtilClient.is_unset(request.src_instance_network_type):
            query['SrcInstanceNetworkType'] = request.src_instance_network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceNetwork',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateInstanceNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_network_with_options_async(
        self,
        request: drds_20190123_models.UpdateInstanceNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdateInstanceNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
        if not UtilClient.is_unset(request.src_instance_network_type):
            query['SrcInstanceNetworkType'] = request.src_instance_network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceNetwork',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateInstanceNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_network(
        self,
        request: drds_20190123_models.UpdateInstanceNetworkRequest,
    ) -> drds_20190123_models.UpdateInstanceNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_network_with_options(request, runtime)

    async def update_instance_network_async(
        self,
        request: drds_20190123_models.UpdateInstanceNetworkRequest,
    ) -> drds_20190123_models.UpdateInstanceNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_network_with_options_async(request, runtime)

    def update_private_rds_class_with_options(
        self,
        request: drds_20190123_models.UpdatePrivateRdsClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdatePrivateRdsClassResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.pre_pay_duration):
            query['PrePayDuration'] = request.pre_pay_duration
        if not UtilClient.is_unset(request.rds_class):
            query['RdsClass'] = request.rds_class
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrivateRdsClass',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdatePrivateRdsClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_private_rds_class_with_options_async(
        self,
        request: drds_20190123_models.UpdatePrivateRdsClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdatePrivateRdsClassResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.pre_pay_duration):
            query['PrePayDuration'] = request.pre_pay_duration
        if not UtilClient.is_unset(request.rds_class):
            query['RdsClass'] = request.rds_class
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrivateRdsClass',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdatePrivateRdsClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_private_rds_class(
        self,
        request: drds_20190123_models.UpdatePrivateRdsClassRequest,
    ) -> drds_20190123_models.UpdatePrivateRdsClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_private_rds_class_with_options(request, runtime)

    async def update_private_rds_class_async(
        self,
        request: drds_20190123_models.UpdatePrivateRdsClassRequest,
    ) -> drds_20190123_models.UpdatePrivateRdsClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_private_rds_class_with_options_async(request, runtime)

    def update_resource_group_attribute_with_options(
        self,
        request: drds_20190123_models.UpdateResourceGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdateResourceGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroupAttribute',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateResourceGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_group_attribute_with_options_async(
        self,
        request: drds_20190123_models.UpdateResourceGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdateResourceGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroupAttribute',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateResourceGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_group_attribute(
        self,
        request: drds_20190123_models.UpdateResourceGroupAttributeRequest,
    ) -> drds_20190123_models.UpdateResourceGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_attribute_with_options(request, runtime)

    async def update_resource_group_attribute_async(
        self,
        request: drds_20190123_models.UpdateResourceGroupAttributeRequest,
    ) -> drds_20190123_models.UpdateResourceGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_group_attribute_with_options_async(request, runtime)

    def upgrade_hi_store_instance_with_options(
        self,
        request: drds_20190123_models.UpgradeHiStoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpgradeHiStoreInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.histore_instance_id):
            query['HistoreInstanceId'] = request.histore_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeHiStoreInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeHiStoreInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_hi_store_instance_with_options_async(
        self,
        request: drds_20190123_models.UpgradeHiStoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpgradeHiStoreInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.histore_instance_id):
            query['HistoreInstanceId'] = request.histore_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeHiStoreInstance',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeHiStoreInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_hi_store_instance(
        self,
        request: drds_20190123_models.UpgradeHiStoreInstanceRequest,
    ) -> drds_20190123_models.UpgradeHiStoreInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_hi_store_instance_with_options(request, runtime)

    async def upgrade_hi_store_instance_async(
        self,
        request: drds_20190123_models.UpgradeHiStoreInstanceRequest,
    ) -> drds_20190123_models.UpgradeHiStoreInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_hi_store_instance_with_options_async(request, runtime)

    def upgrade_instance_version_with_options(
        self,
        request: drds_20190123_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpgradeInstanceVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rpm):
            query['Rpm'] = request.rpm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeInstanceVersion',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeInstanceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_instance_version_with_options_async(
        self,
        request: drds_20190123_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpgradeInstanceVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rpm):
            query['Rpm'] = request.rpm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeInstanceVersion',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeInstanceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_instance_version(
        self,
        request: drds_20190123_models.UpgradeInstanceVersionRequest,
    ) -> drds_20190123_models.UpgradeInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)

    async def upgrade_instance_version_async(
        self,
        request: drds_20190123_models.UpgradeInstanceVersionRequest,
    ) -> drds_20190123_models.UpgradeInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_instance_version_with_options_async(request, runtime)

    def validate_shard_task_with_options(
        self,
        request: drds_20190123_models.ValidateShardTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ValidateShardTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_table_name):
            query['SourceTableName'] = request.source_table_name
        if not UtilClient.is_unset(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateShardTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ValidateShardTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_shard_task_with_options_async(
        self,
        request: drds_20190123_models.ValidateShardTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ValidateShardTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.drds_instance_id):
            query['DrdsInstanceId'] = request.drds_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_table_name):
            query['SourceTableName'] = request.source_table_name
        if not UtilClient.is_unset(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateShardTask',
            version='2019-01-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20190123_models.ValidateShardTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_shard_task(
        self,
        request: drds_20190123_models.ValidateShardTaskRequest,
    ) -> drds_20190123_models.ValidateShardTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_shard_task_with_options(request, runtime)

    async def validate_shard_task_async(
        self,
        request: drds_20190123_models.ValidateShardTaskRequest,
    ) -> drds_20190123_models.ValidateShardTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_shard_task_with_options_async(request, runtime)
