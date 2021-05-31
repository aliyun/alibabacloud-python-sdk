# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_clickhouse20191111 import models as clickhouse_20191111_models
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

    def describe_account_authority_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountAuthorityResponse(),
            self.do_rpcrequest('DescribeAccountAuthority', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_account_authority_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountAuthorityResponse(),
            await self.do_rpcrequest_async('DescribeAccountAuthority', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_account_authority(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_authority_with_options(request, runtime)

    async def describe_account_authority_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_authority_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('CreateServiceLinkedRole', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_linked_role(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def describe_lorne_tasks_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksResponse(),
            self.do_rpcrequest('DescribeLorneTasks', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_lorne_tasks_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksResponse(),
            await self.do_rpcrequest_async('DescribeLorneTasks', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lorne_tasks(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_with_options(request, runtime)

    async def describe_lorne_tasks_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lorne_tasks_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterPerformanceResponse(),
            self.do_rpcrequest('DescribeDBClusterPerformance', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterPerformanceResponse(),
            await self.do_rpcrequest_async('DescribeDBClusterPerformance', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def modify_dbcluster_config_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterConfigResponse(),
            self.do_rpcrequest('ModifyDBClusterConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_config_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterConfigResponse(),
            await self.do_rpcrequest_async('ModifyDBClusterConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_config(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_config_with_options(request, runtime)

    async def modify_dbcluster_config_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_config_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyAccountDescription', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def describe_dbcluster_config_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterConfigResponse(),
            self.do_rpcrequest('DescribeDBClusterConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_config_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterConfigResponse(),
            await self.do_rpcrequest_async('DescribeDBClusterConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_config(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_config_with_options(request, runtime)

    async def describe_dbcluster_config_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_config_with_options_async(request, runtime)

    def describe_ossstorage_with_options(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeOSSStorageResponse(),
            self.do_rpcrequest('DescribeOSSStorage', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ossstorage_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeOSSStorageResponse(),
            await self.do_rpcrequest_async('DescribeOSSStorage', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ossstorage(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ossstorage_with_options(request, runtime)

    async def describe_ossstorage_async(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ossstorage_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateDBInstanceResponse(),
            self.do_rpcrequest('CreateDBInstance', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateDBInstanceResponse(),
            await self.do_rpcrequest_async('CreateDBInstance', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbinstance(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def modify_dbconfig_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBConfigResponse(),
            self.do_rpcrequest('ModifyDBConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbconfig_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBConfigResponse(),
            await self.do_rpcrequest_async('ModifyDBConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbconfig(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbconfig_with_options(request, runtime)

    async def modify_dbconfig_async(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbconfig_with_options_async(request, runtime)

    def create_ports_for_click_house_with_options(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreatePortsForClickHouseResponse(),
            self.do_rpcrequest('CreatePortsForClickHouse', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ports_for_click_house_with_options_async(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreatePortsForClickHouseResponse(),
            await self.do_rpcrequest_async('CreatePortsForClickHouse', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ports_for_click_house(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ports_for_click_house_with_options(request, runtime)

    async def create_ports_for_click_house_async(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ports_for_click_house_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteDBClusterResponse(),
            self.do_rpcrequest('DeleteDBCluster', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteDBClusterResponse(),
            await self.do_rpcrequest_async('DeleteDBCluster', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbcluster(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def describe_slow_log_trend_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSlowLogTrendResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogTrendResponse(),
            self.do_rpcrequest('DescribeSlowLogTrend', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_slow_log_trend_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSlowLogTrendResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogTrendResponse(),
            await self.do_rpcrequest_async('DescribeSlowLogTrend', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_trend(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogTrendRequest,
    ) -> clickhouse_20191111_models.DescribeSlowLogTrendResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_trend_with_options(request, runtime)

    async def describe_slow_log_trend_async(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogTrendRequest,
    ) -> clickhouse_20191111_models.DescribeSlowLogTrendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_trend_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAvailableResourceResponse(),
            self.do_rpcrequest('DescribeAvailableResource', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAvailableResourceResponse(),
            await self.do_rpcrequest_async('DescribeAvailableResource', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(
        self,
        request: clickhouse_20191111_models.DescribeAvailableResourceRequest,
    ) -> clickhouse_20191111_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: clickhouse_20191111_models.DescribeAvailableResourceRequest,
    ) -> clickhouse_20191111_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def release_cluster_public_connection_with_options(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse(),
            self.do_rpcrequest('ReleaseClusterPublicConnection', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_cluster_public_connection_with_options_async(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse(),
            await self.do_rpcrequest_async('ReleaseClusterPublicConnection', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_cluster_public_connection(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    async def release_cluster_public_connection_async(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_public_connection_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountResponse(),
            self.do_rpcrequest('CreateAccount', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountResponse(),
            await self.do_rpcrequest_async('CreateAccount', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def describe_log_store_keys_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLogStoreKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLogStoreKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogStoreKeysResponse(),
            self.do_rpcrequest('DescribeLogStoreKeys', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_log_store_keys_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLogStoreKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLogStoreKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogStoreKeysResponse(),
            await self.do_rpcrequest_async('DescribeLogStoreKeys', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_store_keys(
        self,
        request: clickhouse_20191111_models.DescribeLogStoreKeysRequest,
    ) -> clickhouse_20191111_models.DescribeLogStoreKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_keys_with_options(request, runtime)

    async def describe_log_store_keys_async(
        self,
        request: clickhouse_20191111_models.DescribeLogStoreKeysRequest,
    ) -> clickhouse_20191111_models.DescribeLogStoreKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_store_keys_with_options_async(request, runtime)

    def describe_process_list_with_options(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeProcessListResponse(),
            self.do_rpcrequest('DescribeProcessList', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_process_list_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeProcessListResponse(),
            await self.do_rpcrequest_async('DescribeProcessList', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_process_list(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    async def describe_process_list_async(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_list_with_options_async(request, runtime)

    def create_ossstorage_with_options(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateOSSStorageResponse(),
            self.do_rpcrequest('CreateOSSStorage', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ossstorage_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateOSSStorageResponse(),
            await self.do_rpcrequest_async('CreateOSSStorage', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ossstorage(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ossstorage_with_options(request, runtime)

    async def create_ossstorage_async(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ossstorage_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTablesResponse(),
            self.do_rpcrequest('DescribeTables', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTablesResponse(),
            await self.do_rpcrequest_async('DescribeTables', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tables(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyBackupPolicyResponse(),
            self.do_rpcrequest('ModifyBackupPolicy', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyBackupPolicyResponse(),
            await self.do_rpcrequest_async('ModifyBackupPolicy', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def describe_lorne_tasks_mcount_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMCountResponse(),
            self.do_rpcrequest('DescribeLorneTasksMCount', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_lorne_tasks_mcount_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMCountResponse(),
            await self.do_rpcrequest_async('DescribeLorneTasksMCount', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lorne_tasks_mcount(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMCountRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_mcount_with_options(request, runtime)

    async def describe_lorne_tasks_mcount_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMCountRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lorne_tasks_mcount_with_options_async(request, runtime)

    def describe_dbconfig_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBConfigResponse(),
            self.do_rpcrequest('DescribeDBConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbconfig_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBConfigResponse(),
            await self.do_rpcrequest_async('DescribeDBConfig', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbconfig(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbconfig_with_options(request, runtime)

    async def describe_dbconfig_async(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbconfig_with_options_async(request, runtime)

    def modify_account_authority_with_options(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountAuthorityResponse(),
            self.do_rpcrequest('ModifyAccountAuthority', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_authority_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountAuthorityResponse(),
            await self.do_rpcrequest_async('ModifyAccountAuthority', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_authority(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_authority_with_options(request, runtime)

    async def modify_account_authority_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_authority_with_options_async(request, runtime)

    def describe_lorne_log_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLorneLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneLogResponse(),
            self.do_rpcrequest('DescribeLorneLog', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_lorne_log_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneLogResponse(),
            await self.do_rpcrequest_async('DescribeLorneLog', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lorne_log(
        self,
        request: clickhouse_20191111_models.DescribeLorneLogRequest,
    ) -> clickhouse_20191111_models.DescribeLorneLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_log_with_options(request, runtime)

    async def describe_lorne_log_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneLogRequest,
    ) -> clickhouse_20191111_models.DescribeLorneLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lorne_log_with_options_async(request, runtime)

    def describe_all_data_sources_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourcesResponse(),
            self.do_rpcrequest('DescribeAllDataSources', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_all_data_sources_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourcesResponse(),
            await self.do_rpcrequest_async('DescribeAllDataSources', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_data_sources(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_sources_with_options(request, runtime)

    async def describe_all_data_sources_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_data_sources_with_options_async(request, runtime)

    def operate_lorne_task_status_with_options(
        self,
        request: clickhouse_20191111_models.OperateLorneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.OperateLorneTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLorneTaskStatusResponse(),
            self.do_rpcrequest('OperateLorneTaskStatus', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def operate_lorne_task_status_with_options_async(
        self,
        request: clickhouse_20191111_models.OperateLorneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.OperateLorneTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLorneTaskStatusResponse(),
            await self.do_rpcrequest_async('OperateLorneTaskStatus', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def operate_lorne_task_status(
        self,
        request: clickhouse_20191111_models.OperateLorneTaskStatusRequest,
    ) -> clickhouse_20191111_models.OperateLorneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_lorne_task_status_with_options(request, runtime)

    async def operate_lorne_task_status_async(
        self,
        request: clickhouse_20191111_models.OperateLorneTaskStatusRequest,
    ) -> clickhouse_20191111_models.OperateLorneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_lorne_task_status_with_options_async(request, runtime)

    def describe_dbcluster_attribute_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAttributeResponse(),
            self.do_rpcrequest('DescribeDBClusterAttribute', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_attribute_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAttributeResponse(),
            await self.do_rpcrequest_async('DescribeDBClusterAttribute', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_attribute(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    async def describe_dbcluster_attribute_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_attribute_with_options_async(request, runtime)

    def delete_lorne_task_with_options(
        self,
        request: clickhouse_20191111_models.DeleteLorneTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteLorneTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteLorneTaskResponse(),
            self.do_rpcrequest('DeleteLorneTask', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_lorne_task_with_options_async(
        self,
        request: clickhouse_20191111_models.DeleteLorneTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteLorneTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteLorneTaskResponse(),
            await self.do_rpcrequest_async('DeleteLorneTask', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_lorne_task(
        self,
        request: clickhouse_20191111_models.DeleteLorneTaskRequest,
    ) -> clickhouse_20191111_models.DeleteLorneTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_lorne_task_with_options(request, runtime)

    async def delete_lorne_task_async(
        self,
        request: clickhouse_20191111_models.DeleteLorneTaskRequest,
    ) -> clickhouse_20191111_models.DeleteLorneTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_lorne_task_with_options_async(request, runtime)

    def describe_dbclusters_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClustersResponse(),
            self.do_rpcrequest('DescribeDBClusters', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbclusters_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClustersResponse(),
            await self.do_rpcrequest_async('DescribeDBClusters', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbclusters(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    async def describe_dbclusters_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbclusters_with_options_async(request, runtime)

    def operate_log_hub_with_options(
        self,
        request: clickhouse_20191111_models.OperateLogHubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.OperateLogHubResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLogHubResponse(),
            self.do_rpcrequest('OperateLogHub', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def operate_log_hub_with_options_async(
        self,
        request: clickhouse_20191111_models.OperateLogHubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.OperateLogHubResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLogHubResponse(),
            await self.do_rpcrequest_async('OperateLogHub', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def operate_log_hub(
        self,
        request: clickhouse_20191111_models.OperateLogHubRequest,
    ) -> clickhouse_20191111_models.OperateLogHubResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_log_hub_with_options(request, runtime)

    async def operate_log_hub_async(
        self,
        request: clickhouse_20191111_models.OperateLogHubRequest,
    ) -> clickhouse_20191111_models.OperateLogHubResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_log_hub_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckServiceLinkedRoleResponse(),
            self.do_rpcrequest('CheckServiceLinkedRole', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('CheckServiceLinkedRole', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_service_linked_role(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def create_backup_policy_with_options(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateBackupPolicyResponse(),
            self.do_rpcrequest('CreateBackupPolicy', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_policy_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateBackupPolicyResponse(),
            await self.do_rpcrequest_async('CreateBackupPolicy', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup_policy(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_policy_with_options(request, runtime)

    async def create_backup_policy_async(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_policy_with_options_async(request, runtime)

    def describe_schemas_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSchemasResponse(),
            self.do_rpcrequest('DescribeSchemas', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_schemas_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSchemasResponse(),
            await self.do_rpcrequest_async('DescribeSchemas', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_schemas(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_schemas_with_options(request, runtime)

    async def describe_schemas_async(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_schemas_with_options_async(request, runtime)

    def kill_process_with_options(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.KillProcessResponse(),
            self.do_rpcrequest('KillProcess', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def kill_process_with_options_async(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.KillProcessResponse(),
            await self.do_rpcrequest_async('KillProcess', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kill_process(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    async def kill_process_async(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_process_with_options_async(request, runtime)

    def modify_dbcluster_maintain_time_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse(),
            self.do_rpcrequest('ModifyDBClusterMaintainTime', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_maintain_time_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse(),
            await self.do_rpcrequest_async('ModifyDBClusterMaintainTime', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_maintain_time(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    async def modify_dbcluster_maintain_time_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_maintain_time_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupsResponse(),
            self.do_rpcrequest('DescribeBackups', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupsResponse(),
            await self.do_rpcrequest_async('DescribeBackups', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_dbcluster_access_white_list_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse(),
            self.do_rpcrequest('DescribeDBClusterAccessWhiteList', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_access_white_list_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse(),
            await self.do_rpcrequest_async('DescribeDBClusterAccessWhiteList', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_access_white_list(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_access_white_list_with_options(request, runtime)

    async def describe_dbcluster_access_white_list_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_access_white_list_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def modify_dbcluster_description_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterDescriptionResponse(),
            self.do_rpcrequest('ModifyDBClusterDescription', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_description_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyDBClusterDescription', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_description(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    async def modify_dbcluster_description_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_description_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteAccountResponse(),
            self.do_rpcrequest('DeleteAccount', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteAccountResponse(),
            await self.do_rpcrequest_async('DeleteAccount', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_account(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogRecordsResponse(),
            self.do_rpcrequest('DescribeSlowLogRecords', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogRecordsResponse(),
            await self.do_rpcrequest_async('DescribeSlowLogRecords', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_columns_with_options(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeColumnsResponse(),
            self.do_rpcrequest('DescribeColumns', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_columns_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeColumnsResponse(),
            await self.do_rpcrequest_async('DescribeColumns', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_columns(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    async def describe_columns_async(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_columns_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ResetAccountPasswordResponse(),
            self.do_rpcrequest('ResetAccountPassword', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ResetAccountPasswordResponse(),
            await self.do_rpcrequest_async('ResetAccountPassword', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_password(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountsResponse(),
            self.do_rpcrequest('DescribeAccounts', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountsResponse(),
            await self.do_rpcrequest_async('DescribeAccounts', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_lorne_tasks_metrics_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMetricsResponse(),
            self.do_rpcrequest('DescribeLorneTasksMetrics', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_lorne_tasks_metrics_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMetricsResponse(),
            await self.do_rpcrequest_async('DescribeLorneTasksMetrics', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lorne_tasks_metrics(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMetricsRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_metrics_with_options(request, runtime)

    async def describe_lorne_tasks_metrics_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMetricsRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lorne_tasks_metrics_with_options_async(request, runtime)

    def check_scale_out_balanced_with_options(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckScaleOutBalancedResponse(),
            self.do_rpcrequest('CheckScaleOutBalanced', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_scale_out_balanced_with_options_async(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckScaleOutBalancedResponse(),
            await self.do_rpcrequest_async('CheckScaleOutBalanced', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_scale_out_balanced(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_scale_out_balanced_with_options(request, runtime)

    async def check_scale_out_balanced_async(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_scale_out_balanced_with_options_async(request, runtime)

    def allocate_cluster_public_connection_with_options(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.AllocateClusterPublicConnectionResponse(),
            self.do_rpcrequest('AllocateClusterPublicConnection', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_cluster_public_connection_with_options_async(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.AllocateClusterPublicConnectionResponse(),
            await self.do_rpcrequest_async('AllocateClusterPublicConnection', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_cluster_public_connection(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    async def allocate_cluster_public_connection_async(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_cluster_public_connection_with_options_async(request, runtime)

    def describe_all_data_source_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourceResponse(),
            self.do_rpcrequest('DescribeAllDataSource', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_all_data_source_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourceResponse(),
            await self.do_rpcrequest_async('DescribeAllDataSource', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_data_source(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    async def describe_all_data_source_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_data_source_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupPolicyResponse(),
            await self.do_rpcrequest_async('DescribeBackupPolicy', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_dbcluster_net_info_items_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse(),
            self.do_rpcrequest('DescribeDBClusterNetInfoItems', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_net_info_items_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse(),
            await self.do_rpcrequest_async('DescribeDBClusterNetInfoItems', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_net_info_items(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_net_info_items_with_options(request, runtime)

    async def describe_dbcluster_net_info_items_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_net_info_items_with_options_async(request, runtime)

    def describe_loghub_detail_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLoghubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLoghubDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLoghubDetailResponse(),
            self.do_rpcrequest('DescribeLoghubDetail', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_loghub_detail_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLoghubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLoghubDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLoghubDetailResponse(),
            await self.do_rpcrequest_async('DescribeLoghubDetail', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_loghub_detail(
        self,
        request: clickhouse_20191111_models.DescribeLoghubDetailRequest,
    ) -> clickhouse_20191111_models.DescribeLoghubDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_loghub_detail_with_options(request, runtime)

    async def describe_loghub_detail_async(
        self,
        request: clickhouse_20191111_models.DescribeLoghubDetailRequest,
    ) -> clickhouse_20191111_models.DescribeLoghubDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_loghub_detail_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterResponse(),
            self.do_rpcrequest('ModifyDBCluster', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterResponse(),
            await self.do_rpcrequest_async('ModifyDBCluster', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    async def modify_dbcluster_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_with_options_async(request, runtime)

    def describe_log_hub_attribute_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLogHubAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLogHubAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogHubAttributeResponse(),
            self.do_rpcrequest('DescribeLogHubAttribute', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_log_hub_attribute_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLogHubAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLogHubAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogHubAttributeResponse(),
            await self.do_rpcrequest_async('DescribeLogHubAttribute', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_hub_attribute(
        self,
        request: clickhouse_20191111_models.DescribeLogHubAttributeRequest,
    ) -> clickhouse_20191111_models.DescribeLogHubAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_hub_attribute_with_options(request, runtime)

    async def describe_log_hub_attribute_async(
        self,
        request: clickhouse_20191111_models.DescribeLogHubAttributeRequest,
    ) -> clickhouse_20191111_models.DescribeLogHubAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_hub_attribute_with_options_async(request, runtime)

    def modify_dbcluster_access_white_list_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse(),
            self.do_rpcrequest('ModifyDBClusterAccessWhiteList', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_access_white_list_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse(),
            await self.do_rpcrequest_async('ModifyDBClusterAccessWhiteList', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_access_white_list(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_access_white_list_with_options(request, runtime)

    async def modify_dbcluster_access_white_list_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_access_white_list_with_options_async(request, runtime)

    def create_account_and_authority_with_options(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountAndAuthorityResponse(),
            self.do_rpcrequest('CreateAccountAndAuthority', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_account_and_authority_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountAndAuthorityResponse(),
            await self.do_rpcrequest_async('CreateAccountAndAuthority', '2019-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account_and_authority(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_and_authority_with_options(request, runtime)

    async def create_account_and_authority_async(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_and_authority_with_options_async(request, runtime)
