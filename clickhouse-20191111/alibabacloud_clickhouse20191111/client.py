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

    def allocate_cluster_public_connection_with_options(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        """
        @summary Creates a public endpoint for an ApsaraDB for ClickHouse cluster.
        
        @param request: AllocateClusterPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateClusterPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.AllocateClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cluster_public_connection_with_options_async(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        """
        @summary Creates a public endpoint for an ApsaraDB for ClickHouse cluster.
        
        @param request: AllocateClusterPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateClusterPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.AllocateClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cluster_public_connection(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        """
        @summary Creates a public endpoint for an ApsaraDB for ClickHouse cluster.
        
        @param request: AllocateClusterPublicConnectionRequest
        @return: AllocateClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    async def allocate_cluster_public_connection_async(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        """
        @summary Creates a public endpoint for an ApsaraDB for ClickHouse cluster.
        
        @param request: AllocateClusterPublicConnectionRequest
        @return: AllocateClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_cluster_public_connection_with_options_async(request, runtime)

    def check_clickhouse_to_rdswith_options(
        self,
        request: clickhouse_20191111_models.CheckClickhouseToRDSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckClickhouseToRDSResponse:
        """
        @summary Checks the connectivity between an ApsaraDB for ClickHouse cluster and an ApsaraDB RDS for MySQL instance.
        
        @param request: CheckClickhouseToRDSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckClickhouseToRDSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not UtilClient.is_unset(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not UtilClient.is_unset(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rds_id):
            query['RdsId'] = request.rds_id
        if not UtilClient.is_unset(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not UtilClient.is_unset(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not UtilClient.is_unset(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not UtilClient.is_unset(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not UtilClient.is_unset(request.rds_vpc_url):
            query['RdsVpcUrl'] = request.rds_vpc_url
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckClickhouseToRDS',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckClickhouseToRDSResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_clickhouse_to_rdswith_options_async(
        self,
        request: clickhouse_20191111_models.CheckClickhouseToRDSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckClickhouseToRDSResponse:
        """
        @summary Checks the connectivity between an ApsaraDB for ClickHouse cluster and an ApsaraDB RDS for MySQL instance.
        
        @param request: CheckClickhouseToRDSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckClickhouseToRDSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not UtilClient.is_unset(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not UtilClient.is_unset(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rds_id):
            query['RdsId'] = request.rds_id
        if not UtilClient.is_unset(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not UtilClient.is_unset(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not UtilClient.is_unset(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not UtilClient.is_unset(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not UtilClient.is_unset(request.rds_vpc_url):
            query['RdsVpcUrl'] = request.rds_vpc_url
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckClickhouseToRDS',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckClickhouseToRDSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_clickhouse_to_rds(
        self,
        request: clickhouse_20191111_models.CheckClickhouseToRDSRequest,
    ) -> clickhouse_20191111_models.CheckClickhouseToRDSResponse:
        """
        @summary Checks the connectivity between an ApsaraDB for ClickHouse cluster and an ApsaraDB RDS for MySQL instance.
        
        @param request: CheckClickhouseToRDSRequest
        @return: CheckClickhouseToRDSResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_clickhouse_to_rdswith_options(request, runtime)

    async def check_clickhouse_to_rds_async(
        self,
        request: clickhouse_20191111_models.CheckClickhouseToRDSRequest,
    ) -> clickhouse_20191111_models.CheckClickhouseToRDSResponse:
        """
        @summary Checks the connectivity between an ApsaraDB for ClickHouse cluster and an ApsaraDB RDS for MySQL instance.
        
        @param request: CheckClickhouseToRDSRequest
        @return: CheckClickhouseToRDSResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_clickhouse_to_rdswith_options_async(request, runtime)

    def check_modify_config_need_restart_with_options(
        self,
        request: clickhouse_20191111_models.CheckModifyConfigNeedRestartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckModifyConfigNeedRestartResponse:
        """
        @summary Queries whether an ApsaraDB for ClickHouse cluster needs to be restarted after you change the values of the configuration parameters in XML mode.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: CheckModifyConfigNeedRestartRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckModifyConfigNeedRestartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckModifyConfigNeedRestart',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckModifyConfigNeedRestartResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_modify_config_need_restart_with_options_async(
        self,
        request: clickhouse_20191111_models.CheckModifyConfigNeedRestartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckModifyConfigNeedRestartResponse:
        """
        @summary Queries whether an ApsaraDB for ClickHouse cluster needs to be restarted after you change the values of the configuration parameters in XML mode.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: CheckModifyConfigNeedRestartRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckModifyConfigNeedRestartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckModifyConfigNeedRestart',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckModifyConfigNeedRestartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_modify_config_need_restart(
        self,
        request: clickhouse_20191111_models.CheckModifyConfigNeedRestartRequest,
    ) -> clickhouse_20191111_models.CheckModifyConfigNeedRestartResponse:
        """
        @summary Queries whether an ApsaraDB for ClickHouse cluster needs to be restarted after you change the values of the configuration parameters in XML mode.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: CheckModifyConfigNeedRestartRequest
        @return: CheckModifyConfigNeedRestartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_modify_config_need_restart_with_options(request, runtime)

    async def check_modify_config_need_restart_async(
        self,
        request: clickhouse_20191111_models.CheckModifyConfigNeedRestartRequest,
    ) -> clickhouse_20191111_models.CheckModifyConfigNeedRestartResponse:
        """
        @summary Queries whether an ApsaraDB for ClickHouse cluster needs to be restarted after you change the values of the configuration parameters in XML mode.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: CheckModifyConfigNeedRestartRequest
        @return: CheckModifyConfigNeedRestartResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_modify_config_need_restart_with_options_async(request, runtime)

    def check_monitor_alert_with_options(
        self,
        request: clickhouse_20191111_models.CheckMonitorAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckMonitorAlertResponse:
        """
        @summary Checks whether the monitoring and alerting feature that is provided by Application Real-Time Monitoring Service (ARMS) is enabled for an ApsaraDB for ClickHouse cluster.
        
        @param request: CheckMonitorAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckMonitorAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMonitorAlert',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckMonitorAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_monitor_alert_with_options_async(
        self,
        request: clickhouse_20191111_models.CheckMonitorAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckMonitorAlertResponse:
        """
        @summary Checks whether the monitoring and alerting feature that is provided by Application Real-Time Monitoring Service (ARMS) is enabled for an ApsaraDB for ClickHouse cluster.
        
        @param request: CheckMonitorAlertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckMonitorAlertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMonitorAlert',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckMonitorAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_monitor_alert(
        self,
        request: clickhouse_20191111_models.CheckMonitorAlertRequest,
    ) -> clickhouse_20191111_models.CheckMonitorAlertResponse:
        """
        @summary Checks whether the monitoring and alerting feature that is provided by Application Real-Time Monitoring Service (ARMS) is enabled for an ApsaraDB for ClickHouse cluster.
        
        @param request: CheckMonitorAlertRequest
        @return: CheckMonitorAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_monitor_alert_with_options(request, runtime)

    async def check_monitor_alert_async(
        self,
        request: clickhouse_20191111_models.CheckMonitorAlertRequest,
    ) -> clickhouse_20191111_models.CheckMonitorAlertResponse:
        """
        @summary Checks whether the monitoring and alerting feature that is provided by Application Real-Time Monitoring Service (ARMS) is enabled for an ApsaraDB for ClickHouse cluster.
        
        @param request: CheckMonitorAlertRequest
        @return: CheckMonitorAlertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_monitor_alert_with_options_async(request, runtime)

    def check_scale_out_balanced_with_options(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        """
        @summary Performs migration and scale-out detection on an ApsaraDB for ClickHouse cluster.
        
        @param request: CheckScaleOutBalancedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckScaleOutBalancedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckScaleOutBalanced',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckScaleOutBalancedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_scale_out_balanced_with_options_async(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        """
        @summary Performs migration and scale-out detection on an ApsaraDB for ClickHouse cluster.
        
        @param request: CheckScaleOutBalancedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckScaleOutBalancedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckScaleOutBalanced',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckScaleOutBalancedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_scale_out_balanced(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        """
        @summary Performs migration and scale-out detection on an ApsaraDB for ClickHouse cluster.
        
        @param request: CheckScaleOutBalancedRequest
        @return: CheckScaleOutBalancedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_scale_out_balanced_with_options(request, runtime)

    async def check_scale_out_balanced_async(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        """
        @summary Performs migration and scale-out detection on an ApsaraDB for ClickHouse cluster.
        
        @param request: CheckScaleOutBalancedRequest
        @return: CheckScaleOutBalancedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_scale_out_balanced_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        """
        @summary Queries the service-linked role of ApsaraDB for ClickHouse.
        
        @param request: CheckServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        """
        @summary Queries the service-linked role of ApsaraDB for ClickHouse.
        
        @param request: CheckServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        """
        @summary Queries the service-linked role of ApsaraDB for ClickHouse.
        
        @param request: CheckServiceLinkedRoleRequest
        @return: CheckServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        """
        @summary Queries the service-linked role of ApsaraDB for ClickHouse.
        
        @param request: CheckServiceLinkedRoleRequest
        @return: CheckServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        """
        @summary Creates a database account for an ApsaraDB for ClickHouse cluster.
        
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        """
        @summary Creates a database account for an ApsaraDB for ClickHouse cluster.
        
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        """
        @summary Creates a database account for an ApsaraDB for ClickHouse cluster.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        """
        @summary Creates a database account for an ApsaraDB for ClickHouse cluster.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_account_and_authority_with_options(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        """
        @summary Creates an account and grants permissions to the account.
        
        @param request: CreateAccountAndAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountAndAuthorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.allow_databases):
            query['AllowDatabases'] = request.allow_databases
        if not UtilClient.is_unset(request.allow_dictionaries):
            query['AllowDictionaries'] = request.allow_dictionaries
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ddl_authority):
            query['DdlAuthority'] = request.ddl_authority
        if not UtilClient.is_unset(request.dml_authority):
            query['DmlAuthority'] = request.dml_authority
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.total_databases):
            query['TotalDatabases'] = request.total_databases
        if not UtilClient.is_unset(request.total_dictionaries):
            query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccountAndAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountAndAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_and_authority_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        """
        @summary Creates an account and grants permissions to the account.
        
        @param request: CreateAccountAndAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountAndAuthorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.allow_databases):
            query['AllowDatabases'] = request.allow_databases
        if not UtilClient.is_unset(request.allow_dictionaries):
            query['AllowDictionaries'] = request.allow_dictionaries
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ddl_authority):
            query['DdlAuthority'] = request.ddl_authority
        if not UtilClient.is_unset(request.dml_authority):
            query['DmlAuthority'] = request.dml_authority
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.total_databases):
            query['TotalDatabases'] = request.total_databases
        if not UtilClient.is_unset(request.total_dictionaries):
            query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccountAndAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountAndAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account_and_authority(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        """
        @summary Creates an account and grants permissions to the account.
        
        @param request: CreateAccountAndAuthorityRequest
        @return: CreateAccountAndAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_and_authority_with_options(request, runtime)

    async def create_account_and_authority_async(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        """
        @summary Creates an account and grants permissions to the account.
        
        @param request: CreateAccountAndAuthorityRequest
        @return: CreateAccountAndAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_and_authority_with_options_async(request, runtime)

    def create_backup_policy_with_options(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        """
        @summary Creates a backup policy.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: CreateBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_policy_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        """
        @summary Creates a backup policy.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: CreateBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_policy(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        """
        @summary Creates a backup policy.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: CreateBackupPolicyRequest
        @return: CreateBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_policy_with_options(request, runtime)

    async def create_backup_policy_async(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        """
        @summary Creates a backup policy.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: CreateBackupPolicyRequest
        @return: CreateBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_policy_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse cluster.
        
        @description Before you call this operation, make sure that you are familiar with the billing methods and [pricing](https://help.aliyun.com/document_detail/167450.html) of ApsaraDB for ClickHouse.
        
        @param request: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetID'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not UtilClient.is_unset(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not UtilClient.is_unset(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not UtilClient.is_unset(request.db_node_storage_type):
            query['DbNodeStorageType'] = request.db_node_storage_type
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_dbcluster_id):
            query['SourceDBClusterId'] = request.source_dbcluster_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_bak):
            query['VSwitchBak'] = request.v_switch_bak
        if not UtilClient.is_unset(request.v_switch_bak_2):
            query['VSwitchBak2'] = request.v_switch_bak_2
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zond_id_bak_2):
            query['ZondIdBak2'] = request.zond_id_bak_2
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_id_bak):
            query['ZoneIdBak'] = request.zone_id_bak
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse cluster.
        
        @description Before you call this operation, make sure that you are familiar with the billing methods and [pricing](https://help.aliyun.com/document_detail/167450.html) of ApsaraDB for ClickHouse.
        
        @param request: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetID'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not UtilClient.is_unset(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not UtilClient.is_unset(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not UtilClient.is_unset(request.db_node_storage_type):
            query['DbNodeStorageType'] = request.db_node_storage_type
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_dbcluster_id):
            query['SourceDBClusterId'] = request.source_dbcluster_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_bak):
            query['VSwitchBak'] = request.v_switch_bak
        if not UtilClient.is_unset(request.v_switch_bak_2):
            query['VSwitchBak2'] = request.v_switch_bak_2
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zond_id_bak_2):
            query['ZondIdBak2'] = request.zond_id_bak_2
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_id_bak):
            query['ZoneIdBak'] = request.zone_id_bak
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse cluster.
        
        @description Before you call this operation, make sure that you are familiar with the billing methods and [pricing](https://help.aliyun.com/document_detail/167450.html) of ApsaraDB for ClickHouse.
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse cluster.
        
        @description Before you call this operation, make sure that you are familiar with the billing methods and [pricing](https://help.aliyun.com/document_detail/167450.html) of ApsaraDB for ClickHouse.
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_monitor_data_report_with_options(
        self,
        request: clickhouse_20191111_models.CreateMonitorDataReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateMonitorDataReportResponse:
        """
        @summary Creates a monitoring data report for an ApsaraDB for ClickHouse cluster.
        
        @param request: CreateMonitorDataReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitorDataReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorDataReport',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateMonitorDataReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_data_report_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateMonitorDataReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateMonitorDataReportResponse:
        """
        @summary Creates a monitoring data report for an ApsaraDB for ClickHouse cluster.
        
        @param request: CreateMonitorDataReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMonitorDataReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorDataReport',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateMonitorDataReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_data_report(
        self,
        request: clickhouse_20191111_models.CreateMonitorDataReportRequest,
    ) -> clickhouse_20191111_models.CreateMonitorDataReportResponse:
        """
        @summary Creates a monitoring data report for an ApsaraDB for ClickHouse cluster.
        
        @param request: CreateMonitorDataReportRequest
        @return: CreateMonitorDataReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_data_report_with_options(request, runtime)

    async def create_monitor_data_report_async(
        self,
        request: clickhouse_20191111_models.CreateMonitorDataReportRequest,
    ) -> clickhouse_20191111_models.CreateMonitorDataReportResponse:
        """
        @summary Creates a monitoring data report for an ApsaraDB for ClickHouse cluster.
        
        @param request: CreateMonitorDataReportRequest
        @return: CreateMonitorDataReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_data_report_with_options_async(request, runtime)

    def create_ossstorage_with_options(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        """
        @summary Creates a storage task for cold data.
        
        @description Only an ApsaraDB for ClickHouse cluster of V20.8 or later supports tiered storage of hot data and cold data. If your data is in an ApsaraDB for ClickHouse cluster of a version earlier than V20.8 and you want to use tiered storage of hot data and cold data to store the data, you can migrate the data to an ApsaraDB for ClickHouse cluster of V20.8 or later and use tiered storage of hot data and cold data. For more information about how to migrate data between ApsaraDB for ClickHouse clusters, see [Migrate data between ApsaraDB for ClickHouse clusters](https://help.aliyun.com/document_detail/276926.html).
        
        @param request: CreateOSSStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOSSStorageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOSSStorage',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateOSSStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ossstorage_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        """
        @summary Creates a storage task for cold data.
        
        @description Only an ApsaraDB for ClickHouse cluster of V20.8 or later supports tiered storage of hot data and cold data. If your data is in an ApsaraDB for ClickHouse cluster of a version earlier than V20.8 and you want to use tiered storage of hot data and cold data to store the data, you can migrate the data to an ApsaraDB for ClickHouse cluster of V20.8 or later and use tiered storage of hot data and cold data. For more information about how to migrate data between ApsaraDB for ClickHouse clusters, see [Migrate data between ApsaraDB for ClickHouse clusters](https://help.aliyun.com/document_detail/276926.html).
        
        @param request: CreateOSSStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOSSStorageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOSSStorage',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateOSSStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ossstorage(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        """
        @summary Creates a storage task for cold data.
        
        @description Only an ApsaraDB for ClickHouse cluster of V20.8 or later supports tiered storage of hot data and cold data. If your data is in an ApsaraDB for ClickHouse cluster of a version earlier than V20.8 and you want to use tiered storage of hot data and cold data to store the data, you can migrate the data to an ApsaraDB for ClickHouse cluster of V20.8 or later and use tiered storage of hot data and cold data. For more information about how to migrate data between ApsaraDB for ClickHouse clusters, see [Migrate data between ApsaraDB for ClickHouse clusters](https://help.aliyun.com/document_detail/276926.html).
        
        @param request: CreateOSSStorageRequest
        @return: CreateOSSStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ossstorage_with_options(request, runtime)

    async def create_ossstorage_async(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        """
        @summary Creates a storage task for cold data.
        
        @description Only an ApsaraDB for ClickHouse cluster of V20.8 or later supports tiered storage of hot data and cold data. If your data is in an ApsaraDB for ClickHouse cluster of a version earlier than V20.8 and you want to use tiered storage of hot data and cold data to store the data, you can migrate the data to an ApsaraDB for ClickHouse cluster of V20.8 or later and use tiered storage of hot data and cold data. For more information about how to migrate data between ApsaraDB for ClickHouse clusters, see [Migrate data between ApsaraDB for ClickHouse clusters](https://help.aliyun.com/document_detail/276926.html).
        
        @param request: CreateOSSStorageRequest
        @return: CreateOSSStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ossstorage_with_options_async(request, runtime)

    def create_ports_for_click_house_with_options(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        """
        @summary Enables the MySQL port for an ApsaraDB for ClickHouse cluster.
        
        @description >  For an ApsaraDB for ClickHouse cluster of V20.8 or later that was created before December 1, 2021, you must manually enable the MySQL port. For an ApsaraDB for ClickHouse cluster of V20.8 or later that was created after December 1, 2021, the MySQL port is automatically enabled.
        
        @param request: CreatePortsForClickHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePortsForClickHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_type):
            query['PortType'] = request.port_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePortsForClickHouse',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreatePortsForClickHouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ports_for_click_house_with_options_async(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        """
        @summary Enables the MySQL port for an ApsaraDB for ClickHouse cluster.
        
        @description >  For an ApsaraDB for ClickHouse cluster of V20.8 or later that was created before December 1, 2021, you must manually enable the MySQL port. For an ApsaraDB for ClickHouse cluster of V20.8 or later that was created after December 1, 2021, the MySQL port is automatically enabled.
        
        @param request: CreatePortsForClickHouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePortsForClickHouseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_type):
            query['PortType'] = request.port_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePortsForClickHouse',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreatePortsForClickHouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ports_for_click_house(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        """
        @summary Enables the MySQL port for an ApsaraDB for ClickHouse cluster.
        
        @description >  For an ApsaraDB for ClickHouse cluster of V20.8 or later that was created before December 1, 2021, you must manually enable the MySQL port. For an ApsaraDB for ClickHouse cluster of V20.8 or later that was created after December 1, 2021, the MySQL port is automatically enabled.
        
        @param request: CreatePortsForClickHouseRequest
        @return: CreatePortsForClickHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ports_for_click_house_with_options(request, runtime)

    async def create_ports_for_click_house_async(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        """
        @summary Enables the MySQL port for an ApsaraDB for ClickHouse cluster.
        
        @description >  For an ApsaraDB for ClickHouse cluster of V20.8 or later that was created before December 1, 2021, you must manually enable the MySQL port. For an ApsaraDB for ClickHouse cluster of V20.8 or later that was created after December 1, 2021, the MySQL port is automatically enabled.
        
        @param request: CreatePortsForClickHouseRequest
        @return: CreatePortsForClickHouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ports_for_click_house_with_options_async(request, runtime)

    def create_rdsto_clickhouse_db_with_options(
        self,
        request: clickhouse_20191111_models.CreateRDSToClickhouseDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateRDSToClickhouseDbResponse:
        """
        @summary Creates a task to synchronize data from an ApsaraDB RDS for MySQL instance to an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is only applicable to ApsaraDB for ClickHouse clusters.
        
        @param request: CreateRDSToClickhouseDbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRDSToClickhouseDbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not UtilClient.is_unset(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not UtilClient.is_unset(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.limit_upper):
            query['LimitUpper'] = request.limit_upper
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rds_id):
            query['RdsId'] = request.rds_id
        if not UtilClient.is_unset(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not UtilClient.is_unset(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not UtilClient.is_unset(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not UtilClient.is_unset(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not UtilClient.is_unset(request.rds_vpc_url):
            query['RdsVpcUrl'] = request.rds_vpc_url
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.skip_unsupported):
            query['SkipUnsupported'] = request.skip_unsupported
        if not UtilClient.is_unset(request.syn_db_tables):
            query['SynDbTables'] = request.syn_db_tables
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRDSToClickhouseDb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateRDSToClickhouseDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rdsto_clickhouse_db_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateRDSToClickhouseDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateRDSToClickhouseDbResponse:
        """
        @summary Creates a task to synchronize data from an ApsaraDB RDS for MySQL instance to an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is only applicable to ApsaraDB for ClickHouse clusters.
        
        @param request: CreateRDSToClickhouseDbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRDSToClickhouseDbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not UtilClient.is_unset(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not UtilClient.is_unset(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.limit_upper):
            query['LimitUpper'] = request.limit_upper
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rds_id):
            query['RdsId'] = request.rds_id
        if not UtilClient.is_unset(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not UtilClient.is_unset(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not UtilClient.is_unset(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not UtilClient.is_unset(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not UtilClient.is_unset(request.rds_vpc_url):
            query['RdsVpcUrl'] = request.rds_vpc_url
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.skip_unsupported):
            query['SkipUnsupported'] = request.skip_unsupported
        if not UtilClient.is_unset(request.syn_db_tables):
            query['SynDbTables'] = request.syn_db_tables
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRDSToClickhouseDb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateRDSToClickhouseDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rdsto_clickhouse_db(
        self,
        request: clickhouse_20191111_models.CreateRDSToClickhouseDbRequest,
    ) -> clickhouse_20191111_models.CreateRDSToClickhouseDbResponse:
        """
        @summary Creates a task to synchronize data from an ApsaraDB RDS for MySQL instance to an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is only applicable to ApsaraDB for ClickHouse clusters.
        
        @param request: CreateRDSToClickhouseDbRequest
        @return: CreateRDSToClickhouseDbResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rdsto_clickhouse_db_with_options(request, runtime)

    async def create_rdsto_clickhouse_db_async(
        self,
        request: clickhouse_20191111_models.CreateRDSToClickhouseDbRequest,
    ) -> clickhouse_20191111_models.CreateRDSToClickhouseDbResponse:
        """
        @summary Creates a task to synchronize data from an ApsaraDB RDS for MySQL instance to an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is only applicable to ApsaraDB for ClickHouse clusters.
        
        @param request: CreateRDSToClickhouseDbRequest
        @return: CreateRDSToClickhouseDbResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rdsto_clickhouse_db_with_options_async(request, runtime)

    def create_sqlaccount_with_options(
        self,
        request: clickhouse_20191111_models.CreateSQLAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateSQLAccountResponse:
        """
        @summary Creates a privileged account or a standard account for an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is applicable only to ApsaraDB for ClickHouse clusters of V20.8 or later that were created after December 1, 2021,
        
        @param request: CreateSQLAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSQLAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSQLAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateSQLAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sqlaccount_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateSQLAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateSQLAccountResponse:
        """
        @summary Creates a privileged account or a standard account for an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is applicable only to ApsaraDB for ClickHouse clusters of V20.8 or later that were created after December 1, 2021,
        
        @param request: CreateSQLAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSQLAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSQLAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateSQLAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sqlaccount(
        self,
        request: clickhouse_20191111_models.CreateSQLAccountRequest,
    ) -> clickhouse_20191111_models.CreateSQLAccountResponse:
        """
        @summary Creates a privileged account or a standard account for an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is applicable only to ApsaraDB for ClickHouse clusters of V20.8 or later that were created after December 1, 2021,
        
        @param request: CreateSQLAccountRequest
        @return: CreateSQLAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sqlaccount_with_options(request, runtime)

    async def create_sqlaccount_async(
        self,
        request: clickhouse_20191111_models.CreateSQLAccountRequest,
    ) -> clickhouse_20191111_models.CreateSQLAccountResponse:
        """
        @summary Creates a privileged account or a standard account for an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is applicable only to ApsaraDB for ClickHouse clusters of V20.8 or later that were created after December 1, 2021,
        
        @param request: CreateSQLAccountRequest
        @return: CreateSQLAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sqlaccount_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role.
        
        @param request: CreateServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role.
        
        @param request: CreateServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role.
        
        @param request: CreateServiceLinkedRoleRequest
        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role.
        
        @param request: CreateServiceLinkedRoleRequest
        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        """
        @summary Deletes a database account of an ApsaraDB for ClickHouse cluster.
        
        @description >  After you delete a database account, you cannot use the account to log on to the ApsaraDB for ClickHouse cluster. Exercise caution when performing this operation.
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        """
        @summary Deletes a database account of an ApsaraDB for ClickHouse cluster.
        
        @description >  After you delete a database account, you cannot use the account to log on to the ApsaraDB for ClickHouse cluster. Exercise caution when performing this operation.
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        """
        @summary Deletes a database account of an ApsaraDB for ClickHouse cluster.
        
        @description >  After you delete a database account, you cannot use the account to log on to the ApsaraDB for ClickHouse cluster. Exercise caution when performing this operation.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        """
        @summary Deletes a database account of an ApsaraDB for ClickHouse cluster.
        
        @description >  After you delete a database account, you cannot use the account to log on to the ApsaraDB for ClickHouse cluster. Exercise caution when performing this operation.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        """
        @summary Releases a pay-as-you-go ApsaraDB for ClickHouse cluster.
        
        @description *Warning** After an ApsaraDB for ClickHouse cluster is deleted, all data in the cluster is deleted and cannot be recovered. Exercise caution when performing this operation.
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        """
        @summary Releases a pay-as-you-go ApsaraDB for ClickHouse cluster.
        
        @description *Warning** After an ApsaraDB for ClickHouse cluster is deleted, all data in the cluster is deleted and cannot be recovered. Exercise caution when performing this operation.
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        """
        @summary Releases a pay-as-you-go ApsaraDB for ClickHouse cluster.
        
        @description *Warning** After an ApsaraDB for ClickHouse cluster is deleted, all data in the cluster is deleted and cannot be recovered. Exercise caution when performing this operation.
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        """
        @summary Releases a pay-as-you-go ApsaraDB for ClickHouse cluster.
        
        @description *Warning** After an ApsaraDB for ClickHouse cluster is deleted, all data in the cluster is deleted and cannot be recovered. Exercise caution when performing this operation.
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_syndb_with_options(
        self,
        request: clickhouse_20191111_models.DeleteSyndbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteSyndbResponse:
        """
        @summary Deletes a database used for data synchronization.
        
        @param request: DeleteSyndbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSyndbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.syn_db):
            query['SynDb'] = request.syn_db
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSyndb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteSyndbResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_syndb_with_options_async(
        self,
        request: clickhouse_20191111_models.DeleteSyndbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteSyndbResponse:
        """
        @summary Deletes a database used for data synchronization.
        
        @param request: DeleteSyndbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSyndbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.syn_db):
            query['SynDb'] = request.syn_db
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSyndb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteSyndbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_syndb(
        self,
        request: clickhouse_20191111_models.DeleteSyndbRequest,
    ) -> clickhouse_20191111_models.DeleteSyndbResponse:
        """
        @summary Deletes a database used for data synchronization.
        
        @param request: DeleteSyndbRequest
        @return: DeleteSyndbResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_syndb_with_options(request, runtime)

    async def delete_syndb_async(
        self,
        request: clickhouse_20191111_models.DeleteSyndbRequest,
    ) -> clickhouse_20191111_models.DeleteSyndbResponse:
        """
        @summary Deletes a database used for data synchronization.
        
        @param request: DeleteSyndbRequest
        @return: DeleteSyndbResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_syndb_with_options_async(request, runtime)

    def describe_account_authority_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        """
        @summary Queries the permissions of an account.
        
        @param request: DescribeAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountAuthorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_authority_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        """
        @summary Queries the permissions of an account.
        
        @param request: DescribeAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountAuthorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_authority(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        """
        @summary Queries the permissions of an account.
        
        @param request: DescribeAccountAuthorityRequest
        @return: DescribeAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_authority_with_options(request, runtime)

    async def describe_account_authority_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        """
        @summary Queries the permissions of an account.
        
        @param request: DescribeAccountAuthorityRequest
        @return: DescribeAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_authority_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        """
        @summary Queries the information about the database accounts of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        """
        @summary Queries the information about the database accounts of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        """
        @summary Queries the information about the database accounts of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        """
        @summary Queries the information about the database accounts of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_all_data_source_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAllDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSource',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_data_source_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAllDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSource',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_data_source(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAllDataSourceRequest
        @return: DescribeAllDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    async def describe_all_data_source_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        """
        @summary Queries a list of databases, tables, and columns in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAllDataSourceRequest
        @return: DescribeAllDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_data_source_with_options_async(request, runtime)

    def describe_all_data_sources_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        """
        @summary Queries the data sources of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAllDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSources',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_data_sources_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        """
        @summary Queries the data sources of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAllDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSources',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_data_sources(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        """
        @summary Queries the data sources of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAllDataSourcesRequest
        @return: DescribeAllDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_sources_with_options(request, runtime)

    async def describe_all_data_sources_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        """
        @summary Queries the data sources of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAllDataSourcesRequest
        @return: DescribeAllDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_data_sources_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup settings of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup settings of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup settings of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the backup settings of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for ApsaraDB for ClickHouse clusters of version 21.8 and later.
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for ApsaraDB for ClickHouse clusters of version 21.8 and later.
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for ApsaraDB for ClickHouse clusters of version 21.8 and later.
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        """
        @summary Queries the backup sets of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for ApsaraDB for ClickHouse clusters of version 21.8 and later.
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_columns_with_options(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        """
        @summary Queries information about columns.
        
        @param request: DescribeColumnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columns_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        """
        @summary Queries information about columns.
        
        @param request: DescribeColumnsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columns(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        """
        @summary Queries information about columns.
        
        @param request: DescribeColumnsRequest
        @return: DescribeColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    async def describe_columns_async(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        """
        @summary Queries information about columns.
        
        @param request: DescribeColumnsRequest
        @return: DescribeColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_columns_with_options_async(request, runtime)

    def describe_config_history_with_options(
        self,
        request: clickhouse_20191111_models.DescribeConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeConfigHistoryResponse:
        """
        @summary Queries the change records of the configuration parameters of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeConfigHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConfigHistoryResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigHistory',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeConfigHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_history_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeConfigHistoryResponse:
        """
        @summary Queries the change records of the configuration parameters of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeConfigHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConfigHistoryResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigHistory',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeConfigHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_history(
        self,
        request: clickhouse_20191111_models.DescribeConfigHistoryRequest,
    ) -> clickhouse_20191111_models.DescribeConfigHistoryResponse:
        """
        @summary Queries the change records of the configuration parameters of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeConfigHistoryRequest
        @return: DescribeConfigHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_config_history_with_options(request, runtime)

    async def describe_config_history_async(
        self,
        request: clickhouse_20191111_models.DescribeConfigHistoryRequest,
    ) -> clickhouse_20191111_models.DescribeConfigHistoryResponse:
        """
        @summary Queries the change records of the configuration parameters of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeConfigHistoryRequest
        @return: DescribeConfigHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_config_history_with_options_async(request, runtime)

    def describe_config_version_difference_with_options(
        self,
        request: clickhouse_20191111_models.DescribeConfigVersionDifferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeConfigVersionDifferenceResponse:
        """
        @summary Queries the values of the configuration parameters of an ApsaraDB for ClickHouse cluster before and after the values of the configuration parameters are changed.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeConfigVersionDifferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConfigVersionDifferenceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigVersionDifference',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeConfigVersionDifferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_version_difference_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeConfigVersionDifferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeConfigVersionDifferenceResponse:
        """
        @summary Queries the values of the configuration parameters of an ApsaraDB for ClickHouse cluster before and after the values of the configuration parameters are changed.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeConfigVersionDifferenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeConfigVersionDifferenceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigVersionDifference',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeConfigVersionDifferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_version_difference(
        self,
        request: clickhouse_20191111_models.DescribeConfigVersionDifferenceRequest,
    ) -> clickhouse_20191111_models.DescribeConfigVersionDifferenceResponse:
        """
        @summary Queries the values of the configuration parameters of an ApsaraDB for ClickHouse cluster before and after the values of the configuration parameters are changed.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeConfigVersionDifferenceRequest
        @return: DescribeConfigVersionDifferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_config_version_difference_with_options(request, runtime)

    async def describe_config_version_difference_async(
        self,
        request: clickhouse_20191111_models.DescribeConfigVersionDifferenceRequest,
    ) -> clickhouse_20191111_models.DescribeConfigVersionDifferenceResponse:
        """
        @summary Queries the values of the configuration parameters of an ApsaraDB for ClickHouse cluster before and after the values of the configuration parameters are changed.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeConfigVersionDifferenceRequest
        @return: DescribeConfigVersionDifferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_config_version_difference_with_options_async(request, runtime)

    def describe_dbcluster_access_white_list_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        """
        @summary Queries the IP address whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAccessWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAccessWhiteList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_access_white_list_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        """
        @summary Queries the IP address whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAccessWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAccessWhiteList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_access_white_list(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        """
        @summary Queries the IP address whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterAccessWhiteListRequest
        @return: DescribeDBClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_access_white_list_with_options(request, runtime)

    async def describe_dbcluster_access_white_list_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        """
        @summary Queries the IP address whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterAccessWhiteListRequest
        @return: DescribeDBClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_access_white_list_with_options_async(request, runtime)

    def describe_dbcluster_attribute_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAttribute',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_attribute_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAttribute',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_attribute(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @return: DescribeDBClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    async def describe_dbcluster_attribute_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries the information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @return: DescribeDBClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_attribute_with_options_async(request, runtime)

    def describe_dbcluster_config_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        """
        @summary Queries information about the parameter settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_config_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        """
        @summary Queries information about the parameter settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_config(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        """
        @summary Queries information about the parameter settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterConfigRequest
        @return: DescribeDBClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_config_with_options(request, runtime)

    async def describe_dbcluster_config_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        """
        @summary Queries information about the parameter settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterConfigRequest
        @return: DescribeDBClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_config_with_options_async(request, runtime)

    def describe_dbcluster_config_in_xmlwith_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigInXMLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigInXMLResponse:
        """
        @summary Queries the values of the configuration parameters in the config.xml file of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeDBClusterConfigInXMLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterConfigInXMLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfigInXML',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterConfigInXMLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_config_in_xmlwith_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigInXMLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigInXMLResponse:
        """
        @summary Queries the values of the configuration parameters in the config.xml file of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeDBClusterConfigInXMLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterConfigInXMLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfigInXML',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterConfigInXMLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_config_in_xml(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigInXMLRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigInXMLResponse:
        """
        @summary Queries the values of the configuration parameters in the config.xml file of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeDBClusterConfigInXMLRequest
        @return: DescribeDBClusterConfigInXMLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_config_in_xmlwith_options(request, runtime)

    async def describe_dbcluster_config_in_xml_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigInXMLRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigInXMLResponse:
        """
        @summary Queries the values of the configuration parameters in the config.xml file of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: DescribeDBClusterConfigInXMLRequest
        @return: DescribeDBClusterConfigInXMLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_config_in_xmlwith_options_async(request, runtime)

    def describe_dbcluster_net_info_items_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        """
        @summary Queries the network information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterNetInfoItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterNetInfoItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterNetInfoItems',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_net_info_items_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        """
        @summary Queries the network information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterNetInfoItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterNetInfoItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterNetInfoItems',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_net_info_items(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        """
        @summary Queries the network information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterNetInfoItemsRequest
        @return: DescribeDBClusterNetInfoItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_net_info_items_with_options(request, runtime)

    async def describe_dbcluster_net_info_items_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        """
        @summary Queries the network information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBClusterNetInfoItemsRequest
        @return: DescribeDBClusterNetInfoItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_net_info_items_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries performance data about an ApsaraDB for ClickHouse cluster.
        
        @description You can query the performance data of a specified cluster over a specific time range based on the performance metrics. The data is collected every 30 seconds.
        >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created before December 1, 2021.
        
        @param request: DescribeDBClusterPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries performance data about an ApsaraDB for ClickHouse cluster.
        
        @description You can query the performance data of a specified cluster over a specific time range based on the performance metrics. The data is collected every 30 seconds.
        >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created before December 1, 2021.
        
        @param request: DescribeDBClusterPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries performance data about an ApsaraDB for ClickHouse cluster.
        
        @description You can query the performance data of a specified cluster over a specific time range based on the performance metrics. The data is collected every 30 seconds.
        >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created before December 1, 2021.
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries performance data about an ApsaraDB for ClickHouse cluster.
        
        @description You can query the performance data of a specified cluster over a specific time range based on the performance metrics. The data is collected every 30 seconds.
        >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created before December 1, 2021.
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbclusters_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        """
        @summary Queries the information about ApsaraDB for ClickHouse clusters in a region.
        
        @param request: DescribeDBClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbclusters_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        """
        @summary Queries the information about ApsaraDB for ClickHouse clusters in a region.
        
        @param request: DescribeDBClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbclusters(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        """
        @summary Queries the information about ApsaraDB for ClickHouse clusters in a region.
        
        @param request: DescribeDBClustersRequest
        @return: DescribeDBClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    async def describe_dbclusters_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        """
        @summary Queries the information about ApsaraDB for ClickHouse clusters in a region.
        
        @param request: DescribeDBClustersRequest
        @return: DescribeDBClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbclusters_with_options_async(request, runtime)

    def describe_dbconfig_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        """
        @summary Queries configuration information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbconfig_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        """
        @summary Queries configuration information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbconfig(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        """
        @summary Queries configuration information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBConfigRequest
        @return: DescribeDBConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbconfig_with_options(request, runtime)

    async def describe_dbconfig_async(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        """
        @summary Queries configuration information about an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeDBConfigRequest
        @return: DescribeDBConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbconfig_with_options_async(request, runtime)

    def describe_ossstorage_with_options(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        """
        @summary Queries the storage of cold data.
        
        @param request: DescribeOSSStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOSSStorageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOSSStorage',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeOSSStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ossstorage_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        """
        @summary Queries the storage of cold data.
        
        @param request: DescribeOSSStorageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOSSStorageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOSSStorage',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeOSSStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ossstorage(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        """
        @summary Queries the storage of cold data.
        
        @param request: DescribeOSSStorageRequest
        @return: DescribeOSSStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ossstorage_with_options(request, runtime)

    async def describe_ossstorage_async(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        """
        @summary Queries the storage of cold data.
        
        @param request: DescribeOSSStorageRequest
        @return: DescribeOSSStorageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ossstorage_with_options_async(request, runtime)

    def describe_process_list_with_options(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        """
        @summary Queries the details of queries that are being executed in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.initial_user):
            query['InitialUser'] = request.initial_user
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_list_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        """
        @summary Queries the details of queries that are being executed in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.initial_user):
            query['InitialUser'] = request.initial_user
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeProcessListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_list(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        """
        @summary Queries the details of queries that are being executed in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeProcessListRequest
        @return: DescribeProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    async def describe_process_list_async(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        """
        @summary Queries the details of queries that are being executed in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeProcessListRequest
        @return: DescribeProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_list_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        """
        @summary Queries the information about all regions and zones of ApsaraDB for ClickHouse clusters.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        """
        @summary Queries the information about all regions and zones of ApsaraDB for ClickHouse clusters.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        """
        @summary Queries the information about all regions and zones of ApsaraDB for ClickHouse clusters.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        """
        @summary Queries the information about all regions and zones of ApsaraDB for ClickHouse clusters.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_schemas_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        """
        @summary Queries a list of all databases in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSchemasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSchemasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSchemas',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_schemas_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        """
        @summary Queries a list of all databases in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSchemasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSchemasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSchemas',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_schemas(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        """
        @summary Queries a list of all databases in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSchemasRequest
        @return: DescribeSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_schemas_with_options(request, runtime)

    async def describe_schemas_async(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        """
        @summary Queries a list of all databases in an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSchemasRequest
        @return: DescribeSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_schemas_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details about slow query logs.
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details about slow query logs.
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details about slow query logs.
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details about slow query logs.
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_syn_db_tables_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSynDbTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSynDbTablesResponse:
        """
        @summary Queries information about tables that are synchronized from an ApsaraDB RDS for MySQL instance to an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSynDbTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynDbTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.syn_db):
            query['SynDb'] = request.syn_db
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynDbTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSynDbTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_syn_db_tables_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSynDbTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSynDbTablesResponse:
        """
        @summary Queries information about tables that are synchronized from an ApsaraDB RDS for MySQL instance to an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSynDbTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynDbTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.syn_db):
            query['SynDb'] = request.syn_db
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynDbTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSynDbTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_syn_db_tables(
        self,
        request: clickhouse_20191111_models.DescribeSynDbTablesRequest,
    ) -> clickhouse_20191111_models.DescribeSynDbTablesResponse:
        """
        @summary Queries information about tables that are synchronized from an ApsaraDB RDS for MySQL instance to an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSynDbTablesRequest
        @return: DescribeSynDbTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_syn_db_tables_with_options(request, runtime)

    async def describe_syn_db_tables_async(
        self,
        request: clickhouse_20191111_models.DescribeSynDbTablesRequest,
    ) -> clickhouse_20191111_models.DescribeSynDbTablesResponse:
        """
        @summary Queries information about tables that are synchronized from an ApsaraDB RDS for MySQL instance to an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSynDbTablesRequest
        @return: DescribeSynDbTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_syn_db_tables_with_options_async(request, runtime)

    def describe_syn_dbs_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSynDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSynDbsResponse:
        """
        @summary Queries the information about data synchronization between an ApsaraDB for ClickHouse cluster and an ApsaraDB RDS for MySQL instance.
        
        @param request: DescribeSynDbsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynDbsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynDbs',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSynDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_syn_dbs_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSynDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSynDbsResponse:
        """
        @summary Queries the information about data synchronization between an ApsaraDB for ClickHouse cluster and an ApsaraDB RDS for MySQL instance.
        
        @param request: DescribeSynDbsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSynDbsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynDbs',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSynDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_syn_dbs(
        self,
        request: clickhouse_20191111_models.DescribeSynDbsRequest,
    ) -> clickhouse_20191111_models.DescribeSynDbsResponse:
        """
        @summary Queries the information about data synchronization between an ApsaraDB for ClickHouse cluster and an ApsaraDB RDS for MySQL instance.
        
        @param request: DescribeSynDbsRequest
        @return: DescribeSynDbsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_syn_dbs_with_options(request, runtime)

    async def describe_syn_dbs_async(
        self,
        request: clickhouse_20191111_models.DescribeSynDbsRequest,
    ) -> clickhouse_20191111_models.DescribeSynDbsResponse:
        """
        @summary Queries the information about data synchronization between an ApsaraDB for ClickHouse cluster and an ApsaraDB RDS for MySQL instance.
        
        @param request: DescribeSynDbsRequest
        @return: DescribeSynDbsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_syn_dbs_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        """
        @summary Queries the information about tables in a database of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        """
        @summary Queries the information about tables in a database of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tables(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        """
        @summary Queries the information about tables in a database of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeTablesRequest
        @return: DescribeTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        """
        @summary Queries the information about tables in a database of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeTablesRequest
        @return: DescribeTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def describe_transfer_history_with_options(
        self,
        request: clickhouse_20191111_models.DescribeTransferHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeTransferHistoryResponse:
        """
        @summary Queries information about data migration from an ApsaraDB for ClickHouse cluster of an earlier version to an ApsaraDB for ClickHouse cluster of a later version
        
        @description >  You can call this operation to query information about only data migration from an ApsaraDB for ClickHouse cluster of an earlier version to an ApsaraDB for ClickHouse cluster of a later version.
        
        @param request: DescribeTransferHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTransferHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransferHistory',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTransferHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transfer_history_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeTransferHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeTransferHistoryResponse:
        """
        @summary Queries information about data migration from an ApsaraDB for ClickHouse cluster of an earlier version to an ApsaraDB for ClickHouse cluster of a later version
        
        @description >  You can call this operation to query information about only data migration from an ApsaraDB for ClickHouse cluster of an earlier version to an ApsaraDB for ClickHouse cluster of a later version.
        
        @param request: DescribeTransferHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTransferHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransferHistory',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTransferHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transfer_history(
        self,
        request: clickhouse_20191111_models.DescribeTransferHistoryRequest,
    ) -> clickhouse_20191111_models.DescribeTransferHistoryResponse:
        """
        @summary Queries information about data migration from an ApsaraDB for ClickHouse cluster of an earlier version to an ApsaraDB for ClickHouse cluster of a later version
        
        @description >  You can call this operation to query information about only data migration from an ApsaraDB for ClickHouse cluster of an earlier version to an ApsaraDB for ClickHouse cluster of a later version.
        
        @param request: DescribeTransferHistoryRequest
        @return: DescribeTransferHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_transfer_history_with_options(request, runtime)

    async def describe_transfer_history_async(
        self,
        request: clickhouse_20191111_models.DescribeTransferHistoryRequest,
    ) -> clickhouse_20191111_models.DescribeTransferHistoryResponse:
        """
        @summary Queries information about data migration from an ApsaraDB for ClickHouse cluster of an earlier version to an ApsaraDB for ClickHouse cluster of a later version
        
        @description >  You can call this operation to query information about only data migration from an ApsaraDB for ClickHouse cluster of an earlier version to an ApsaraDB for ClickHouse cluster of a later version.
        
        @param request: DescribeTransferHistoryRequest
        @return: DescribeTransferHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_transfer_history_with_options_async(request, runtime)

    def kill_process_with_options(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        """
        @summary Terminates an ongoing task.
        
        @param request: KillProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.KillProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_process_with_options_async(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        """
        @summary Terminates an ongoing task.
        
        @param request: KillProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.KillProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_process(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        """
        @summary Terminates an ongoing task.
        
        @param request: KillProcessRequest
        @return: KillProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    async def kill_process_async(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        """
        @summary Terminates an ongoing task.
        
        @param request: KillProcessRequest
        @return: KillProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_process_with_options_async(request, runtime)

    def modify_account_authority_with_options(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        """
        @summary Modifies the permissions of an account.
        
        @param request: ModifyAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountAuthorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.allow_databases):
            query['AllowDatabases'] = request.allow_databases
        if not UtilClient.is_unset(request.allow_dictionaries):
            query['AllowDictionaries'] = request.allow_dictionaries
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ddl_authority):
            query['DdlAuthority'] = request.ddl_authority
        if not UtilClient.is_unset(request.dml_authority):
            query['DmlAuthority'] = request.dml_authority
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.total_databases):
            query['TotalDatabases'] = request.total_databases
        if not UtilClient.is_unset(request.total_dictionaries):
            query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_authority_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        """
        @summary Modifies the permissions of an account.
        
        @param request: ModifyAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountAuthorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.allow_databases):
            query['AllowDatabases'] = request.allow_databases
        if not UtilClient.is_unset(request.allow_dictionaries):
            query['AllowDictionaries'] = request.allow_dictionaries
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ddl_authority):
            query['DdlAuthority'] = request.ddl_authority
        if not UtilClient.is_unset(request.dml_authority):
            query['DmlAuthority'] = request.dml_authority
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.total_databases):
            query['TotalDatabases'] = request.total_databases
        if not UtilClient.is_unset(request.total_dictionaries):
            query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_authority(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        """
        @summary Modifies the permissions of an account.
        
        @param request: ModifyAccountAuthorityRequest
        @return: ModifyAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_authority_with_options(request, runtime)

    async def modify_account_authority_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        """
        @summary Modifies the permissions of an account.
        
        @param request: ModifyAccountAuthorityRequest
        @return: ModifyAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_authority_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the backup settings of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the backup settings of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the backup settings of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the backup settings of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is available only for the ApsaraDB for ClickHouse clusters of versions 20.3, 20.8, and 21.8.
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        """
        @summary Upgrades or downgrades an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not UtilClient.is_unset(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not UtilClient.is_unset(request.db_node_storage_type):
            query['DbNodeStorageType'] = request.db_node_storage_type
        if not UtilClient.is_unset(request.disable_write_windows):
            query['DisableWriteWindows'] = request.disable_write_windows
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        """
        @summary Upgrades or downgrades an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not UtilClient.is_unset(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not UtilClient.is_unset(request.db_node_storage_type):
            query['DbNodeStorageType'] = request.db_node_storage_type
        if not UtilClient.is_unset(request.disable_write_windows):
            query['DisableWriteWindows'] = request.disable_write_windows
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        """
        @summary Upgrades or downgrades an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterRequest
        @return: ModifyDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    async def modify_dbcluster_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        """
        @summary Upgrades or downgrades an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterRequest
        @return: ModifyDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_with_options_async(request, runtime)

    def modify_dbcluster_access_white_list_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterAccessWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_iparray_attribute):
            query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        if not UtilClient.is_unset(request.dbcluster_iparray_name):
            query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAccessWhiteList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_access_white_list_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterAccessWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterAccessWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_iparray_attribute):
            query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        if not UtilClient.is_unset(request.dbcluster_iparray_name):
            query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAccessWhiteList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_access_white_list(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterAccessWhiteListRequest
        @return: ModifyDBClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_access_white_list_with_options(request, runtime)

    async def modify_dbcluster_access_white_list_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterAccessWhiteListRequest
        @return: ModifyDBClusterAccessWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_access_white_list_with_options_async(request, runtime)

    def modify_dbcluster_config_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        """
        @summary Modifies the configurations of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_config):
            query['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_config_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        """
        @summary Modifies the configurations of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_config):
            query['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_config(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        """
        @summary Modifies the configurations of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterConfigRequest
        @return: ModifyDBClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_config_with_options(request, runtime)

    async def modify_dbcluster_config_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        """
        @summary Modifies the configurations of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterConfigRequest
        @return: ModifyDBClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_config_with_options_async(request, runtime)

    def modify_dbcluster_config_in_xmlwith_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigInXMLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigInXMLResponse:
        """
        @summary Changes the configuration parameters of an ApsaraDB for ClickHouse cluster that runs Community-compatible Edition.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: ModifyDBClusterConfigInXMLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterConfigInXMLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfigInXML',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterConfigInXMLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_config_in_xmlwith_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigInXMLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigInXMLResponse:
        """
        @summary Changes the configuration parameters of an ApsaraDB for ClickHouse cluster that runs Community-compatible Edition.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: ModifyDBClusterConfigInXMLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterConfigInXMLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfigInXML',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterConfigInXMLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_config_in_xml(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigInXMLRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigInXMLResponse:
        """
        @summary Changes the configuration parameters of an ApsaraDB for ClickHouse cluster that runs Community-compatible Edition.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: ModifyDBClusterConfigInXMLRequest
        @return: ModifyDBClusterConfigInXMLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_config_in_xmlwith_options(request, runtime)

    async def modify_dbcluster_config_in_xml_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigInXMLRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigInXMLResponse:
        """
        @summary Changes the configuration parameters of an ApsaraDB for ClickHouse cluster that runs Community-compatible Edition.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were created after December 1, 2021.
        
        @param request: ModifyDBClusterConfigInXMLRequest
        @return: ModifyDBClusterConfigInXMLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_config_in_xmlwith_options_async(request, runtime)

    def modify_dbcluster_description_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Changes the name of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_description_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Changes the name of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_description(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Changes the name of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterDescriptionRequest
        @return: ModifyDBClusterDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    async def modify_dbcluster_description_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Changes the name of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterDescriptionRequest
        @return: ModifyDBClusterDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_description_with_options_async(request, runtime)

    def modify_dbcluster_maintain_time_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_maintain_time_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_maintain_time(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @return: ModifyDBClusterMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    async def modify_dbcluster_maintain_time_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @return: ModifyDBClusterMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_maintain_time_with_options_async(request, runtime)

    def modify_dbconfig_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        """
        @summary Modifies the dictionary configuration of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbconfig_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        """
        @summary Modifies the dictionary configuration of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbconfig(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        """
        @summary Modifies the dictionary configuration of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBConfigRequest
        @return: ModifyDBConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbconfig_with_options(request, runtime)

    async def modify_dbconfig_async(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        """
        @summary Modifies the dictionary configuration of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBConfigRequest
        @return: ModifyDBConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbconfig_with_options_async(request, runtime)

    def modify_minor_version_greade_type_with_options(
        self,
        request: clickhouse_20191111_models.ModifyMinorVersionGreadeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyMinorVersionGreadeTypeResponse:
        """
        @summary Modifies the type of a minor version update in ApsaraDB for ClickHouse.
        
        @param request: ModifyMinorVersionGreadeTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMinorVersionGreadeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.maintain_auto_type):
            query['MaintainAutoType'] = request.maintain_auto_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMinorVersionGreadeType',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyMinorVersionGreadeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_minor_version_greade_type_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyMinorVersionGreadeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyMinorVersionGreadeTypeResponse:
        """
        @summary Modifies the type of a minor version update in ApsaraDB for ClickHouse.
        
        @param request: ModifyMinorVersionGreadeTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMinorVersionGreadeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.maintain_auto_type):
            query['MaintainAutoType'] = request.maintain_auto_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMinorVersionGreadeType',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyMinorVersionGreadeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_minor_version_greade_type(
        self,
        request: clickhouse_20191111_models.ModifyMinorVersionGreadeTypeRequest,
    ) -> clickhouse_20191111_models.ModifyMinorVersionGreadeTypeResponse:
        """
        @summary Modifies the type of a minor version update in ApsaraDB for ClickHouse.
        
        @param request: ModifyMinorVersionGreadeTypeRequest
        @return: ModifyMinorVersionGreadeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_minor_version_greade_type_with_options(request, runtime)

    async def modify_minor_version_greade_type_async(
        self,
        request: clickhouse_20191111_models.ModifyMinorVersionGreadeTypeRequest,
    ) -> clickhouse_20191111_models.ModifyMinorVersionGreadeTypeResponse:
        """
        @summary Modifies the type of a minor version update in ApsaraDB for ClickHouse.
        
        @param request: ModifyMinorVersionGreadeTypeRequest
        @return: ModifyMinorVersionGreadeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_minor_version_greade_type_with_options_async(request, runtime)

    def modify_rdsto_clickhouse_db_with_options(
        self,
        request: clickhouse_20191111_models.ModifyRDSToClickhouseDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse:
        """
        @summary Modifies the synchronization task of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is applicable only to ApsaraDB for ClickHouse clusters.
        
        @param request: ModifyRDSToClickhouseDbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRDSToClickhouseDbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not UtilClient.is_unset(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not UtilClient.is_unset(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.limit_upper):
            query['LimitUpper'] = request.limit_upper
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rds_id):
            query['RdsId'] = request.rds_id
        if not UtilClient.is_unset(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not UtilClient.is_unset(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not UtilClient.is_unset(request.rds_syn_db):
            query['RdsSynDb'] = request.rds_syn_db
        if not UtilClient.is_unset(request.rds_syn_tables):
            query['RdsSynTables'] = request.rds_syn_tables
        if not UtilClient.is_unset(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not UtilClient.is_unset(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.skip_unsupported):
            query['SkipUnsupported'] = request.skip_unsupported
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRDSToClickhouseDb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rdsto_clickhouse_db_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyRDSToClickhouseDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse:
        """
        @summary Modifies the synchronization task of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is applicable only to ApsaraDB for ClickHouse clusters.
        
        @param request: ModifyRDSToClickhouseDbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRDSToClickhouseDbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not UtilClient.is_unset(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not UtilClient.is_unset(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not UtilClient.is_unset(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not UtilClient.is_unset(request.limit_upper):
            query['LimitUpper'] = request.limit_upper
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rds_id):
            query['RdsId'] = request.rds_id
        if not UtilClient.is_unset(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not UtilClient.is_unset(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not UtilClient.is_unset(request.rds_syn_db):
            query['RdsSynDb'] = request.rds_syn_db
        if not UtilClient.is_unset(request.rds_syn_tables):
            query['RdsSynTables'] = request.rds_syn_tables
        if not UtilClient.is_unset(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not UtilClient.is_unset(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.skip_unsupported):
            query['SkipUnsupported'] = request.skip_unsupported
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRDSToClickhouseDb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rdsto_clickhouse_db(
        self,
        request: clickhouse_20191111_models.ModifyRDSToClickhouseDbRequest,
    ) -> clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse:
        """
        @summary Modifies the synchronization task of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is applicable only to ApsaraDB for ClickHouse clusters.
        
        @param request: ModifyRDSToClickhouseDbRequest
        @return: ModifyRDSToClickhouseDbResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_rdsto_clickhouse_db_with_options(request, runtime)

    async def modify_rdsto_clickhouse_db_async(
        self,
        request: clickhouse_20191111_models.ModifyRDSToClickhouseDbRequest,
    ) -> clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse:
        """
        @summary Modifies the synchronization task of an ApsaraDB for ClickHouse cluster.
        
        @description >  This operation is applicable only to ApsaraDB for ClickHouse clusters.
        
        @param request: ModifyRDSToClickhouseDbRequest
        @return: ModifyRDSToClickhouseDbResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_rdsto_clickhouse_db_with_options_async(request, runtime)

    def release_cluster_public_connection_with_options(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ReleaseClusterPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseClusterPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_public_connection_with_options_async(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ReleaseClusterPublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseClusterPublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cluster_public_connection(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ReleaseClusterPublicConnectionRequest
        @return: ReleaseClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    async def release_cluster_public_connection_async(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ReleaseClusterPublicConnectionRequest
        @return: ReleaseClusterPublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an ApsaraDB for ClickHouse cluster.
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an ApsaraDB for ClickHouse cluster.
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an ApsaraDB for ClickHouse cluster.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an ApsaraDB for ClickHouse cluster.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: clickhouse_20191111_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.RestartInstanceResponse:
        """
        @summary Restarts an ApsaraDB for ClickHouse cluster.
        
        @param request: RestartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restart_time):
            query['RestartTime'] = request.restart_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: clickhouse_20191111_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.RestartInstanceResponse:
        """
        @summary Restarts an ApsaraDB for ClickHouse cluster.
        
        @param request: RestartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restart_time):
            query['RestartTime'] = request.restart_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: clickhouse_20191111_models.RestartInstanceRequest,
    ) -> clickhouse_20191111_models.RestartInstanceResponse:
        """
        @summary Restarts an ApsaraDB for ClickHouse cluster.
        
        @param request: RestartInstanceRequest
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: clickhouse_20191111_models.RestartInstanceRequest,
    ) -> clickhouse_20191111_models.RestartInstanceResponse:
        """
        @summary Restarts an ApsaraDB for ClickHouse cluster.
        
        @param request: RestartInstanceRequest
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def transfer_version_with_options(
        self,
        request: clickhouse_20191111_models.TransferVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.TransferVersionResponse:
        """
        @summary Migrates the data of a source ApsaraDB for ClickHouse cluster to a destination ApsaraDB for ClickHouse cluster.
        
        @description ## [](#)Prerequisites
        The IP address of the source ApsaraDB for ClickHouse cluster is added to the IP address whitelist of the destination ApsaraDB for ClickHouse cluster.
        The IP address of the destination ApsaraDB for ClickHouse cluster is added to the IP address whitelist of the source ApsaraDB for ClickHouse cluster.
        >  You can execute the `select  from system.clusters;` statement to query the IP address of an ApsaraDB for ClickHouse cluster.
        
        @param request: TransferVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.disable_write_windows):
            query['DisableWriteWindows'] = request.disable_write_windows
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_account):
            query['SourceAccount'] = request.source_account
        if not UtilClient.is_unset(request.source_cluster_name):
            query['SourceClusterName'] = request.source_cluster_name
        if not UtilClient.is_unset(request.source_password):
            query['SourcePassword'] = request.source_password
        if not UtilClient.is_unset(request.source_shards):
            query['SourceShards'] = request.source_shards
        if not UtilClient.is_unset(request.target_account):
            query['TargetAccount'] = request.target_account
        if not UtilClient.is_unset(request.target_db_cluster_id):
            query['TargetDbClusterId'] = request.target_db_cluster_id
        if not UtilClient.is_unset(request.target_password):
            query['TargetPassword'] = request.target_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferVersion',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.TransferVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_version_with_options_async(
        self,
        request: clickhouse_20191111_models.TransferVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.TransferVersionResponse:
        """
        @summary Migrates the data of a source ApsaraDB for ClickHouse cluster to a destination ApsaraDB for ClickHouse cluster.
        
        @description ## [](#)Prerequisites
        The IP address of the source ApsaraDB for ClickHouse cluster is added to the IP address whitelist of the destination ApsaraDB for ClickHouse cluster.
        The IP address of the destination ApsaraDB for ClickHouse cluster is added to the IP address whitelist of the source ApsaraDB for ClickHouse cluster.
        >  You can execute the `select  from system.clusters;` statement to query the IP address of an ApsaraDB for ClickHouse cluster.
        
        @param request: TransferVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransferVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.disable_write_windows):
            query['DisableWriteWindows'] = request.disable_write_windows
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_account):
            query['SourceAccount'] = request.source_account
        if not UtilClient.is_unset(request.source_cluster_name):
            query['SourceClusterName'] = request.source_cluster_name
        if not UtilClient.is_unset(request.source_password):
            query['SourcePassword'] = request.source_password
        if not UtilClient.is_unset(request.source_shards):
            query['SourceShards'] = request.source_shards
        if not UtilClient.is_unset(request.target_account):
            query['TargetAccount'] = request.target_account
        if not UtilClient.is_unset(request.target_db_cluster_id):
            query['TargetDbClusterId'] = request.target_db_cluster_id
        if not UtilClient.is_unset(request.target_password):
            query['TargetPassword'] = request.target_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferVersion',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.TransferVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_version(
        self,
        request: clickhouse_20191111_models.TransferVersionRequest,
    ) -> clickhouse_20191111_models.TransferVersionResponse:
        """
        @summary Migrates the data of a source ApsaraDB for ClickHouse cluster to a destination ApsaraDB for ClickHouse cluster.
        
        @description ## [](#)Prerequisites
        The IP address of the source ApsaraDB for ClickHouse cluster is added to the IP address whitelist of the destination ApsaraDB for ClickHouse cluster.
        The IP address of the destination ApsaraDB for ClickHouse cluster is added to the IP address whitelist of the source ApsaraDB for ClickHouse cluster.
        >  You can execute the `select  from system.clusters;` statement to query the IP address of an ApsaraDB for ClickHouse cluster.
        
        @param request: TransferVersionRequest
        @return: TransferVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_version_with_options(request, runtime)

    async def transfer_version_async(
        self,
        request: clickhouse_20191111_models.TransferVersionRequest,
    ) -> clickhouse_20191111_models.TransferVersionResponse:
        """
        @summary Migrates the data of a source ApsaraDB for ClickHouse cluster to a destination ApsaraDB for ClickHouse cluster.
        
        @description ## [](#)Prerequisites
        The IP address of the source ApsaraDB for ClickHouse cluster is added to the IP address whitelist of the destination ApsaraDB for ClickHouse cluster.
        The IP address of the destination ApsaraDB for ClickHouse cluster is added to the IP address whitelist of the source ApsaraDB for ClickHouse cluster.
        >  You can execute the `select  from system.clusters;` statement to query the IP address of an ApsaraDB for ClickHouse cluster.
        
        @param request: TransferVersionRequest
        @return: TransferVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transfer_version_with_options_async(request, runtime)

    def upgrade_minor_version_with_options(
        self,
        request: clickhouse_20191111_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.UpgradeMinorVersionResponse:
        """
        @summary Updates the minor engine version of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were purchased after December 1, 2021.
        
        @param request: UpgradeMinorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.upgrade_immediately):
            query['UpgradeImmediately'] = request.upgrade_immediately
        if not UtilClient.is_unset(request.upgrade_time):
            query['UpgradeTime'] = request.upgrade_time
        if not UtilClient.is_unset(request.upgrade_version):
            query['UpgradeVersion'] = request.upgrade_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMinorVersion',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.UpgradeMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_minor_version_with_options_async(
        self,
        request: clickhouse_20191111_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.UpgradeMinorVersionResponse:
        """
        @summary Updates the minor engine version of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were purchased after December 1, 2021.
        
        @param request: UpgradeMinorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.upgrade_immediately):
            query['UpgradeImmediately'] = request.upgrade_immediately
        if not UtilClient.is_unset(request.upgrade_time):
            query['UpgradeTime'] = request.upgrade_time
        if not UtilClient.is_unset(request.upgrade_version):
            query['UpgradeVersion'] = request.upgrade_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMinorVersion',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.UpgradeMinorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_minor_version(
        self,
        request: clickhouse_20191111_models.UpgradeMinorVersionRequest,
    ) -> clickhouse_20191111_models.UpgradeMinorVersionResponse:
        """
        @summary Updates the minor engine version of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were purchased after December 1, 2021.
        
        @param request: UpgradeMinorVersionRequest
        @return: UpgradeMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_minor_version_with_options(request, runtime)

    async def upgrade_minor_version_async(
        self,
        request: clickhouse_20191111_models.UpgradeMinorVersionRequest,
    ) -> clickhouse_20191111_models.UpgradeMinorVersionResponse:
        """
        @summary Updates the minor engine version of an ApsaraDB for ClickHouse cluster.
        
        @description >  You can call this operation only for ApsaraDB for ClickHouse clusters that were purchased after December 1, 2021.
        
        @param request: UpgradeMinorVersionRequest
        @return: UpgradeMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_minor_version_with_options_async(request, runtime)
