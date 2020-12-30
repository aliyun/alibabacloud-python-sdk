# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cassandra20190101 import models as cassandra_20190101_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cassandra', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_public_contact_points_with_options(
        self,
        request: cassandra_20190101_models.AllocatePublicContactPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.AllocatePublicContactPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.AllocatePublicContactPointsResponse().from_map(
            self.do_rpcrequest('AllocatePublicContactPoints', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_public_contact_points_with_options_async(
        self,
        request: cassandra_20190101_models.AllocatePublicContactPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.AllocatePublicContactPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.AllocatePublicContactPointsResponse().from_map(
            await self.do_rpcrequest_async('AllocatePublicContactPoints', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_public_contact_points(
        self,
        request: cassandra_20190101_models.AllocatePublicContactPointsRequest,
    ) -> cassandra_20190101_models.AllocatePublicContactPointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_contact_points_with_options(request, runtime)

    async def allocate_public_contact_points_async(
        self,
        request: cassandra_20190101_models.AllocatePublicContactPointsRequest,
    ) -> cassandra_20190101_models.AllocatePublicContactPointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_public_contact_points_with_options_async(request, runtime)

    def create_backup_plan_with_options(
        self,
        request: cassandra_20190101_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.CreateBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.CreateBackupPlanResponse().from_map(
            self.do_rpcrequest('CreateBackupPlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_plan_with_options_async(
        self,
        request: cassandra_20190101_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.CreateBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.CreateBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('CreateBackupPlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup_plan(
        self,
        request: cassandra_20190101_models.CreateBackupPlanRequest,
    ) -> cassandra_20190101_models.CreateBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    async def create_backup_plan_async(
        self,
        request: cassandra_20190101_models.CreateBackupPlanRequest,
    ) -> cassandra_20190101_models.CreateBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_plan_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: cassandra_20190101_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.CreateClusterResponse().from_map(
            self.do_rpcrequest('CreateCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: cassandra_20190101_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.CreateClusterResponse().from_map(
            await self.do_rpcrequest_async('CreateCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster(
        self,
        request: cassandra_20190101_models.CreateClusterRequest,
    ) -> cassandra_20190101_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: cassandra_20190101_models.CreateClusterRequest,
    ) -> cassandra_20190101_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_data_center_with_options(
        self,
        request: cassandra_20190101_models.CreateDataCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.CreateDataCenterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.CreateDataCenterResponse().from_map(
            self.do_rpcrequest('CreateDataCenter', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_center_with_options_async(
        self,
        request: cassandra_20190101_models.CreateDataCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.CreateDataCenterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.CreateDataCenterResponse().from_map(
            await self.do_rpcrequest_async('CreateDataCenter', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_center(
        self,
        request: cassandra_20190101_models.CreateDataCenterRequest,
    ) -> cassandra_20190101_models.CreateDataCenterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_center_with_options(request, runtime)

    async def create_data_center_async(
        self,
        request: cassandra_20190101_models.CreateDataCenterRequest,
    ) -> cassandra_20190101_models.CreateDataCenterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_center_with_options_async(request, runtime)

    def delete_backup_plan_with_options(
        self,
        request: cassandra_20190101_models.DeleteBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DeleteBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DeleteBackupPlanResponse().from_map(
            self.do_rpcrequest('DeleteBackupPlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_backup_plan_with_options_async(
        self,
        request: cassandra_20190101_models.DeleteBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DeleteBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DeleteBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('DeleteBackupPlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_backup_plan(
        self,
        request: cassandra_20190101_models.DeleteBackupPlanRequest,
    ) -> cassandra_20190101_models.DeleteBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_plan_with_options(request, runtime)

    async def delete_backup_plan_async(
        self,
        request: cassandra_20190101_models.DeleteBackupPlanRequest,
    ) -> cassandra_20190101_models.DeleteBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_plan_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: cassandra_20190101_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DeleteClusterResponse().from_map(
            self.do_rpcrequest('DeleteCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: cassandra_20190101_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DeleteClusterResponse().from_map(
            await self.do_rpcrequest_async('DeleteCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cluster(
        self,
        request: cassandra_20190101_models.DeleteClusterRequest,
    ) -> cassandra_20190101_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: cassandra_20190101_models.DeleteClusterRequest,
    ) -> cassandra_20190101_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_data_center_with_options(
        self,
        request: cassandra_20190101_models.DeleteDataCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DeleteDataCenterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DeleteDataCenterResponse().from_map(
            self.do_rpcrequest('DeleteDataCenter', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_data_center_with_options_async(
        self,
        request: cassandra_20190101_models.DeleteDataCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DeleteDataCenterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DeleteDataCenterResponse().from_map(
            await self.do_rpcrequest_async('DeleteDataCenter', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_center(
        self,
        request: cassandra_20190101_models.DeleteDataCenterRequest,
    ) -> cassandra_20190101_models.DeleteDataCenterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_center_with_options(request, runtime)

    async def delete_data_center_async(
        self,
        request: cassandra_20190101_models.DeleteDataCenterRequest,
    ) -> cassandra_20190101_models.DeleteDataCenterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_center_with_options_async(request, runtime)

    def delete_node_tool_execution_history_with_options(
        self,
        request: cassandra_20190101_models.DeleteNodeToolExecutionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DeleteNodeToolExecutionHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DeleteNodeToolExecutionHistoryResponse().from_map(
            self.do_rpcrequest('DeleteNodeToolExecutionHistory', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_node_tool_execution_history_with_options_async(
        self,
        request: cassandra_20190101_models.DeleteNodeToolExecutionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DeleteNodeToolExecutionHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DeleteNodeToolExecutionHistoryResponse().from_map(
            await self.do_rpcrequest_async('DeleteNodeToolExecutionHistory', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_node_tool_execution_history(
        self,
        request: cassandra_20190101_models.DeleteNodeToolExecutionHistoryRequest,
    ) -> cassandra_20190101_models.DeleteNodeToolExecutionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_node_tool_execution_history_with_options(request, runtime)

    async def delete_node_tool_execution_history_async(
        self,
        request: cassandra_20190101_models.DeleteNodeToolExecutionHistoryRequest,
    ) -> cassandra_20190101_models.DeleteNodeToolExecutionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_node_tool_execution_history_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: cassandra_20190101_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeAccountsResponse().from_map(
            self.do_rpcrequest('DescribeAccounts', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeAccountsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccounts', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(
        self,
        request: cassandra_20190101_models.DescribeAccountsRequest,
    ) -> cassandra_20190101_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: cassandra_20190101_models.DescribeAccountsRequest,
    ) -> cassandra_20190101_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_backup_with_options(
        self,
        request: cassandra_20190101_models.DescribeBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeBackupResponse().from_map(
            self.do_rpcrequest('DescribeBackup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeBackupResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup(
        self,
        request: cassandra_20190101_models.DescribeBackupRequest,
    ) -> cassandra_20190101_models.DescribeBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_with_options(request, runtime)

    async def describe_backup_async(
        self,
        request: cassandra_20190101_models.DescribeBackupRequest,
    ) -> cassandra_20190101_models.DescribeBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_with_options_async(request, runtime)

    def describe_backup_plan_with_options(
        self,
        request: cassandra_20190101_models.DescribeBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeBackupPlanResponse().from_map(
            self.do_rpcrequest('DescribeBackupPlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_plan_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupPlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_plan(
        self,
        request: cassandra_20190101_models.DescribeBackupPlanRequest,
    ) -> cassandra_20190101_models.DescribeBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plan_with_options(request, runtime)

    async def describe_backup_plan_async(
        self,
        request: cassandra_20190101_models.DescribeBackupPlanRequest,
    ) -> cassandra_20190101_models.DescribeBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_plan_with_options_async(request, runtime)

    def describe_backup_plans_with_options(
        self,
        request: cassandra_20190101_models.DescribeBackupPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeBackupPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeBackupPlansResponse().from_map(
            self.do_rpcrequest('DescribeBackupPlans', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_plans_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeBackupPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeBackupPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeBackupPlansResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupPlans', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_plans(
        self,
        request: cassandra_20190101_models.DescribeBackupPlansRequest,
    ) -> cassandra_20190101_models.DescribeBackupPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plans_with_options(request, runtime)

    async def describe_backup_plans_async(
        self,
        request: cassandra_20190101_models.DescribeBackupPlansRequest,
    ) -> cassandra_20190101_models.DescribeBackupPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_plans_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: cassandra_20190101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeBackupsResponse().from_map(
            self.do_rpcrequest('DescribeBackups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeBackupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(
        self,
        request: cassandra_20190101_models.DescribeBackupsRequest,
    ) -> cassandra_20190101_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: cassandra_20190101_models.DescribeBackupsRequest,
    ) -> cassandra_20190101_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_cluster_with_options(
        self,
        request: cassandra_20190101_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeClusterResponse().from_map(
            self.do_rpcrequest('DescribeCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeClusterResponse().from_map(
            await self.do_rpcrequest_async('DescribeCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster(
        self,
        request: cassandra_20190101_models.DescribeClusterRequest,
    ) -> cassandra_20190101_models.DescribeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    async def describe_cluster_async(
        self,
        request: cassandra_20190101_models.DescribeClusterRequest,
    ) -> cassandra_20190101_models.DescribeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_with_options_async(request, runtime)

    def describe_cluster_dashboard_with_options(
        self,
        request: cassandra_20190101_models.DescribeClusterDashboardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeClusterDashboardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeClusterDashboardResponse().from_map(
            self.do_rpcrequest('DescribeClusterDashboard', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_dashboard_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeClusterDashboardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeClusterDashboardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeClusterDashboardResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterDashboard', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_dashboard(
        self,
        request: cassandra_20190101_models.DescribeClusterDashboardRequest,
    ) -> cassandra_20190101_models.DescribeClusterDashboardResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_dashboard_with_options(request, runtime)

    async def describe_cluster_dashboard_async(
        self,
        request: cassandra_20190101_models.DescribeClusterDashboardRequest,
    ) -> cassandra_20190101_models.DescribeClusterDashboardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_dashboard_with_options_async(request, runtime)

    def describe_clusters_with_options(
        self,
        request: cassandra_20190101_models.DescribeClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeClustersResponse().from_map(
            self.do_rpcrequest('DescribeClusters', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_clusters_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeClustersResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusters', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_clusters(
        self,
        request: cassandra_20190101_models.DescribeClustersRequest,
    ) -> cassandra_20190101_models.DescribeClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_with_options(request, runtime)

    async def describe_clusters_async(
        self,
        request: cassandra_20190101_models.DescribeClustersRequest,
    ) -> cassandra_20190101_models.DescribeClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_clusters_with_options_async(request, runtime)

    def describe_cluster_status_with_options(
        self,
        request: cassandra_20190101_models.DescribeClusterStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeClusterStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeClusterStatusResponse().from_map(
            self.do_rpcrequest('DescribeClusterStatus', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_status_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeClusterStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeClusterStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeClusterStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterStatus', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_status(
        self,
        request: cassandra_20190101_models.DescribeClusterStatusRequest,
    ) -> cassandra_20190101_models.DescribeClusterStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_status_with_options(request, runtime)

    async def describe_cluster_status_async(
        self,
        request: cassandra_20190101_models.DescribeClusterStatusRequest,
    ) -> cassandra_20190101_models.DescribeClusterStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_status_with_options_async(request, runtime)

    def describe_contact_points_with_options(
        self,
        request: cassandra_20190101_models.DescribeContactPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeContactPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeContactPointsResponse().from_map(
            self.do_rpcrequest('DescribeContactPoints', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_contact_points_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeContactPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeContactPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeContactPointsResponse().from_map(
            await self.do_rpcrequest_async('DescribeContactPoints', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_contact_points(
        self,
        request: cassandra_20190101_models.DescribeContactPointsRequest,
    ) -> cassandra_20190101_models.DescribeContactPointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_points_with_options(request, runtime)

    async def describe_contact_points_async(
        self,
        request: cassandra_20190101_models.DescribeContactPointsRequest,
    ) -> cassandra_20190101_models.DescribeContactPointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_contact_points_with_options_async(request, runtime)

    def describe_data_center_with_options(
        self,
        request: cassandra_20190101_models.DescribeDataCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeDataCenterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeDataCenterResponse().from_map(
            self.do_rpcrequest('DescribeDataCenter', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_center_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeDataCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeDataCenterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeDataCenterResponse().from_map(
            await self.do_rpcrequest_async('DescribeDataCenter', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_center(
        self,
        request: cassandra_20190101_models.DescribeDataCenterRequest,
    ) -> cassandra_20190101_models.DescribeDataCenterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_center_with_options(request, runtime)

    async def describe_data_center_async(
        self,
        request: cassandra_20190101_models.DescribeDataCenterRequest,
    ) -> cassandra_20190101_models.DescribeDataCenterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_center_with_options_async(request, runtime)

    def describe_data_centers_with_options(
        self,
        request: cassandra_20190101_models.DescribeDataCentersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeDataCentersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeDataCentersResponse().from_map(
            self.do_rpcrequest('DescribeDataCenters', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_centers_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeDataCentersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeDataCentersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeDataCentersResponse().from_map(
            await self.do_rpcrequest_async('DescribeDataCenters', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_centers(
        self,
        request: cassandra_20190101_models.DescribeDataCentersRequest,
    ) -> cassandra_20190101_models.DescribeDataCentersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_centers_with_options(request, runtime)

    async def describe_data_centers_async(
        self,
        request: cassandra_20190101_models.DescribeDataCentersRequest,
    ) -> cassandra_20190101_models.DescribeDataCentersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_centers_with_options_async(request, runtime)

    def describe_deleted_clusters_with_options(
        self,
        request: cassandra_20190101_models.DescribeDeletedClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeDeletedClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeDeletedClustersResponse().from_map(
            self.do_rpcrequest('DescribeDeletedClusters', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_deleted_clusters_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeDeletedClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeDeletedClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeDeletedClustersResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeletedClusters', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_deleted_clusters(
        self,
        request: cassandra_20190101_models.DescribeDeletedClustersRequest,
    ) -> cassandra_20190101_models.DescribeDeletedClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deleted_clusters_with_options(request, runtime)

    async def describe_deleted_clusters_async(
        self,
        request: cassandra_20190101_models.DescribeDeletedClustersRequest,
    ) -> cassandra_20190101_models.DescribeDeletedClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deleted_clusters_with_options_async(request, runtime)

    def describe_instance_type_with_options(
        self,
        request: cassandra_20190101_models.DescribeInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeInstanceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeInstanceTypeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceType', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_type_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeInstanceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeInstanceTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceType', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_type(
        self,
        request: cassandra_20190101_models.DescribeInstanceTypeRequest,
    ) -> cassandra_20190101_models.DescribeInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_type_with_options(request, runtime)

    async def describe_instance_type_async(
        self,
        request: cassandra_20190101_models.DescribeInstanceTypeRequest,
    ) -> cassandra_20190101_models.DescribeInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_type_with_options_async(request, runtime)

    def describe_ip_whitelist_with_options(
        self,
        request: cassandra_20190101_models.DescribeIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeIpWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeIpWhitelistResponse().from_map(
            self.do_rpcrequest('DescribeIpWhitelist', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ip_whitelist_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeIpWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeIpWhitelistResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpWhitelist', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ip_whitelist(
        self,
        request: cassandra_20190101_models.DescribeIpWhitelistRequest,
    ) -> cassandra_20190101_models.DescribeIpWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_whitelist_with_options(request, runtime)

    async def describe_ip_whitelist_async(
        self,
        request: cassandra_20190101_models.DescribeIpWhitelistRequest,
    ) -> cassandra_20190101_models.DescribeIpWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_whitelist_with_options_async(request, runtime)

    def describe_ip_whitelist_groups_with_options(
        self,
        request: cassandra_20190101_models.DescribeIpWhitelistGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeIpWhitelistGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeIpWhitelistGroupsResponse().from_map(
            self.do_rpcrequest('DescribeIpWhitelistGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ip_whitelist_groups_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeIpWhitelistGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeIpWhitelistGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeIpWhitelistGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpWhitelistGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ip_whitelist_groups(
        self,
        request: cassandra_20190101_models.DescribeIpWhitelistGroupsRequest,
    ) -> cassandra_20190101_models.DescribeIpWhitelistGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_whitelist_groups_with_options(request, runtime)

    async def describe_ip_whitelist_groups_async(
        self,
        request: cassandra_20190101_models.DescribeIpWhitelistGroupsRequest,
    ) -> cassandra_20190101_models.DescribeIpWhitelistGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_whitelist_groups_with_options_async(request, runtime)

    def describe_node_tool_execution_histories_with_options(
        self,
        request: cassandra_20190101_models.DescribeNodeToolExecutionHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeNodeToolExecutionHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeNodeToolExecutionHistoriesResponse().from_map(
            self.do_rpcrequest('DescribeNodeToolExecutionHistories', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_node_tool_execution_histories_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeNodeToolExecutionHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeNodeToolExecutionHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeNodeToolExecutionHistoriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeNodeToolExecutionHistories', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_node_tool_execution_histories(
        self,
        request: cassandra_20190101_models.DescribeNodeToolExecutionHistoriesRequest,
    ) -> cassandra_20190101_models.DescribeNodeToolExecutionHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_node_tool_execution_histories_with_options(request, runtime)

    async def describe_node_tool_execution_histories_async(
        self,
        request: cassandra_20190101_models.DescribeNodeToolExecutionHistoriesRequest,
    ) -> cassandra_20190101_models.DescribeNodeToolExecutionHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_tool_execution_histories_with_options_async(request, runtime)

    def describe_node_tool_execution_history_with_options(
        self,
        request: cassandra_20190101_models.DescribeNodeToolExecutionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeNodeToolExecutionHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeNodeToolExecutionHistoryResponse().from_map(
            self.do_rpcrequest('DescribeNodeToolExecutionHistory', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_node_tool_execution_history_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeNodeToolExecutionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeNodeToolExecutionHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeNodeToolExecutionHistoryResponse().from_map(
            await self.do_rpcrequest_async('DescribeNodeToolExecutionHistory', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_node_tool_execution_history(
        self,
        request: cassandra_20190101_models.DescribeNodeToolExecutionHistoryRequest,
    ) -> cassandra_20190101_models.DescribeNodeToolExecutionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_node_tool_execution_history_with_options(request, runtime)

    async def describe_node_tool_execution_history_async(
        self,
        request: cassandra_20190101_models.DescribeNodeToolExecutionHistoryRequest,
    ) -> cassandra_20190101_models.DescribeNodeToolExecutionHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_tool_execution_history_with_options_async(request, runtime)

    def describe_parameter_modification_histories_with_options(
        self,
        request: cassandra_20190101_models.DescribeParameterModificationHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeParameterModificationHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeParameterModificationHistoriesResponse().from_map(
            self.do_rpcrequest('DescribeParameterModificationHistories', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameter_modification_histories_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeParameterModificationHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeParameterModificationHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeParameterModificationHistoriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeParameterModificationHistories', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_modification_histories(
        self,
        request: cassandra_20190101_models.DescribeParameterModificationHistoriesRequest,
    ) -> cassandra_20190101_models.DescribeParameterModificationHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_modification_histories_with_options(request, runtime)

    async def describe_parameter_modification_histories_async(
        self,
        request: cassandra_20190101_models.DescribeParameterModificationHistoriesRequest,
    ) -> cassandra_20190101_models.DescribeParameterModificationHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_modification_histories_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: cassandra_20190101_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeParametersResponse().from_map(
            self.do_rpcrequest('DescribeParameters', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeParametersResponse().from_map(
            await self.do_rpcrequest_async('DescribeParameters', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameters(
        self,
        request: cassandra_20190101_models.DescribeParametersRequest,
    ) -> cassandra_20190101_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: cassandra_20190101_models.DescribeParametersRequest,
    ) -> cassandra_20190101_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: cassandra_20190101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: cassandra_20190101_models.DescribeRegionsRequest,
    ) -> cassandra_20190101_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: cassandra_20190101_models.DescribeRegionsRequest,
    ) -> cassandra_20190101_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_security_groups_with_options(
        self,
        request: cassandra_20190101_models.DescribeSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeSecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeSecurityGroupsResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_groups_with_options_async(
        self,
        request: cassandra_20190101_models.DescribeSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.DescribeSecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.DescribeSecurityGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_groups(
        self,
        request: cassandra_20190101_models.DescribeSecurityGroupsRequest,
    ) -> cassandra_20190101_models.DescribeSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_groups_with_options(request, runtime)

    async def describe_security_groups_async(
        self,
        request: cassandra_20190101_models.DescribeSecurityGroupsRequest,
    ) -> cassandra_20190101_models.DescribeSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_groups_with_options_async(request, runtime)

    def execute_node_tool_with_options(
        self,
        request: cassandra_20190101_models.ExecuteNodeToolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ExecuteNodeToolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ExecuteNodeToolResponse().from_map(
            self.do_rpcrequest('ExecuteNodeTool', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_node_tool_with_options_async(
        self,
        request: cassandra_20190101_models.ExecuteNodeToolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ExecuteNodeToolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ExecuteNodeToolResponse().from_map(
            await self.do_rpcrequest_async('ExecuteNodeTool', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_node_tool(
        self,
        request: cassandra_20190101_models.ExecuteNodeToolRequest,
    ) -> cassandra_20190101_models.ExecuteNodeToolResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_node_tool_with_options(request, runtime)

    async def execute_node_tool_async(
        self,
        request: cassandra_20190101_models.ExecuteNodeToolRequest,
    ) -> cassandra_20190101_models.ExecuteNodeToolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_node_tool_with_options_async(request, runtime)

    def get_cms_url_with_options(
        self,
        request: cassandra_20190101_models.GetCmsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.GetCmsUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.GetCmsUrlResponse().from_map(
            self.do_rpcrequest('GetCmsUrl', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_cms_url_with_options_async(
        self,
        request: cassandra_20190101_models.GetCmsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.GetCmsUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.GetCmsUrlResponse().from_map(
            await self.do_rpcrequest_async('GetCmsUrl', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_cms_url(
        self,
        request: cassandra_20190101_models.GetCmsUrlRequest,
    ) -> cassandra_20190101_models.GetCmsUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cms_url_with_options(request, runtime)

    async def get_cms_url_async(
        self,
        request: cassandra_20190101_models.GetCmsUrlRequest,
    ) -> cassandra_20190101_models.GetCmsUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cms_url_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: cassandra_20190101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: cassandra_20190101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: cassandra_20190101_models.ListTagResourcesRequest,
    ) -> cassandra_20190101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: cassandra_20190101_models.ListTagResourcesRequest,
    ) -> cassandra_20190101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tags_with_options(
        self,
        request: cassandra_20190101_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ListTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ListTagsResponse().from_map(
            self.do_rpcrequest('ListTags', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: cassandra_20190101_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ListTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ListTagsResponse().from_map(
            await self.do_rpcrequest_async('ListTags', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tags(
        self,
        request: cassandra_20190101_models.ListTagsRequest,
    ) -> cassandra_20190101_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    async def list_tags_async(
        self,
        request: cassandra_20190101_models.ListTagsRequest,
    ) -> cassandra_20190101_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_with_options_async(request, runtime)

    def modify_account_password_with_options(
        self,
        request: cassandra_20190101_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyAccountPasswordResponse().from_map(
            self.do_rpcrequest('ModifyAccountPassword', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_password_with_options_async(
        self,
        request: cassandra_20190101_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyAccountPasswordResponse().from_map(
            await self.do_rpcrequest_async('ModifyAccountPassword', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_password(
        self,
        request: cassandra_20190101_models.ModifyAccountPasswordRequest,
    ) -> cassandra_20190101_models.ModifyAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_password_with_options(request, runtime)

    async def modify_account_password_async(
        self,
        request: cassandra_20190101_models.ModifyAccountPasswordRequest,
    ) -> cassandra_20190101_models.ModifyAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_password_with_options_async(request, runtime)

    def modify_backup_plan_with_options(
        self,
        request: cassandra_20190101_models.ModifyBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyBackupPlanResponse().from_map(
            self.do_rpcrequest('ModifyBackupPlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_plan_with_options_async(
        self,
        request: cassandra_20190101_models.ModifyBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupPlan', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_plan(
        self,
        request: cassandra_20190101_models.ModifyBackupPlanRequest,
    ) -> cassandra_20190101_models.ModifyBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_plan_with_options(request, runtime)

    async def modify_backup_plan_async(
        self,
        request: cassandra_20190101_models.ModifyBackupPlanRequest,
    ) -> cassandra_20190101_models.ModifyBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_plan_with_options_async(request, runtime)

    def modify_cluster_with_options(
        self,
        request: cassandra_20190101_models.ModifyClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyClusterResponse().from_map(
            self.do_rpcrequest('ModifyCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_with_options_async(
        self,
        request: cassandra_20190101_models.ModifyClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyClusterResponse().from_map(
            await self.do_rpcrequest_async('ModifyCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster(
        self,
        request: cassandra_20190101_models.ModifyClusterRequest,
    ) -> cassandra_20190101_models.ModifyClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_with_options(request, runtime)

    async def modify_cluster_async(
        self,
        request: cassandra_20190101_models.ModifyClusterRequest,
    ) -> cassandra_20190101_models.ModifyClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_with_options_async(request, runtime)

    def modify_data_center_with_options(
        self,
        request: cassandra_20190101_models.ModifyDataCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyDataCenterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyDataCenterResponse().from_map(
            self.do_rpcrequest('ModifyDataCenter', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_data_center_with_options_async(
        self,
        request: cassandra_20190101_models.ModifyDataCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyDataCenterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyDataCenterResponse().from_map(
            await self.do_rpcrequest_async('ModifyDataCenter', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_data_center(
        self,
        request: cassandra_20190101_models.ModifyDataCenterRequest,
    ) -> cassandra_20190101_models.ModifyDataCenterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_data_center_with_options(request, runtime)

    async def modify_data_center_async(
        self,
        request: cassandra_20190101_models.ModifyDataCenterRequest,
    ) -> cassandra_20190101_models.ModifyDataCenterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_center_with_options_async(request, runtime)

    def modify_instance_maintain_time_with_options(
        self,
        request: cassandra_20190101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyInstanceMaintainTimeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceMaintainTime', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_maintain_time_with_options_async(
        self,
        request: cassandra_20190101_models.ModifyInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyInstanceMaintainTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceMaintainTime', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_maintain_time(
        self,
        request: cassandra_20190101_models.ModifyInstanceMaintainTimeRequest,
    ) -> cassandra_20190101_models.ModifyInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintain_time_with_options(request, runtime)

    async def modify_instance_maintain_time_async(
        self,
        request: cassandra_20190101_models.ModifyInstanceMaintainTimeRequest,
    ) -> cassandra_20190101_models.ModifyInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_maintain_time_with_options_async(request, runtime)

    def modify_instance_type_with_options(
        self,
        request: cassandra_20190101_models.ModifyInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyInstanceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyInstanceTypeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceType', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_type_with_options_async(
        self,
        request: cassandra_20190101_models.ModifyInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyInstanceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyInstanceTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceType', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_type(
        self,
        request: cassandra_20190101_models.ModifyInstanceTypeRequest,
    ) -> cassandra_20190101_models.ModifyInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_type_with_options(request, runtime)

    async def modify_instance_type_async(
        self,
        request: cassandra_20190101_models.ModifyInstanceTypeRequest,
    ) -> cassandra_20190101_models.ModifyInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_type_with_options_async(request, runtime)

    def modify_ip_whitelist_with_options(
        self,
        request: cassandra_20190101_models.ModifyIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyIpWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyIpWhitelistResponse().from_map(
            self.do_rpcrequest('ModifyIpWhitelist', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ip_whitelist_with_options_async(
        self,
        request: cassandra_20190101_models.ModifyIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyIpWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyIpWhitelistResponse().from_map(
            await self.do_rpcrequest_async('ModifyIpWhitelist', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ip_whitelist(
        self,
        request: cassandra_20190101_models.ModifyIpWhitelistRequest,
    ) -> cassandra_20190101_models.ModifyIpWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_whitelist_with_options(request, runtime)

    async def modify_ip_whitelist_async(
        self,
        request: cassandra_20190101_models.ModifyIpWhitelistRequest,
    ) -> cassandra_20190101_models.ModifyIpWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_whitelist_with_options_async(request, runtime)

    def modify_ip_whitelist_group_with_options(
        self,
        request: cassandra_20190101_models.ModifyIpWhitelistGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyIpWhitelistGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyIpWhitelistGroupResponse().from_map(
            self.do_rpcrequest('ModifyIpWhitelistGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ip_whitelist_group_with_options_async(
        self,
        request: cassandra_20190101_models.ModifyIpWhitelistGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyIpWhitelistGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyIpWhitelistGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyIpWhitelistGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ip_whitelist_group(
        self,
        request: cassandra_20190101_models.ModifyIpWhitelistGroupRequest,
    ) -> cassandra_20190101_models.ModifyIpWhitelistGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_whitelist_group_with_options(request, runtime)

    async def modify_ip_whitelist_group_async(
        self,
        request: cassandra_20190101_models.ModifyIpWhitelistGroupRequest,
    ) -> cassandra_20190101_models.ModifyIpWhitelistGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_whitelist_group_with_options_async(request, runtime)

    def modify_parameter_with_options(
        self,
        request: cassandra_20190101_models.ModifyParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyParameterResponse().from_map(
            self.do_rpcrequest('ModifyParameter', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_parameter_with_options_async(
        self,
        request: cassandra_20190101_models.ModifyParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifyParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifyParameterResponse().from_map(
            await self.do_rpcrequest_async('ModifyParameter', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parameter(
        self,
        request: cassandra_20190101_models.ModifyParameterRequest,
    ) -> cassandra_20190101_models.ModifyParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    async def modify_parameter_async(
        self,
        request: cassandra_20190101_models.ModifyParameterRequest,
    ) -> cassandra_20190101_models.ModifyParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameter_with_options_async(request, runtime)

    def modify_security_groups_with_options(
        self,
        request: cassandra_20190101_models.ModifySecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifySecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifySecurityGroupsResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_groups_with_options_async(
        self,
        request: cassandra_20190101_models.ModifySecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ModifySecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ModifySecurityGroupsResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_groups(
        self,
        request: cassandra_20190101_models.ModifySecurityGroupsRequest,
    ) -> cassandra_20190101_models.ModifySecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_groups_with_options(request, runtime)

    async def modify_security_groups_async(
        self,
        request: cassandra_20190101_models.ModifySecurityGroupsRequest,
    ) -> cassandra_20190101_models.ModifySecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_groups_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: cassandra_20190101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.MoveResourceGroupResponse().from_map(
            self.do_rpcrequest('MoveResourceGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: cassandra_20190101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.MoveResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('MoveResourceGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        request: cassandra_20190101_models.MoveResourceGroupRequest,
    ) -> cassandra_20190101_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: cassandra_20190101_models.MoveResourceGroupRequest,
    ) -> cassandra_20190101_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def purge_cluster_with_options(
        self,
        request: cassandra_20190101_models.PurgeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.PurgeClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.PurgeClusterResponse().from_map(
            self.do_rpcrequest('PurgeCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def purge_cluster_with_options_async(
        self,
        request: cassandra_20190101_models.PurgeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.PurgeClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.PurgeClusterResponse().from_map(
            await self.do_rpcrequest_async('PurgeCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def purge_cluster(
        self,
        request: cassandra_20190101_models.PurgeClusterRequest,
    ) -> cassandra_20190101_models.PurgeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.purge_cluster_with_options(request, runtime)

    async def purge_cluster_async(
        self,
        request: cassandra_20190101_models.PurgeClusterRequest,
    ) -> cassandra_20190101_models.PurgeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purge_cluster_with_options_async(request, runtime)

    def reboot_cluster_with_options(
        self,
        request: cassandra_20190101_models.RebootClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.RebootClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.RebootClusterResponse().from_map(
            self.do_rpcrequest('RebootCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reboot_cluster_with_options_async(
        self,
        request: cassandra_20190101_models.RebootClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.RebootClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.RebootClusterResponse().from_map(
            await self.do_rpcrequest_async('RebootCluster', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_cluster(
        self,
        request: cassandra_20190101_models.RebootClusterRequest,
    ) -> cassandra_20190101_models.RebootClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_cluster_with_options(request, runtime)

    async def reboot_cluster_async(
        self,
        request: cassandra_20190101_models.RebootClusterRequest,
    ) -> cassandra_20190101_models.RebootClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_cluster_with_options_async(request, runtime)

    def release_public_contact_points_with_options(
        self,
        request: cassandra_20190101_models.ReleasePublicContactPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ReleasePublicContactPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ReleasePublicContactPointsResponse().from_map(
            self.do_rpcrequest('ReleasePublicContactPoints', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_public_contact_points_with_options_async(
        self,
        request: cassandra_20190101_models.ReleasePublicContactPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ReleasePublicContactPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ReleasePublicContactPointsResponse().from_map(
            await self.do_rpcrequest_async('ReleasePublicContactPoints', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_public_contact_points(
        self,
        request: cassandra_20190101_models.ReleasePublicContactPointsRequest,
    ) -> cassandra_20190101_models.ReleasePublicContactPointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_public_contact_points_with_options(request, runtime)

    async def release_public_contact_points_async(
        self,
        request: cassandra_20190101_models.ReleasePublicContactPointsRequest,
    ) -> cassandra_20190101_models.ReleasePublicContactPointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_public_contact_points_with_options_async(request, runtime)

    def resize_disk_size_with_options(
        self,
        request: cassandra_20190101_models.ResizeDiskSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ResizeDiskSizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ResizeDiskSizeResponse().from_map(
            self.do_rpcrequest('ResizeDiskSize', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_disk_size_with_options_async(
        self,
        request: cassandra_20190101_models.ResizeDiskSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ResizeDiskSizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ResizeDiskSizeResponse().from_map(
            await self.do_rpcrequest_async('ResizeDiskSize', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resize_disk_size(
        self,
        request: cassandra_20190101_models.ResizeDiskSizeRequest,
    ) -> cassandra_20190101_models.ResizeDiskSizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_disk_size_with_options(request, runtime)

    async def resize_disk_size_async(
        self,
        request: cassandra_20190101_models.ResizeDiskSizeRequest,
    ) -> cassandra_20190101_models.ResizeDiskSizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_disk_size_with_options_async(request, runtime)

    def resize_node_count_with_options(
        self,
        request: cassandra_20190101_models.ResizeNodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ResizeNodeCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ResizeNodeCountResponse().from_map(
            self.do_rpcrequest('ResizeNodeCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_node_count_with_options_async(
        self,
        request: cassandra_20190101_models.ResizeNodeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.ResizeNodeCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.ResizeNodeCountResponse().from_map(
            await self.do_rpcrequest_async('ResizeNodeCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resize_node_count(
        self,
        request: cassandra_20190101_models.ResizeNodeCountRequest,
    ) -> cassandra_20190101_models.ResizeNodeCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_node_count_with_options(request, runtime)

    async def resize_node_count_async(
        self,
        request: cassandra_20190101_models.ResizeNodeCountRequest,
    ) -> cassandra_20190101_models.ResizeNodeCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_node_count_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: cassandra_20190101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: cassandra_20190101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: cassandra_20190101_models.TagResourcesRequest,
    ) -> cassandra_20190101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: cassandra_20190101_models.TagResourcesRequest,
    ) -> cassandra_20190101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: cassandra_20190101_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.UnTagResourcesResponse().from_map(
            self.do_rpcrequest('UnTagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: cassandra_20190101_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.UnTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UnTagResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def un_tag_resources(
        self,
        request: cassandra_20190101_models.UnTagResourcesRequest,
    ) -> cassandra_20190101_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: cassandra_20190101_models.UnTagResourcesRequest,
    ) -> cassandra_20190101_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def upgrade_cluster_version_with_options(
        self,
        request: cassandra_20190101_models.UpgradeClusterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.UpgradeClusterVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.UpgradeClusterVersionResponse().from_map(
            self.do_rpcrequest('UpgradeClusterVersion', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_cluster_version_with_options_async(
        self,
        request: cassandra_20190101_models.UpgradeClusterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cassandra_20190101_models.UpgradeClusterVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cassandra_20190101_models.UpgradeClusterVersionResponse().from_map(
            await self.do_rpcrequest_async('UpgradeClusterVersion', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_cluster_version(
        self,
        request: cassandra_20190101_models.UpgradeClusterVersionRequest,
    ) -> cassandra_20190101_models.UpgradeClusterVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_cluster_version_with_options(request, runtime)

    async def upgrade_cluster_version_async(
        self,
        request: cassandra_20190101_models.UpgradeClusterVersionRequest,
    ) -> cassandra_20190101_models.UpgradeClusterVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_cluster_version_with_options_async(request, runtime)
