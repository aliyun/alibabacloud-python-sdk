# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_drds20171016 import models as drds_20171016_models
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

    def create_drds_account_with_options(
        self,
        request: drds_20171016_models.CreateDrdsAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.CreateDrdsAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Password'] = request.password
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDrdsAccount',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.CreateDrdsAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_drds_account_with_options_async(
        self,
        request: drds_20171016_models.CreateDrdsAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.CreateDrdsAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Password'] = request.password
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDrdsAccount',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.CreateDrdsAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_drds_account(
        self,
        request: drds_20171016_models.CreateDrdsAccountRequest,
    ) -> drds_20171016_models.CreateDrdsAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_drds_account_with_options(request, runtime)

    async def create_drds_account_async(
        self,
        request: drds_20171016_models.CreateDrdsAccountRequest,
    ) -> drds_20171016_models.CreateDrdsAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_drds_account_with_options_async(request, runtime)

    def create_drds_dbwith_options(
        self,
        request: drds_20171016_models.CreateDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.CreateDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Encode'] = request.encode
        query['Password'] = request.password
        query['RdsInstances'] = request.rds_instances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDrdsDB',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.CreateDrdsDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_drds_dbwith_options_async(
        self,
        request: drds_20171016_models.CreateDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.CreateDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['Encode'] = request.encode
        query['Password'] = request.password
        query['RdsInstances'] = request.rds_instances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDrdsDB',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.CreateDrdsDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_drds_db(
        self,
        request: drds_20171016_models.CreateDrdsDBRequest,
    ) -> drds_20171016_models.CreateDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbwith_options(request, runtime)

    async def create_drds_db_async(
        self,
        request: drds_20171016_models.CreateDrdsDBRequest,
    ) -> drds_20171016_models.CreateDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_drds_dbwith_options_async(request, runtime)

    def create_drds_instance_with_options(
        self,
        request: drds_20171016_models.CreateDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.CreateDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['Duration'] = request.duration
        query['InstanceSeries'] = request.instance_series
        query['IsAutoRenew'] = request.is_auto_renew
        query['IsHa'] = request.is_ha
        query['PayType'] = request.pay_type
        query['PricingCycle'] = request.pricing_cycle
        query['Quantity'] = request.quantity
        query['RegionId'] = request.region_id
        query['Specification'] = request.specification
        query['Type'] = request.type
        query['VpcId'] = request.vpc_id
        query['VswitchId'] = request.vswitch_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDrdsInstance',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.CreateDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_drds_instance_with_options_async(
        self,
        request: drds_20171016_models.CreateDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.CreateDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['Duration'] = request.duration
        query['InstanceSeries'] = request.instance_series
        query['IsAutoRenew'] = request.is_auto_renew
        query['IsHa'] = request.is_ha
        query['PayType'] = request.pay_type
        query['PricingCycle'] = request.pricing_cycle
        query['Quantity'] = request.quantity
        query['RegionId'] = request.region_id
        query['Specification'] = request.specification
        query['Type'] = request.type
        query['VpcId'] = request.vpc_id
        query['VswitchId'] = request.vswitch_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDrdsInstance',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.CreateDrdsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_drds_instance(
        self,
        request: drds_20171016_models.CreateDrdsInstanceRequest,
    ) -> drds_20171016_models.CreateDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_drds_instance_with_options(request, runtime)

    async def create_drds_instance_async(
        self,
        request: drds_20171016_models.CreateDrdsInstanceRequest,
    ) -> drds_20171016_models.CreateDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_drds_instance_with_options_async(request, runtime)

    def create_read_only_account_with_options(
        self,
        request: drds_20171016_models.CreateReadOnlyAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.CreateReadOnlyAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateReadOnlyAccount',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.CreateReadOnlyAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_read_only_account_with_options_async(
        self,
        request: drds_20171016_models.CreateReadOnlyAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.CreateReadOnlyAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateReadOnlyAccount',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.CreateReadOnlyAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_read_only_account(
        self,
        request: drds_20171016_models.CreateReadOnlyAccountRequest,
    ) -> drds_20171016_models.CreateReadOnlyAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_read_only_account_with_options(request, runtime)

    async def create_read_only_account_async(
        self,
        request: drds_20171016_models.CreateReadOnlyAccountRequest,
    ) -> drds_20171016_models.CreateReadOnlyAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_read_only_account_with_options_async(request, runtime)

    def delete_drds_dbwith_options(
        self,
        request: drds_20171016_models.DeleteDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DeleteDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDrdsDB',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DeleteDrdsDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_drds_dbwith_options_async(
        self,
        request: drds_20171016_models.DeleteDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DeleteDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDrdsDB',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DeleteDrdsDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_drds_db(
        self,
        request: drds_20171016_models.DeleteDrdsDBRequest,
    ) -> drds_20171016_models.DeleteDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_drds_dbwith_options(request, runtime)

    async def delete_drds_db_async(
        self,
        request: drds_20171016_models.DeleteDrdsDBRequest,
    ) -> drds_20171016_models.DeleteDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_drds_dbwith_options_async(request, runtime)

    def delete_failed_drds_dbwith_options(
        self,
        request: drds_20171016_models.DeleteFailedDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DeleteFailedDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFailedDrdsDB',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DeleteFailedDrdsDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_failed_drds_dbwith_options_async(
        self,
        request: drds_20171016_models.DeleteFailedDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DeleteFailedDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFailedDrdsDB',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DeleteFailedDrdsDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_failed_drds_db(
        self,
        request: drds_20171016_models.DeleteFailedDrdsDBRequest,
    ) -> drds_20171016_models.DeleteFailedDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_failed_drds_dbwith_options(request, runtime)

    async def delete_failed_drds_db_async(
        self,
        request: drds_20171016_models.DeleteFailedDrdsDBRequest,
    ) -> drds_20171016_models.DeleteFailedDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_failed_drds_dbwith_options_async(request, runtime)

    def describe_create_drds_instance_status_with_options(
        self,
        request: drds_20171016_models.DescribeCreateDrdsInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeCreateDrdsInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCreateDrdsInstanceStatus',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeCreateDrdsInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_create_drds_instance_status_with_options_async(
        self,
        request: drds_20171016_models.DescribeCreateDrdsInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeCreateDrdsInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCreateDrdsInstanceStatus',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeCreateDrdsInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_create_drds_instance_status(
        self,
        request: drds_20171016_models.DescribeCreateDrdsInstanceStatusRequest,
    ) -> drds_20171016_models.DescribeCreateDrdsInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_create_drds_instance_status_with_options(request, runtime)

    async def describe_create_drds_instance_status_async(
        self,
        request: drds_20171016_models.DescribeCreateDrdsInstanceStatusRequest,
    ) -> drds_20171016_models.DescribeCreateDrdsInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_create_drds_instance_status_with_options_async(request, runtime)

    def describe_drds_dbwith_options(
        self,
        request: drds_20171016_models.DescribeDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDB',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_dbwith_options_async(
        self,
        request: drds_20171016_models.DescribeDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsDBResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDB',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_db(
        self,
        request: drds_20171016_models.DescribeDrdsDBRequest,
    ) -> drds_20171016_models.DescribeDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbwith_options(request, runtime)

    async def describe_drds_db_async(
        self,
        request: drds_20171016_models.DescribeDrdsDBRequest,
    ) -> drds_20171016_models.DescribeDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbwith_options_async(request, runtime)

    def describe_drds_dbip_white_list_with_options(
        self,
        request: drds_20171016_models.DescribeDrdsDBIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsDBIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBIpWhiteList',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsDBIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_dbip_white_list_with_options_async(
        self,
        request: drds_20171016_models.DescribeDrdsDBIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsDBIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBIpWhiteList',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsDBIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_dbip_white_list(
        self,
        request: drds_20171016_models.DescribeDrdsDBIpWhiteListRequest,
    ) -> drds_20171016_models.DescribeDrdsDBIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbip_white_list_with_options(request, runtime)

    async def describe_drds_dbip_white_list_async(
        self,
        request: drds_20171016_models.DescribeDrdsDBIpWhiteListRequest,
    ) -> drds_20171016_models.DescribeDrdsDBIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbip_white_list_with_options_async(request, runtime)

    def describe_drds_dbs_with_options(
        self,
        request: drds_20171016_models.DescribeDrdsDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsDBsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBs',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsDBsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_dbs_with_options_async(
        self,
        request: drds_20171016_models.DescribeDrdsDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsDBsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsDBs',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsDBsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_dbs(
        self,
        request: drds_20171016_models.DescribeDrdsDBsRequest,
    ) -> drds_20171016_models.DescribeDrdsDBsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbs_with_options(request, runtime)

    async def describe_drds_dbs_async(
        self,
        request: drds_20171016_models.DescribeDrdsDBsRequest,
    ) -> drds_20171016_models.DescribeDrdsDBsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbs_with_options_async(request, runtime)

    def describe_drds_instance_with_options(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstance',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instance_with_options_async(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstance',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instance(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceRequest,
    ) -> drds_20171016_models.DescribeDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_with_options(request, runtime)

    async def describe_drds_instance_async(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceRequest,
    ) -> drds_20171016_models.DescribeDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_with_options_async(request, runtime)

    def describe_drds_instance_db_monitor_with_options(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceDbMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsInstanceDbMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['Key'] = request.key
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceDbMonitor',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsInstanceDbMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instance_db_monitor_with_options_async(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceDbMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsInstanceDbMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['Key'] = request.key
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceDbMonitor',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsInstanceDbMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instance_db_monitor(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceDbMonitorRequest,
    ) -> drds_20171016_models.DescribeDrdsInstanceDbMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_db_monitor_with_options(request, runtime)

    async def describe_drds_instance_db_monitor_async(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceDbMonitorRequest,
    ) -> drds_20171016_models.DescribeDrdsInstanceDbMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_db_monitor_with_options_async(request, runtime)

    def describe_drds_instance_monitor_with_options(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsInstanceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['Key'] = request.key
        query['PeriodMultiple'] = request.period_multiple
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceMonitor',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instance_monitor_with_options_async(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsInstanceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EndTime'] = request.end_time
        query['Key'] = request.key
        query['PeriodMultiple'] = request.period_multiple
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceMonitor',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsInstanceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instance_monitor(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceMonitorRequest,
    ) -> drds_20171016_models.DescribeDrdsInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_monitor_with_options(request, runtime)

    async def describe_drds_instance_monitor_async(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceMonitorRequest,
    ) -> drds_20171016_models.DescribeDrdsInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_monitor_with_options_async(request, runtime)

    def describe_drds_instance_net_info_for_inner_with_options(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceNetInfoForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsInstanceNetInfoForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceNetInfoForInner',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsInstanceNetInfoForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instance_net_info_for_inner_with_options_async(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceNetInfoForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsInstanceNetInfoForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstanceNetInfoForInner',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsInstanceNetInfoForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instance_net_info_for_inner(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceNetInfoForInnerRequest,
    ) -> drds_20171016_models.DescribeDrdsInstanceNetInfoForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_net_info_for_inner_with_options(request, runtime)

    async def describe_drds_instance_net_info_for_inner_async(
        self,
        request: drds_20171016_models.DescribeDrdsInstanceNetInfoForInnerRequest,
    ) -> drds_20171016_models.DescribeDrdsInstanceNetInfoForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_net_info_for_inner_with_options_async(request, runtime)

    def describe_drds_instances_with_options(
        self,
        request: drds_20171016_models.DescribeDrdsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['Tags'] = request.tags
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstances',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drds_instances_with_options_async(
        self,
        request: drds_20171016_models.DescribeDrdsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeDrdsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['Tags'] = request.tags
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDrdsInstances',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeDrdsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drds_instances(
        self,
        request: drds_20171016_models.DescribeDrdsInstancesRequest,
    ) -> drds_20171016_models.DescribeDrdsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instances_with_options(request, runtime)

    async def describe_drds_instances_async(
        self,
        request: drds_20171016_models.DescribeDrdsInstancesRequest,
    ) -> drds_20171016_models.DescribeDrdsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instances_with_options_async(request, runtime)

    def describe_rds_list_with_options(
        self,
        request: drds_20171016_models.DescribeRdsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeRdsListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsList',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeRdsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_list_with_options_async(
        self,
        request: drds_20171016_models.DescribeRdsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeRdsListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRdsList',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeRdsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_list(
        self,
        request: drds_20171016_models.DescribeRdsListRequest,
    ) -> drds_20171016_models.DescribeRdsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_list_with_options(request, runtime)

    async def describe_rds_list_async(
        self,
        request: drds_20171016_models.DescribeRdsListRequest,
    ) -> drds_20171016_models.DescribeRdsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_list_with_options_async(request, runtime)

    def describe_read_only_account_with_options(
        self,
        request: drds_20171016_models.DescribeReadOnlyAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeReadOnlyAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeReadOnlyAccount',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeReadOnlyAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_read_only_account_with_options_async(
        self,
        request: drds_20171016_models.DescribeReadOnlyAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeReadOnlyAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeReadOnlyAccount',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeReadOnlyAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_read_only_account(
        self,
        request: drds_20171016_models.DescribeReadOnlyAccountRequest,
    ) -> drds_20171016_models.DescribeReadOnlyAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_read_only_account_with_options(request, runtime)

    async def describe_read_only_account_async(
        self,
        request: drds_20171016_models.DescribeReadOnlyAccountRequest,
    ) -> drds_20171016_models.DescribeReadOnlyAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_read_only_account_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> drds_20171016_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> drds_20171016_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_shard_dbs_with_options(
        self,
        request: drds_20171016_models.DescribeShardDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeShardDBsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeShardDBs',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeShardDBsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_shard_dbs_with_options_async(
        self,
        request: drds_20171016_models.DescribeShardDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeShardDBsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeShardDBs',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeShardDBsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_shard_dbs(
        self,
        request: drds_20171016_models.DescribeShardDBsRequest,
    ) -> drds_20171016_models.DescribeShardDBsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_shard_dbs_with_options(request, runtime)

    async def describe_shard_dbs_async(
        self,
        request: drds_20171016_models.DescribeShardDBsRequest,
    ) -> drds_20171016_models.DescribeShardDBsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_shard_dbs_with_options_async(request, runtime)

    def describe_shard_db_connection_info_with_options(
        self,
        request: drds_20171016_models.DescribeShardDbConnectionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeShardDbConnectionInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['SubDbName'] = request.sub_db_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeShardDbConnectionInfo',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeShardDbConnectionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_shard_db_connection_info_with_options_async(
        self,
        request: drds_20171016_models.DescribeShardDbConnectionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.DescribeShardDbConnectionInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['SubDbName'] = request.sub_db_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeShardDbConnectionInfo',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.DescribeShardDbConnectionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_shard_db_connection_info(
        self,
        request: drds_20171016_models.DescribeShardDbConnectionInfoRequest,
    ) -> drds_20171016_models.DescribeShardDbConnectionInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_shard_db_connection_info_with_options(request, runtime)

    async def describe_shard_db_connection_info_async(
        self,
        request: drds_20171016_models.DescribeShardDbConnectionInfoRequest,
    ) -> drds_20171016_models.DescribeShardDbConnectionInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_shard_db_connection_info_with_options_async(request, runtime)

    def enable_instance_with_options(
        self,
        request: drds_20171016_models.EnableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.EnableInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BackupId'] = request.backup_id
        query['ClientToken'] = request.client_token
        query['DbInstanceClass'] = request.db_instance_class
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EngineVersion'] = request.engine_version
        query['RestoreTime'] = request.restore_time
        query['SourceDbInstId'] = request.source_db_inst_id
        query['SwitchId'] = request.switch_id
        query['VpcId'] = request.vpc_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableInstance',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.EnableInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_instance_with_options_async(
        self,
        request: drds_20171016_models.EnableInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.EnableInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BackupId'] = request.backup_id
        query['ClientToken'] = request.client_token
        query['DbInstanceClass'] = request.db_instance_class
        query['DrdsInstanceId'] = request.drds_instance_id
        query['EngineVersion'] = request.engine_version
        query['RestoreTime'] = request.restore_time
        query['SourceDbInstId'] = request.source_db_inst_id
        query['SwitchId'] = request.switch_id
        query['VpcId'] = request.vpc_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableInstance',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.EnableInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_instance(
        self,
        request: drds_20171016_models.EnableInstanceRequest,
    ) -> drds_20171016_models.EnableInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_with_options(request, runtime)

    async def enable_instance_async(
        self,
        request: drds_20171016_models.EnableInstanceRequest,
    ) -> drds_20171016_models.EnableInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_instance_with_options_async(request, runtime)

    def modify_drds_dbpasswd_with_options(
        self,
        request: drds_20171016_models.ModifyDrdsDBPasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyDrdsDBPasswdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['NewPasswd'] = request.new_passwd
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDrdsDBPasswd',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyDrdsDBPasswdResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_drds_dbpasswd_with_options_async(
        self,
        request: drds_20171016_models.ModifyDrdsDBPasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyDrdsDBPasswdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['NewPasswd'] = request.new_passwd
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDrdsDBPasswd',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyDrdsDBPasswdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_drds_dbpasswd(
        self,
        request: drds_20171016_models.ModifyDrdsDBPasswdRequest,
    ) -> drds_20171016_models.ModifyDrdsDBPasswdResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_dbpasswd_with_options(request, runtime)

    async def modify_drds_dbpasswd_async(
        self,
        request: drds_20171016_models.ModifyDrdsDBPasswdRequest,
    ) -> drds_20171016_models.ModifyDrdsDBPasswdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_drds_dbpasswd_with_options_async(request, runtime)

    def modify_drds_instance_description_with_options(
        self,
        request: drds_20171016_models.ModifyDrdsInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyDrdsInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDrdsInstanceDescription',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyDrdsInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_drds_instance_description_with_options_async(
        self,
        request: drds_20171016_models.ModifyDrdsInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyDrdsInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDrdsInstanceDescription',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyDrdsInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_drds_instance_description(
        self,
        request: drds_20171016_models.ModifyDrdsInstanceDescriptionRequest,
    ) -> drds_20171016_models.ModifyDrdsInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_instance_description_with_options(request, runtime)

    async def modify_drds_instance_description_async(
        self,
        request: drds_20171016_models.ModifyDrdsInstanceDescriptionRequest,
    ) -> drds_20171016_models.ModifyDrdsInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_drds_instance_description_with_options_async(request, runtime)

    def modify_drds_ip_white_list_with_options(
        self,
        request: drds_20171016_models.ModifyDrdsIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyDrdsIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['GroupAttribute'] = request.group_attribute
        query['GroupName'] = request.group_name
        query['IpWhiteList'] = request.ip_white_list
        query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDrdsIpWhiteList',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyDrdsIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_drds_ip_white_list_with_options_async(
        self,
        request: drds_20171016_models.ModifyDrdsIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyDrdsIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['GroupAttribute'] = request.group_attribute
        query['GroupName'] = request.group_name
        query['IpWhiteList'] = request.ip_white_list
        query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDrdsIpWhiteList',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyDrdsIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_drds_ip_white_list(
        self,
        request: drds_20171016_models.ModifyDrdsIpWhiteListRequest,
    ) -> drds_20171016_models.ModifyDrdsIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_ip_white_list_with_options(request, runtime)

    async def modify_drds_ip_white_list_async(
        self,
        request: drds_20171016_models.ModifyDrdsIpWhiteListRequest,
    ) -> drds_20171016_models.ModifyDrdsIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_drds_ip_white_list_with_options_async(request, runtime)

    def modify_full_table_scan_with_options(
        self,
        request: drds_20171016_models.ModifyFullTableScanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyFullTableScanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['FullTableScan'] = request.full_table_scan
        query['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFullTableScan',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyFullTableScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_full_table_scan_with_options_async(
        self,
        request: drds_20171016_models.ModifyFullTableScanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyFullTableScanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['FullTableScan'] = request.full_table_scan
        query['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFullTableScan',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyFullTableScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_full_table_scan(
        self,
        request: drds_20171016_models.ModifyFullTableScanRequest,
    ) -> drds_20171016_models.ModifyFullTableScanResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_full_table_scan_with_options(request, runtime)

    async def modify_full_table_scan_async(
        self,
        request: drds_20171016_models.ModifyFullTableScanRequest,
    ) -> drds_20171016_models.ModifyFullTableScanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_full_table_scan_with_options_async(request, runtime)

    def modify_rds_read_weight_with_options(
        self,
        request: drds_20171016_models.ModifyRdsReadWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyRdsReadWeightResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['InstanceNames'] = request.instance_names
        query['Weights'] = request.weights
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyRdsReadWeight',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyRdsReadWeightResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rds_read_weight_with_options_async(
        self,
        request: drds_20171016_models.ModifyRdsReadWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyRdsReadWeightResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['InstanceNames'] = request.instance_names
        query['Weights'] = request.weights
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyRdsReadWeight',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyRdsReadWeightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rds_read_weight(
        self,
        request: drds_20171016_models.ModifyRdsReadWeightRequest,
    ) -> drds_20171016_models.ModifyRdsReadWeightResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_rds_read_weight_with_options(request, runtime)

    async def modify_rds_read_weight_async(
        self,
        request: drds_20171016_models.ModifyRdsReadWeightRequest,
    ) -> drds_20171016_models.ModifyRdsReadWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_rds_read_weight_with_options_async(request, runtime)

    def modify_read_only_account_password_with_options(
        self,
        request: drds_20171016_models.ModifyReadOnlyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyReadOnlyAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['NewPasswd'] = request.new_passwd
        query['OriginPassword'] = request.origin_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyReadOnlyAccountPassword',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyReadOnlyAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_read_only_account_password_with_options_async(
        self,
        request: drds_20171016_models.ModifyReadOnlyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.ModifyReadOnlyAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        query['NewPasswd'] = request.new_passwd
        query['OriginPassword'] = request.origin_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyReadOnlyAccountPassword',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.ModifyReadOnlyAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_read_only_account_password(
        self,
        request: drds_20171016_models.ModifyReadOnlyAccountPasswordRequest,
    ) -> drds_20171016_models.ModifyReadOnlyAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_read_only_account_password_with_options(request, runtime)

    async def modify_read_only_account_password_async(
        self,
        request: drds_20171016_models.ModifyReadOnlyAccountPasswordRequest,
    ) -> drds_20171016_models.ModifyReadOnlyAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_read_only_account_password_with_options_async(request, runtime)

    def query_instance_info_by_conn_with_options(
        self,
        request: drds_20171016_models.QueryInstanceInfoByConnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.QueryInstanceInfoByConnResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Host'] = request.host
        query['Port'] = request.port
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryInstanceInfoByConn',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.QueryInstanceInfoByConnResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_info_by_conn_with_options_async(
        self,
        request: drds_20171016_models.QueryInstanceInfoByConnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.QueryInstanceInfoByConnResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Host'] = request.host
        query['Port'] = request.port
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryInstanceInfoByConn',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.QueryInstanceInfoByConnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_info_by_conn(
        self,
        request: drds_20171016_models.QueryInstanceInfoByConnRequest,
    ) -> drds_20171016_models.QueryInstanceInfoByConnResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_instance_info_by_conn_with_options(request, runtime)

    async def query_instance_info_by_conn_async(
        self,
        request: drds_20171016_models.QueryInstanceInfoByConnRequest,
    ) -> drds_20171016_models.QueryInstanceInfoByConnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_instance_info_by_conn_with_options_async(request, runtime)

    def remove_drds_instance_with_options(
        self,
        request: drds_20171016_models.RemoveDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.RemoveDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveDrdsInstance',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.RemoveDrdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_drds_instance_with_options_async(
        self,
        request: drds_20171016_models.RemoveDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.RemoveDrdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveDrdsInstance',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.RemoveDrdsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_drds_instance(
        self,
        request: drds_20171016_models.RemoveDrdsInstanceRequest,
    ) -> drds_20171016_models.RemoveDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_instance_with_options(request, runtime)

    async def remove_drds_instance_async(
        self,
        request: drds_20171016_models.RemoveDrdsInstanceRequest,
    ) -> drds_20171016_models.RemoveDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_drds_instance_with_options_async(request, runtime)

    def remove_read_only_account_with_options(
        self,
        request: drds_20171016_models.RemoveReadOnlyAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.RemoveReadOnlyAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveReadOnlyAccount',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.RemoveReadOnlyAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_read_only_account_with_options_async(
        self,
        request: drds_20171016_models.RemoveReadOnlyAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20171016_models.RemoveReadOnlyAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DbName'] = request.db_name
        query['DrdsInstanceId'] = request.drds_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveReadOnlyAccount',
            version='2017-10-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            drds_20171016_models.RemoveReadOnlyAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_read_only_account(
        self,
        request: drds_20171016_models.RemoveReadOnlyAccountRequest,
    ) -> drds_20171016_models.RemoveReadOnlyAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_read_only_account_with_options(request, runtime)

    async def remove_read_only_account_async(
        self,
        request: drds_20171016_models.RemoveReadOnlyAccountRequest,
    ) -> drds_20171016_models.RemoveReadOnlyAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_read_only_account_with_options_async(request, runtime)
