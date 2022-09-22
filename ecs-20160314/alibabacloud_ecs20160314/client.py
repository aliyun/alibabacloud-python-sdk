# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ecs20160314 import models as ecs_20160314_models
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
            'cn-hangzhou': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'ecs.aliyuncs.com',
            'ap-northeast-2-pop': 'ecs.aliyuncs.com',
            'cn-beijing-finance-pop': 'ecs.aliyuncs.com',
            'cn-beijing-gov-1': 'ecs.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-edge-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'cn-fujian': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-finance': 'ecs.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-test-306': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ecs.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-inner': 'ecs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-inner': 'ecs.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-wuhan': 'ecs.aliyuncs.com',
            'cn-yushanfang': 'ecs.aliyuncs.com',
            'cn-zhangbei': 'ecs.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ecs.cn-zhangjiakou.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'eu-west-1-oxs': 'ecs.cn-shenzhen-cloudstone.aliyuncs.com',
            'rus-west-1-pop': 'ecs.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_migratable_instances_with_options(
        self,
        request: ecs_20160314_models.AddMigratableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.AddMigratableInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_migration_type):
            query['BusinessMigrationType'] = request.business_migration_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMigratableInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.AddMigratableInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_migratable_instances_with_options_async(
        self,
        request: ecs_20160314_models.AddMigratableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.AddMigratableInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_migration_type):
            query['BusinessMigrationType'] = request.business_migration_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMigratableInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.AddMigratableInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_migratable_instances(
        self,
        request: ecs_20160314_models.AddMigratableInstancesRequest,
    ) -> ecs_20160314_models.AddMigratableInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_migratable_instances_with_options(request, runtime)

    async def add_migratable_instances_async(
        self,
        request: ecs_20160314_models.AddMigratableInstancesRequest,
    ) -> ecs_20160314_models.AddMigratableInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_migratable_instances_with_options_async(request, runtime)

    def allocate_dedicated_hosts_with_options(
        self,
        request: ecs_20160314_models.AllocateDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.AllocateDedicatedHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_on_maintenance):
            query['ActionOnMaintenance'] = request.action_on_maintenance
        if not UtilClient.is_unset(request.auto_placement):
            query['AutoPlacement'] = request.auto_placement
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cpu_over_commit_ratio):
            query['CpuOverCommitRatio'] = request.cpu_over_commit_ratio
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.dedicated_host_type):
            query['DedicatedHostType'] = request.dedicated_host_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.min_quantity):
            query['MinQuantity'] = request.min_quantity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.network_attributes):
            query['NetworkAttributes'] = request.network_attributes
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateDedicatedHosts',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.AllocateDedicatedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_dedicated_hosts_with_options_async(
        self,
        request: ecs_20160314_models.AllocateDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.AllocateDedicatedHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_on_maintenance):
            query['ActionOnMaintenance'] = request.action_on_maintenance
        if not UtilClient.is_unset(request.auto_placement):
            query['AutoPlacement'] = request.auto_placement
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cpu_over_commit_ratio):
            query['CpuOverCommitRatio'] = request.cpu_over_commit_ratio
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.dedicated_host_type):
            query['DedicatedHostType'] = request.dedicated_host_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.min_quantity):
            query['MinQuantity'] = request.min_quantity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.network_attributes):
            query['NetworkAttributes'] = request.network_attributes
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateDedicatedHosts',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.AllocateDedicatedHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_dedicated_hosts(
        self,
        request: ecs_20160314_models.AllocateDedicatedHostsRequest,
    ) -> ecs_20160314_models.AllocateDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_dedicated_hosts_with_options(request, runtime)

    async def allocate_dedicated_hosts_async(
        self,
        request: ecs_20160314_models.AllocateDedicatedHostsRequest,
    ) -> ecs_20160314_models.AllocateDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_dedicated_hosts_with_options_async(request, runtime)

    def cancel_migration_instances_with_options(
        self,
        request: ecs_20160314_models.CancelMigrationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CancelMigrationInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
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
            action='CancelMigrationInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CancelMigrationInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_migration_instances_with_options_async(
        self,
        request: ecs_20160314_models.CancelMigrationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CancelMigrationInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
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
            action='CancelMigrationInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CancelMigrationInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_migration_instances(
        self,
        request: ecs_20160314_models.CancelMigrationInstancesRequest,
    ) -> ecs_20160314_models.CancelMigrationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_migration_instances_with_options(request, runtime)

    async def cancel_migration_instances_async(
        self,
        request: ecs_20160314_models.CancelMigrationInstancesRequest,
    ) -> ecs_20160314_models.CancelMigrationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_migration_instances_with_options_async(request, runtime)

    def cancel_migration_plan_with_options(
        self,
        request: ecs_20160314_models.CancelMigrationPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CancelMigrationPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_plan_id):
            query['MigrationPlanId'] = request.migration_plan_id
        if not UtilClient.is_unset(request.only_cancel_plan):
            query['OnlyCancelPlan'] = request.only_cancel_plan
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
            action='CancelMigrationPlan',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CancelMigrationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_migration_plan_with_options_async(
        self,
        request: ecs_20160314_models.CancelMigrationPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CancelMigrationPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_plan_id):
            query['MigrationPlanId'] = request.migration_plan_id
        if not UtilClient.is_unset(request.only_cancel_plan):
            query['OnlyCancelPlan'] = request.only_cancel_plan
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
            action='CancelMigrationPlan',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CancelMigrationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_migration_plan(
        self,
        request: ecs_20160314_models.CancelMigrationPlanRequest,
    ) -> ecs_20160314_models.CancelMigrationPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_migration_plan_with_options(request, runtime)

    async def cancel_migration_plan_async(
        self,
        request: ecs_20160314_models.CancelMigrationPlanRequest,
    ) -> ecs_20160314_models.CancelMigrationPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_migration_plan_with_options_async(request, runtime)

    def configure_security_group_permissions_with_options(
        self,
        request: ecs_20160314_models.ConfigureSecurityGroupPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ConfigureSecurityGroupPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize_permission):
            query['AuthorizePermission'] = request.authorize_permission
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.revoke_permission):
            query['RevokePermission'] = request.revoke_permission
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSecurityGroupPermissions',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ConfigureSecurityGroupPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_security_group_permissions_with_options_async(
        self,
        request: ecs_20160314_models.ConfigureSecurityGroupPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ConfigureSecurityGroupPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize_permission):
            query['AuthorizePermission'] = request.authorize_permission
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.revoke_permission):
            query['RevokePermission'] = request.revoke_permission
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSecurityGroupPermissions',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ConfigureSecurityGroupPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_security_group_permissions(
        self,
        request: ecs_20160314_models.ConfigureSecurityGroupPermissionsRequest,
    ) -> ecs_20160314_models.ConfigureSecurityGroupPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_security_group_permissions_with_options(request, runtime)

    async def configure_security_group_permissions_async(
        self,
        request: ecs_20160314_models.ConfigureSecurityGroupPermissionsRequest,
    ) -> ecs_20160314_models.ConfigureSecurityGroupPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_security_group_permissions_with_options_async(request, runtime)

    def confirm_reservation_demand_with_options(
        self,
        request: ecs_20160314_models.ConfirmReservationDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ConfirmReservationDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmReservationDemand',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ConfirmReservationDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_reservation_demand_with_options_async(
        self,
        request: ecs_20160314_models.ConfirmReservationDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ConfirmReservationDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmReservationDemand',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ConfirmReservationDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_reservation_demand(
        self,
        request: ecs_20160314_models.ConfirmReservationDemandRequest,
    ) -> ecs_20160314_models.ConfirmReservationDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_reservation_demand_with_options(request, runtime)

    async def confirm_reservation_demand_async(
        self,
        request: ecs_20160314_models.ConfirmReservationDemandRequest,
    ) -> ecs_20160314_models.ConfirmReservationDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_reservation_demand_with_options_async(request, runtime)

    def create_capacity_reservation_with_options(
        self,
        request: ecs_20160314_models.CreateCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateCapacityReservationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity_reservation_name):
            query['CapacityReservationName'] = request.capacity_reservation_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_date_type):
            query['EndDateType'] = request.end_date_type
        if not UtilClient.is_unset(request.instance_count):
            query['InstanceCount'] = request.instance_count
        if not UtilClient.is_unset(request.instance_match_criteria):
            query['InstanceMatchCriteria'] = request.instance_match_criteria
        if not UtilClient.is_unset(request.instance_platform):
            query['InstancePlatform'] = request.instance_platform
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.time_slot):
            query['TimeSlot'] = request.time_slot
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCapacityReservation',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateCapacityReservationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_capacity_reservation_with_options_async(
        self,
        request: ecs_20160314_models.CreateCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateCapacityReservationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity_reservation_name):
            query['CapacityReservationName'] = request.capacity_reservation_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_date_type):
            query['EndDateType'] = request.end_date_type
        if not UtilClient.is_unset(request.instance_count):
            query['InstanceCount'] = request.instance_count
        if not UtilClient.is_unset(request.instance_match_criteria):
            query['InstanceMatchCriteria'] = request.instance_match_criteria
        if not UtilClient.is_unset(request.instance_platform):
            query['InstancePlatform'] = request.instance_platform
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.time_slot):
            query['TimeSlot'] = request.time_slot
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCapacityReservation',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateCapacityReservationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_capacity_reservation(
        self,
        request: ecs_20160314_models.CreateCapacityReservationRequest,
    ) -> ecs_20160314_models.CreateCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_capacity_reservation_with_options(request, runtime)

    async def create_capacity_reservation_async(
        self,
        request: ecs_20160314_models.CreateCapacityReservationRequest,
    ) -> ecs_20160314_models.CreateCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_capacity_reservation_with_options_async(request, runtime)

    def create_dedicated_block_storage_cluster_with_options(
        self,
        request: ecs_20160314_models.CreateDedicatedBlockStorageClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDedicatedBlockStorageClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_block_storage_cluster_name):
            query['DedicatedBlockStorageClusterName'] = request.dedicated_block_storage_cluster_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedBlockStorageCluster',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDedicatedBlockStorageClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_block_storage_cluster_with_options_async(
        self,
        request: ecs_20160314_models.CreateDedicatedBlockStorageClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDedicatedBlockStorageClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_block_storage_cluster_name):
            query['DedicatedBlockStorageClusterName'] = request.dedicated_block_storage_cluster_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedBlockStorageCluster',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDedicatedBlockStorageClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_block_storage_cluster(
        self,
        request: ecs_20160314_models.CreateDedicatedBlockStorageClusterRequest,
    ) -> ecs_20160314_models.CreateDedicatedBlockStorageClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_block_storage_cluster_with_options(request, runtime)

    async def create_dedicated_block_storage_cluster_async(
        self,
        request: ecs_20160314_models.CreateDedicatedBlockStorageClusterRequest,
    ) -> ecs_20160314_models.CreateDedicatedBlockStorageClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_block_storage_cluster_with_options_async(request, runtime)

    def create_dedicated_host_cluster_with_options(
        self,
        request: ecs_20160314_models.CreateDedicatedHostClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDedicatedHostClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_name):
            query['DedicatedHostClusterName'] = request.dedicated_host_cluster_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostCluster',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDedicatedHostClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_host_cluster_with_options_async(
        self,
        request: ecs_20160314_models.CreateDedicatedHostClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDedicatedHostClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_name):
            query['DedicatedHostClusterName'] = request.dedicated_host_cluster_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostCluster',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDedicatedHostClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_host_cluster(
        self,
        request: ecs_20160314_models.CreateDedicatedHostClusterRequest,
    ) -> ecs_20160314_models.CreateDedicatedHostClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_cluster_with_options(request, runtime)

    async def create_dedicated_host_cluster_async(
        self,
        request: ecs_20160314_models.CreateDedicatedHostClusterRequest,
    ) -> ecs_20160314_models.CreateDedicatedHostClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_cluster_with_options_async(request, runtime)

    def create_default_auto_snapshot_policy_with_options(
        self,
        request: ecs_20160314_models.CreateDefaultAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDefaultAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='CreateDefaultAutoSnapshotPolicy',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDefaultAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_default_auto_snapshot_policy_with_options_async(
        self,
        request: ecs_20160314_models.CreateDefaultAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDefaultAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='CreateDefaultAutoSnapshotPolicy',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDefaultAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_default_auto_snapshot_policy(
        self,
        request: ecs_20160314_models.CreateDefaultAutoSnapshotPolicyRequest,
    ) -> ecs_20160314_models.CreateDefaultAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_default_auto_snapshot_policy_with_options(request, runtime)

    async def create_default_auto_snapshot_policy_async(
        self,
        request: ecs_20160314_models.CreateDefaultAutoSnapshotPolicyRequest,
    ) -> ecs_20160314_models.CreateDefaultAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_default_auto_snapshot_policy_with_options_async(request, runtime)

    def create_diagnose_with_options(
        self,
        request: ecs_20160314_models.CreateDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDiagnoseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.diagnose_action):
            query['DiagnoseAction'] = request.diagnose_action
        if not UtilClient.is_unset(request.diagnose_error_code):
            query['DiagnoseErrorCode'] = request.diagnose_error_code
        if not UtilClient.is_unset(request.diagnose_product):
            query['DiagnoseProduct'] = request.diagnose_product
        if not UtilClient.is_unset(request.diagnose_request_id):
            query['DiagnoseRequestId'] = request.diagnose_request_id
        if not UtilClient.is_unset(request.diagnose_request_params):
            query['DiagnoseRequestParams'] = request.diagnose_request_params
        if not UtilClient.is_unset(request.diagnose_response):
            query['DiagnoseResponse'] = request.diagnose_response
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type_name):
            query['InstanceTypeName'] = request.instance_type_name
        if not UtilClient.is_unset(request.iz_no):
            query['IzNo'] = request.iz_no
        if not UtilClient.is_unset(request.mark):
            query['Mark'] = request.mark
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnose',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnose_with_options_async(
        self,
        request: ecs_20160314_models.CreateDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDiagnoseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.diagnose_action):
            query['DiagnoseAction'] = request.diagnose_action
        if not UtilClient.is_unset(request.diagnose_error_code):
            query['DiagnoseErrorCode'] = request.diagnose_error_code
        if not UtilClient.is_unset(request.diagnose_product):
            query['DiagnoseProduct'] = request.diagnose_product
        if not UtilClient.is_unset(request.diagnose_request_id):
            query['DiagnoseRequestId'] = request.diagnose_request_id
        if not UtilClient.is_unset(request.diagnose_request_params):
            query['DiagnoseRequestParams'] = request.diagnose_request_params
        if not UtilClient.is_unset(request.diagnose_response):
            query['DiagnoseResponse'] = request.diagnose_response
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type_name):
            query['InstanceTypeName'] = request.instance_type_name
        if not UtilClient.is_unset(request.iz_no):
            query['IzNo'] = request.iz_no
        if not UtilClient.is_unset(request.mark):
            query['Mark'] = request.mark
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnose',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDiagnoseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnose(
        self,
        request: ecs_20160314_models.CreateDiagnoseRequest,
    ) -> ecs_20160314_models.CreateDiagnoseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_diagnose_with_options(request, runtime)

    async def create_diagnose_async(
        self,
        request: ecs_20160314_models.CreateDiagnoseRequest,
    ) -> ecs_20160314_models.CreateDiagnoseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_diagnose_with_options_async(request, runtime)

    def create_diagnosis_operate_records_with_options(
        self,
        request: ecs_20160314_models.CreateDiagnosisOperateRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDiagnosisOperateRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.new_instance_type):
            query['NewInstanceType'] = request.new_instance_type
        if not UtilClient.is_unset(request.new_zone_id):
            query['NewZoneId'] = request.new_zone_id
        if not UtilClient.is_unset(request.operate_record_type):
            query['OperateRecordType'] = request.operate_record_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnosisOperateRecords',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDiagnosisOperateRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnosis_operate_records_with_options_async(
        self,
        request: ecs_20160314_models.CreateDiagnosisOperateRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDiagnosisOperateRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.new_instance_type):
            query['NewInstanceType'] = request.new_instance_type
        if not UtilClient.is_unset(request.new_zone_id):
            query['NewZoneId'] = request.new_zone_id
        if not UtilClient.is_unset(request.operate_record_type):
            query['OperateRecordType'] = request.operate_record_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnosisOperateRecords',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDiagnosisOperateRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnosis_operate_records(
        self,
        request: ecs_20160314_models.CreateDiagnosisOperateRecordsRequest,
    ) -> ecs_20160314_models.CreateDiagnosisOperateRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_diagnosis_operate_records_with_options(request, runtime)

    async def create_diagnosis_operate_records_async(
        self,
        request: ecs_20160314_models.CreateDiagnosisOperateRecordsRequest,
    ) -> ecs_20160314_models.CreateDiagnosisOperateRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_diagnosis_operate_records_with_options_async(request, runtime)

    def create_diagnostic_report_with_options(
        self,
        request: ecs_20160314_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.command_name):
            query['CommandName'] = request.command_name
        if not UtilClient.is_unset(request.command_type):
            query['CommandType'] = request.command_type
        if not UtilClient.is_unset(request.diagnostic_category):
            query['DiagnosticCategory'] = request.diagnostic_category
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plugin_version):
            query['PluginVersion'] = request.plugin_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_system):
            query['SourceSystem'] = request.source_system
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.source_system):
            query['sourceSystem'] = request.source_system
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDiagnosticReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnostic_report_with_options_async(
        self,
        request: ecs_20160314_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.command_name):
            query['CommandName'] = request.command_name
        if not UtilClient.is_unset(request.command_type):
            query['CommandType'] = request.command_type
        if not UtilClient.is_unset(request.diagnostic_category):
            query['DiagnosticCategory'] = request.diagnostic_category
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plugin_version):
            query['PluginVersion'] = request.plugin_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_system):
            query['SourceSystem'] = request.source_system
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.source_system):
            query['sourceSystem'] = request.source_system
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDiagnosticReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnostic_report(
        self,
        request: ecs_20160314_models.CreateDiagnosticReportRequest,
    ) -> ecs_20160314_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    async def create_diagnostic_report_async(
        self,
        request: ecs_20160314_models.CreateDiagnosticReportRequest,
    ) -> ecs_20160314_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_diagnostic_report_with_options_async(request, runtime)

    def create_disks_with_options(
        self,
        request: ecs_20160314_models.CreateDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.bursting_enabled):
            query['BurstingEnabled'] = request.bursting_enabled
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.encrypt_algorithm):
            query['EncryptAlgorithm'] = request.encrypt_algorithm
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.multi_attach):
            query['MultiAttach'] = request.multi_attach
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.storage_cluster_id):
            query['StorageClusterId'] = request.storage_cluster_id
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDisks',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_disks_with_options_async(
        self,
        request: ecs_20160314_models.CreateDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.bursting_enabled):
            query['BurstingEnabled'] = request.bursting_enabled
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.encrypt_algorithm):
            query['EncryptAlgorithm'] = request.encrypt_algorithm
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.multi_attach):
            query['MultiAttach'] = request.multi_attach
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.storage_cluster_id):
            query['StorageClusterId'] = request.storage_cluster_id
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDisks',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_disks(
        self,
        request: ecs_20160314_models.CreateDisksRequest,
    ) -> ecs_20160314_models.CreateDisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_disks_with_options(request, runtime)

    async def create_disks_async(
        self,
        request: ecs_20160314_models.CreateDisksRequest,
    ) -> ecs_20160314_models.CreateDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_disks_with_options_async(request, runtime)

    def create_elasticity_assurance_with_options(
        self,
        request: ecs_20160314_models.CreateElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assurance_times):
            query['AssuranceTimes'] = request.assurance_times
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_cpu_core_count):
            query['InstanceCpuCoreCount'] = request.instance_cpu_core_count
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticityAssurance',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateElasticityAssuranceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_elasticity_assurance_with_options_async(
        self,
        request: ecs_20160314_models.CreateElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assurance_times):
            query['AssuranceTimes'] = request.assurance_times
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_cpu_core_count):
            query['InstanceCpuCoreCount'] = request.instance_cpu_core_count
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticityAssurance',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateElasticityAssuranceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_elasticity_assurance(
        self,
        request: ecs_20160314_models.CreateElasticityAssuranceRequest,
    ) -> ecs_20160314_models.CreateElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_elasticity_assurance_with_options(request, runtime)

    async def create_elasticity_assurance_async(
        self,
        request: ecs_20160314_models.CreateElasticityAssuranceRequest,
    ) -> ecs_20160314_models.CreateElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_elasticity_assurance_with_options_async(request, runtime)

    def create_eni_qos_group_with_options(
        self,
        request: ecs_20160314_models.CreateEniQosGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateEniQosGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_group_name):
            query['QosGroupName'] = request.qos_group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rx):
            query['Rx'] = request.rx
        if not UtilClient.is_unset(request.rx_pps):
            query['RxPps'] = request.rx_pps
        if not UtilClient.is_unset(request.tx):
            query['Tx'] = request.tx
        if not UtilClient.is_unset(request.tx_pps):
            query['TxPps'] = request.tx_pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEniQosGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateEniQosGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_eni_qos_group_with_options_async(
        self,
        request: ecs_20160314_models.CreateEniQosGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateEniQosGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_group_name):
            query['QosGroupName'] = request.qos_group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rx):
            query['Rx'] = request.rx
        if not UtilClient.is_unset(request.rx_pps):
            query['RxPps'] = request.rx_pps
        if not UtilClient.is_unset(request.tx):
            query['Tx'] = request.tx
        if not UtilClient.is_unset(request.tx_pps):
            query['TxPps'] = request.tx_pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEniQosGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateEniQosGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_eni_qos_group(
        self,
        request: ecs_20160314_models.CreateEniQosGroupRequest,
    ) -> ecs_20160314_models.CreateEniQosGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_eni_qos_group_with_options(request, runtime)

    async def create_eni_qos_group_async(
        self,
        request: ecs_20160314_models.CreateEniQosGroupRequest,
    ) -> ecs_20160314_models.CreateEniQosGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_eni_qos_group_with_options_async(request, runtime)

    def create_function_feedback_with_options(
        self,
        request: ecs_20160314_models.CreateFunctionFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateFunctionFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFunctionFeedback',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateFunctionFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_function_feedback_with_options_async(
        self,
        request: ecs_20160314_models.CreateFunctionFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateFunctionFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFunctionFeedback',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateFunctionFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_function_feedback(
        self,
        request: ecs_20160314_models.CreateFunctionFeedbackRequest,
    ) -> ecs_20160314_models.CreateFunctionFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_function_feedback_with_options(request, runtime)

    async def create_function_feedback_async(
        self,
        request: ecs_20160314_models.CreateFunctionFeedbackRequest,
    ) -> ecs_20160314_models.CreateFunctionFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_function_feedback_with_options_async(request, runtime)

    def create_image_cache_with_options(
        self,
        request: ecs_20160314_models.CreateImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateImageCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageCache',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_cache_with_options_async(
        self,
        request: ecs_20160314_models.CreateImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateImageCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageCache',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateImageCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_cache(
        self,
        request: ecs_20160314_models.CreateImageCacheRequest,
    ) -> ecs_20160314_models.CreateImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_cache_with_options(request, runtime)

    async def create_image_cache_async(
        self,
        request: ecs_20160314_models.CreateImageCacheRequest,
    ) -> ecs_20160314_models.CreateImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_cache_with_options_async(request, runtime)

    def create_issue_category_report_relation_with_options(
        self,
        request: ecs_20160314_models.CreateIssueCategoryReportRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateIssueCategoryReportRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relation_model_list):
            query['RelationModelList'] = request.relation_model_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIssueCategoryReportRelation',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateIssueCategoryReportRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_issue_category_report_relation_with_options_async(
        self,
        request: ecs_20160314_models.CreateIssueCategoryReportRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateIssueCategoryReportRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relation_model_list):
            query['RelationModelList'] = request.relation_model_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIssueCategoryReportRelation',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateIssueCategoryReportRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_issue_category_report_relation(
        self,
        request: ecs_20160314_models.CreateIssueCategoryReportRelationRequest,
    ) -> ecs_20160314_models.CreateIssueCategoryReportRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_issue_category_report_relation_with_options(request, runtime)

    async def create_issue_category_report_relation_async(
        self,
        request: ecs_20160314_models.CreateIssueCategoryReportRelationRequest,
    ) -> ecs_20160314_models.CreateIssueCategoryReportRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_issue_category_report_relation_with_options_async(request, runtime)

    def create_migration_plan_with_options(
        self,
        request: ecs_20160314_models.CreateMigrationPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateMigrationPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_migration_times):
            query['CustomMigrationTimes'] = request.custom_migration_times
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.enable_auto_create_vswitch):
            query['EnableAutoCreateVSwitch'] = request.enable_auto_create_vswitch
        if not UtilClient.is_unset(request.ensure_network_connectivity):
            query['EnsureNetworkConnectivity'] = request.ensure_network_connectivity
        if not UtilClient.is_unset(request.global_migration_time):
            query['GlobalMigrationTime'] = request.global_migration_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remain_private_ip):
            query['RemainPrivateIp'] = request.remain_private_ip
        if not UtilClient.is_unset(request.remain_public_mac_as_priority):
            query['RemainPublicMacAsPriority'] = request.remain_public_mac_as_priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_security_group_ids):
            query['TargetSecurityGroupIds'] = request.target_security_group_ids
        if not UtilClient.is_unset(request.target_vswitch_id):
            query['TargetVSwitchId'] = request.target_vswitch_id
        if not UtilClient.is_unset(request.target_vpc_id):
            query['TargetVpcId'] = request.target_vpc_id
        if not UtilClient.is_unset(request.target_zone_id):
            query['TargetZoneId'] = request.target_zone_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrationPlan',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateMigrationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_migration_plan_with_options_async(
        self,
        request: ecs_20160314_models.CreateMigrationPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateMigrationPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_migration_times):
            query['CustomMigrationTimes'] = request.custom_migration_times
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.enable_auto_create_vswitch):
            query['EnableAutoCreateVSwitch'] = request.enable_auto_create_vswitch
        if not UtilClient.is_unset(request.ensure_network_connectivity):
            query['EnsureNetworkConnectivity'] = request.ensure_network_connectivity
        if not UtilClient.is_unset(request.global_migration_time):
            query['GlobalMigrationTime'] = request.global_migration_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remain_private_ip):
            query['RemainPrivateIp'] = request.remain_private_ip
        if not UtilClient.is_unset(request.remain_public_mac_as_priority):
            query['RemainPublicMacAsPriority'] = request.remain_public_mac_as_priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_security_group_ids):
            query['TargetSecurityGroupIds'] = request.target_security_group_ids
        if not UtilClient.is_unset(request.target_vswitch_id):
            query['TargetVSwitchId'] = request.target_vswitch_id
        if not UtilClient.is_unset(request.target_vpc_id):
            query['TargetVpcId'] = request.target_vpc_id
        if not UtilClient.is_unset(request.target_zone_id):
            query['TargetZoneId'] = request.target_zone_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrationPlan',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateMigrationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_migration_plan(
        self,
        request: ecs_20160314_models.CreateMigrationPlanRequest,
    ) -> ecs_20160314_models.CreateMigrationPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_migration_plan_with_options(request, runtime)

    async def create_migration_plan_async(
        self,
        request: ecs_20160314_models.CreateMigrationPlanRequest,
    ) -> ecs_20160314_models.CreateMigrationPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_migration_plan_with_options_async(request, runtime)

    def create_network_insights_path_with_options(
        self,
        request: ecs_20160314_models.CreateNetworkInsightsPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateNetworkInsightsPathResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.need_diagnose_guest):
            query['NeedDiagnoseGuest'] = request.need_diagnose_guest
        if not UtilClient.is_unset(request.network_insights_path_name):
            query['NetworkInsightsPathName'] = request.network_insights_path_name
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkInsightsPath',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateNetworkInsightsPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_insights_path_with_options_async(
        self,
        request: ecs_20160314_models.CreateNetworkInsightsPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateNetworkInsightsPathResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.need_diagnose_guest):
            query['NeedDiagnoseGuest'] = request.need_diagnose_guest
        if not UtilClient.is_unset(request.network_insights_path_name):
            query['NetworkInsightsPathName'] = request.network_insights_path_name
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkInsightsPath',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateNetworkInsightsPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_insights_path(
        self,
        request: ecs_20160314_models.CreateNetworkInsightsPathRequest,
    ) -> ecs_20160314_models.CreateNetworkInsightsPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_insights_path_with_options(request, runtime)

    async def create_network_insights_path_async(
        self,
        request: ecs_20160314_models.CreateNetworkInsightsPathRequest,
    ) -> ecs_20160314_models.CreateNetworkInsightsPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_insights_path_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        request: ecs_20160314_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.async_pattern):
            query['AsyncPattern'] = request.async_pattern
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
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
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: ecs_20160314_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.async_pattern):
            query['AsyncPattern'] = request.async_pattern
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
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
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order(
        self,
        request: ecs_20160314_models.CreateOrderRequest,
    ) -> ecs_20160314_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: ecs_20160314_models.CreateOrderRequest,
    ) -> ecs_20160314_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def create_reservation_demand_with_options(
        self,
        request: ecs_20160314_models.CreateReservationDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateReservationDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.confirm_type):
            query['ConfirmType'] = request.confirm_type
        if not UtilClient.is_unset(request.coupon_auto):
            query['CouponAuto'] = request.coupon_auto
        if not UtilClient.is_unset(request.coupon_type):
            query['CouponType'] = request.coupon_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_cpu_core_count):
            query['InstanceCpuCoreCount'] = request.instance_cpu_core_count
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.match_criteria):
            query['MatchCriteria'] = request.match_criteria
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_description):
            query['ReservedInstanceDescription'] = request.reserved_instance_description
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.reserved_instance_offering_type):
            query['ReservedInstanceOfferingType'] = request.reserved_instance_offering_type
        if not UtilClient.is_unset(request.reserved_instance_scope):
            query['ReservedInstanceScope'] = request.reserved_instance_scope
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_supply_type):
            query['ResourceSupplyType'] = request.resource_supply_type
        if not UtilClient.is_unset(request.saving_plan_description):
            query['SavingPlanDescription'] = request.saving_plan_description
        if not UtilClient.is_unset(request.saving_plan_hour_fee):
            query['SavingPlanHourFee'] = request.saving_plan_hour_fee
        if not UtilClient.is_unset(request.saving_plan_id):
            query['SavingPlanId'] = request.saving_plan_id
        if not UtilClient.is_unset(request.saving_plan_instance_type_family_group):
            query['SavingPlanInstanceTypeFamilyGroup'] = request.saving_plan_instance_type_family_group
        if not UtilClient.is_unset(request.saving_plan_name):
            query['SavingPlanName'] = request.saving_plan_name
        if not UtilClient.is_unset(request.saving_plan_pay_mode):
            query['SavingPlanPayMode'] = request.saving_plan_pay_mode
        if not UtilClient.is_unset(request.saving_plan_saving_type):
            query['SavingPlanSavingType'] = request.saving_plan_saving_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_ids):
            query['ZoneIds'] = request.zone_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReservationDemand',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateReservationDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_reservation_demand_with_options_async(
        self,
        request: ecs_20160314_models.CreateReservationDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateReservationDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.confirm_type):
            query['ConfirmType'] = request.confirm_type
        if not UtilClient.is_unset(request.coupon_auto):
            query['CouponAuto'] = request.coupon_auto
        if not UtilClient.is_unset(request.coupon_type):
            query['CouponType'] = request.coupon_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_cpu_core_count):
            query['InstanceCpuCoreCount'] = request.instance_cpu_core_count
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.match_criteria):
            query['MatchCriteria'] = request.match_criteria
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_description):
            query['ReservedInstanceDescription'] = request.reserved_instance_description
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.reserved_instance_offering_type):
            query['ReservedInstanceOfferingType'] = request.reserved_instance_offering_type
        if not UtilClient.is_unset(request.reserved_instance_scope):
            query['ReservedInstanceScope'] = request.reserved_instance_scope
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_supply_type):
            query['ResourceSupplyType'] = request.resource_supply_type
        if not UtilClient.is_unset(request.saving_plan_description):
            query['SavingPlanDescription'] = request.saving_plan_description
        if not UtilClient.is_unset(request.saving_plan_hour_fee):
            query['SavingPlanHourFee'] = request.saving_plan_hour_fee
        if not UtilClient.is_unset(request.saving_plan_id):
            query['SavingPlanId'] = request.saving_plan_id
        if not UtilClient.is_unset(request.saving_plan_instance_type_family_group):
            query['SavingPlanInstanceTypeFamilyGroup'] = request.saving_plan_instance_type_family_group
        if not UtilClient.is_unset(request.saving_plan_name):
            query['SavingPlanName'] = request.saving_plan_name
        if not UtilClient.is_unset(request.saving_plan_pay_mode):
            query['SavingPlanPayMode'] = request.saving_plan_pay_mode
        if not UtilClient.is_unset(request.saving_plan_saving_type):
            query['SavingPlanSavingType'] = request.saving_plan_saving_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_ids):
            query['ZoneIds'] = request.zone_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReservationDemand',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateReservationDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_reservation_demand(
        self,
        request: ecs_20160314_models.CreateReservationDemandRequest,
    ) -> ecs_20160314_models.CreateReservationDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_reservation_demand_with_options(request, runtime)

    async def create_reservation_demand_async(
        self,
        request: ecs_20160314_models.CreateReservationDemandRequest,
    ) -> ecs_20160314_models.CreateReservationDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_reservation_demand_with_options_async(request, runtime)

    def create_storage_set_with_options(
        self,
        request: ecs_20160314_models.CreateStorageSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateStorageSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.max_partition_number):
            query['MaxPartitionNumber'] = request.max_partition_number
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
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStorageSet',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateStorageSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_storage_set_with_options_async(
        self,
        request: ecs_20160314_models.CreateStorageSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateStorageSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.max_partition_number):
            query['MaxPartitionNumber'] = request.max_partition_number
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
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStorageSet',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateStorageSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_storage_set(
        self,
        request: ecs_20160314_models.CreateStorageSetRequest,
    ) -> ecs_20160314_models.CreateStorageSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_storage_set_with_options(request, runtime)

    async def create_storage_set_async(
        self,
        request: ecs_20160314_models.CreateStorageSetRequest,
    ) -> ecs_20160314_models.CreateStorageSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_storage_set_with_options_async(request, runtime)

    def create_user_quota_application_with_options(
        self,
        request: ecs_20160314_models.CreateUserQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateUserQuotaApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.quota_type):
            query['QuotaType'] = request.quota_type
        if not UtilClient.is_unset(request.quota_value):
            query['QuotaValue'] = request.quota_value
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserQuotaApplication',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateUserQuotaApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_quota_application_with_options_async(
        self,
        request: ecs_20160314_models.CreateUserQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateUserQuotaApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.quota_type):
            query['QuotaType'] = request.quota_type
        if not UtilClient.is_unset(request.quota_value):
            query['QuotaValue'] = request.quota_value
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserQuotaApplication',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateUserQuotaApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_quota_application(
        self,
        request: ecs_20160314_models.CreateUserQuotaApplicationRequest,
    ) -> ecs_20160314_models.CreateUserQuotaApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_quota_application_with_options(request, runtime)

    async def create_user_quota_application_async(
        self,
        request: ecs_20160314_models.CreateUserQuotaApplicationRequest,
    ) -> ecs_20160314_models.CreateUserQuotaApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_quota_application_with_options_async(request, runtime)

    def create_volumes_with_options(
        self,
        request: ecs_20160314_models.CreateVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateVolumesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
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
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.volume_category):
            query['VolumeCategory'] = request.volume_category
        if not UtilClient.is_unset(request.volume_encrypted):
            query['VolumeEncrypted'] = request.volume_encrypted
        if not UtilClient.is_unset(request.volume_name):
            query['VolumeName'] = request.volume_name
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVolumes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_volumes_with_options_async(
        self,
        request: ecs_20160314_models.CreateVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateVolumesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
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
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.volume_category):
            query['VolumeCategory'] = request.volume_category
        if not UtilClient.is_unset(request.volume_encrypted):
            query['VolumeEncrypted'] = request.volume_encrypted
        if not UtilClient.is_unset(request.volume_name):
            query['VolumeName'] = request.volume_name
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVolumes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_volumes(
        self,
        request: ecs_20160314_models.CreateVolumesRequest,
    ) -> ecs_20160314_models.CreateVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_volumes_with_options(request, runtime)

    async def create_volumes_async(
        self,
        request: ecs_20160314_models.CreateVolumesRequest,
    ) -> ecs_20160314_models.CreateVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_volumes_with_options_async(request, runtime)

    def create_waiting_order_with_options(
        self,
        request: ecs_20160314_models.CreateWaitingOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateWaitingOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.arn):
            query['Arn'] = request.arn
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_group_no):
            query['DeploymentSetGroupNo'] = request.deployment_set_group_no
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_names):
            query['HostNames'] = request.host_names
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not UtilClient.is_unset(request.http_put_response_hop_limit):
            query['HttpPutResponseHopLimit'] = request.http_put_response_hop_limit
        if not UtilClient.is_unset(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_name):
            query['LaunchTemplateName'] = request.launch_template_name
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.max_amount):
            query['MaxAmount'] = request.max_amount
        if not UtilClient.is_unset(request.min_amount):
            query['MinAmount'] = request.min_amount
        if not UtilClient.is_unset(request.network_interface):
            query['NetworkInterface'] = request.network_interface
        if not UtilClient.is_unset(request.network_interface_queue_number):
            query['NetworkInterfaceQueueNumber'] = request.network_interface_queue_number
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.unique_suffix):
            query['UniqueSuffix'] = request.unique_suffix
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.cpu_options):
            query['CpuOptions'] = request.cpu_options
        if not UtilClient.is_unset(request.hibernation_options):
            query['HibernationOptions'] = request.hibernation_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        if not UtilClient.is_unset(request.security_options):
            query['SecurityOptions'] = request.security_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWaitingOrder',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateWaitingOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_waiting_order_with_options_async(
        self,
        request: ecs_20160314_models.CreateWaitingOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.CreateWaitingOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.arn):
            query['Arn'] = request.arn
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_group_no):
            query['DeploymentSetGroupNo'] = request.deployment_set_group_no
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_names):
            query['HostNames'] = request.host_names
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not UtilClient.is_unset(request.http_put_response_hop_limit):
            query['HttpPutResponseHopLimit'] = request.http_put_response_hop_limit
        if not UtilClient.is_unset(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_name):
            query['LaunchTemplateName'] = request.launch_template_name
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.max_amount):
            query['MaxAmount'] = request.max_amount
        if not UtilClient.is_unset(request.min_amount):
            query['MinAmount'] = request.min_amount
        if not UtilClient.is_unset(request.network_interface):
            query['NetworkInterface'] = request.network_interface
        if not UtilClient.is_unset(request.network_interface_queue_number):
            query['NetworkInterfaceQueueNumber'] = request.network_interface_queue_number
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.unique_suffix):
            query['UniqueSuffix'] = request.unique_suffix
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.cpu_options):
            query['CpuOptions'] = request.cpu_options
        if not UtilClient.is_unset(request.hibernation_options):
            query['HibernationOptions'] = request.hibernation_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        if not UtilClient.is_unset(request.security_options):
            query['SecurityOptions'] = request.security_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWaitingOrder',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.CreateWaitingOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_waiting_order(
        self,
        request: ecs_20160314_models.CreateWaitingOrderRequest,
    ) -> ecs_20160314_models.CreateWaitingOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_waiting_order_with_options(request, runtime)

    async def create_waiting_order_async(
        self,
        request: ecs_20160314_models.CreateWaitingOrderRequest,
    ) -> ecs_20160314_models.CreateWaitingOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_waiting_order_with_options_async(request, runtime)

    def delete_dedicated_host_cluster_with_options(
        self,
        request: ecs_20160314_models.DeleteDedicatedHostClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteDedicatedHostClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
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
            action='DeleteDedicatedHostCluster',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteDedicatedHostClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dedicated_host_cluster_with_options_async(
        self,
        request: ecs_20160314_models.DeleteDedicatedHostClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteDedicatedHostClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
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
            action='DeleteDedicatedHostCluster',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteDedicatedHostClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dedicated_host_cluster(
        self,
        request: ecs_20160314_models.DeleteDedicatedHostClusterRequest,
    ) -> ecs_20160314_models.DeleteDedicatedHostClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_cluster_with_options(request, runtime)

    async def delete_dedicated_host_cluster_async(
        self,
        request: ecs_20160314_models.DeleteDedicatedHostClusterRequest,
    ) -> ecs_20160314_models.DeleteDedicatedHostClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_cluster_with_options_async(request, runtime)

    def delete_eni_qos_group_with_options(
        self,
        request: ecs_20160314_models.DeleteEniQosGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteEniQosGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_group_name):
            query['QosGroupName'] = request.qos_group_name
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
            action='DeleteEniQosGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteEniQosGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_eni_qos_group_with_options_async(
        self,
        request: ecs_20160314_models.DeleteEniQosGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteEniQosGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_group_name):
            query['QosGroupName'] = request.qos_group_name
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
            action='DeleteEniQosGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteEniQosGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_eni_qos_group(
        self,
        request: ecs_20160314_models.DeleteEniQosGroupRequest,
    ) -> ecs_20160314_models.DeleteEniQosGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_eni_qos_group_with_options(request, runtime)

    async def delete_eni_qos_group_async(
        self,
        request: ecs_20160314_models.DeleteEniQosGroupRequest,
    ) -> ecs_20160314_models.DeleteEniQosGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_eni_qos_group_with_options_async(request, runtime)

    def delete_image_cache_with_options(
        self,
        request: ecs_20160314_models.DeleteImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteImageCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageCache',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_cache_with_options_async(
        self,
        request: ecs_20160314_models.DeleteImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteImageCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageCache',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteImageCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image_cache(
        self,
        request: ecs_20160314_models.DeleteImageCacheRequest,
    ) -> ecs_20160314_models.DeleteImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_cache_with_options(request, runtime)

    async def delete_image_cache_async(
        self,
        request: ecs_20160314_models.DeleteImageCacheRequest,
    ) -> ecs_20160314_models.DeleteImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_cache_with_options_async(request, runtime)

    def delete_migratable_instances_with_options(
        self,
        request: ecs_20160314_models.DeleteMigratableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteMigratableInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DeleteMigratableInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteMigratableInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_migratable_instances_with_options_async(
        self,
        request: ecs_20160314_models.DeleteMigratableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteMigratableInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DeleteMigratableInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteMigratableInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_migratable_instances(
        self,
        request: ecs_20160314_models.DeleteMigratableInstancesRequest,
    ) -> ecs_20160314_models.DeleteMigratableInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_migratable_instances_with_options(request, runtime)

    async def delete_migratable_instances_async(
        self,
        request: ecs_20160314_models.DeleteMigratableInstancesRequest,
    ) -> ecs_20160314_models.DeleteMigratableInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_migratable_instances_with_options_async(request, runtime)

    def delete_network_insights_analysis_with_options(
        self,
        request: ecs_20160314_models.DeleteNetworkInsightsAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteNetworkInsightsAnalysisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.network_insights_analysis_id):
            query['NetworkInsightsAnalysisId'] = request.network_insights_analysis_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkInsightsAnalysis',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteNetworkInsightsAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_insights_analysis_with_options_async(
        self,
        request: ecs_20160314_models.DeleteNetworkInsightsAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteNetworkInsightsAnalysisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.network_insights_analysis_id):
            query['NetworkInsightsAnalysisId'] = request.network_insights_analysis_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkInsightsAnalysis',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteNetworkInsightsAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_insights_analysis(
        self,
        request: ecs_20160314_models.DeleteNetworkInsightsAnalysisRequest,
    ) -> ecs_20160314_models.DeleteNetworkInsightsAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_insights_analysis_with_options(request, runtime)

    async def delete_network_insights_analysis_async(
        self,
        request: ecs_20160314_models.DeleteNetworkInsightsAnalysisRequest,
    ) -> ecs_20160314_models.DeleteNetworkInsightsAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_insights_analysis_with_options_async(request, runtime)

    def delete_network_insights_path_with_options(
        self,
        request: ecs_20160314_models.DeleteNetworkInsightsPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteNetworkInsightsPathResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.network_insights_path_id):
            query['NetworkInsightsPathId'] = request.network_insights_path_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkInsightsPath',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteNetworkInsightsPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_insights_path_with_options_async(
        self,
        request: ecs_20160314_models.DeleteNetworkInsightsPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteNetworkInsightsPathResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.network_insights_path_id):
            query['NetworkInsightsPathId'] = request.network_insights_path_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkInsightsPath',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteNetworkInsightsPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_insights_path(
        self,
        request: ecs_20160314_models.DeleteNetworkInsightsPathRequest,
    ) -> ecs_20160314_models.DeleteNetworkInsightsPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_insights_path_with_options(request, runtime)

    async def delete_network_insights_path_async(
        self,
        request: ecs_20160314_models.DeleteNetworkInsightsPathRequest,
    ) -> ecs_20160314_models.DeleteNetworkInsightsPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_insights_path_with_options_async(request, runtime)

    def delete_reservation_demand_with_options(
        self,
        request: ecs_20160314_models.DeleteReservationDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteReservationDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReservationDemand',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteReservationDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_reservation_demand_with_options_async(
        self,
        request: ecs_20160314_models.DeleteReservationDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteReservationDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReservationDemand',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteReservationDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_reservation_demand(
        self,
        request: ecs_20160314_models.DeleteReservationDemandRequest,
    ) -> ecs_20160314_models.DeleteReservationDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_reservation_demand_with_options(request, runtime)

    async def delete_reservation_demand_async(
        self,
        request: ecs_20160314_models.DeleteReservationDemandRequest,
    ) -> ecs_20160314_models.DeleteReservationDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_reservation_demand_with_options_async(request, runtime)

    def delete_storage_set_with_options(
        self,
        request: ecs_20160314_models.DeleteStorageSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteStorageSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStorageSet',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteStorageSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_storage_set_with_options_async(
        self,
        request: ecs_20160314_models.DeleteStorageSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteStorageSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStorageSet',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteStorageSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_storage_set(
        self,
        request: ecs_20160314_models.DeleteStorageSetRequest,
    ) -> ecs_20160314_models.DeleteStorageSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_storage_set_with_options(request, runtime)

    async def delete_storage_set_async(
        self,
        request: ecs_20160314_models.DeleteStorageSetRequest,
    ) -> ecs_20160314_models.DeleteStorageSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_storage_set_with_options_async(request, runtime)

    def delete_user_quota_application_with_options(
        self,
        request: ecs_20160314_models.DeleteUserQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteUserQuotaApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='DeleteUserQuotaApplication',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteUserQuotaApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_quota_application_with_options_async(
        self,
        request: ecs_20160314_models.DeleteUserQuotaApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteUserQuotaApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='DeleteUserQuotaApplication',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteUserQuotaApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_quota_application(
        self,
        request: ecs_20160314_models.DeleteUserQuotaApplicationRequest,
    ) -> ecs_20160314_models.DeleteUserQuotaApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_quota_application_with_options(request, runtime)

    async def delete_user_quota_application_async(
        self,
        request: ecs_20160314_models.DeleteUserQuotaApplicationRequest,
    ) -> ecs_20160314_models.DeleteUserQuotaApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_quota_application_with_options_async(request, runtime)

    def delete_waiting_orders_with_options(
        self,
        request: ecs_20160314_models.DeleteWaitingOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteWaitingOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.waiting_order_id):
            query['WaitingOrderId'] = request.waiting_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaitingOrders',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteWaitingOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_waiting_orders_with_options_async(
        self,
        request: ecs_20160314_models.DeleteWaitingOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DeleteWaitingOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.waiting_order_id):
            query['WaitingOrderId'] = request.waiting_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaitingOrders',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DeleteWaitingOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_waiting_orders(
        self,
        request: ecs_20160314_models.DeleteWaitingOrdersRequest,
    ) -> ecs_20160314_models.DeleteWaitingOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_waiting_orders_with_options(request, runtime)

    async def delete_waiting_orders_async(
        self,
        request: ecs_20160314_models.DeleteWaitingOrdersRequest,
    ) -> ecs_20160314_models.DeleteWaitingOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_waiting_orders_with_options_async(request, runtime)

    def describe_account_attributes_with_options(
        self,
        request: ecs_20160314_models.DescribeAccountAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeAccountAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_name):
            query['AttributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeAccountAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_attributes_with_options_async(
        self,
        request: ecs_20160314_models.DescribeAccountAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeAccountAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_name):
            query['AttributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeAccountAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_attributes(
        self,
        request: ecs_20160314_models.DescribeAccountAttributesRequest,
    ) -> ecs_20160314_models.DescribeAccountAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_attributes_with_options(request, runtime)

    async def describe_account_attributes_async(
        self,
        request: ecs_20160314_models.DescribeAccountAttributesRequest,
    ) -> ecs_20160314_models.DescribeAccountAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_attributes_with_options_async(request, runtime)

    def describe_account_limits_with_options(
        self,
        request: ecs_20160314_models.DescribeAccountLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeAccountLimitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
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
            action='DescribeAccountLimits',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeAccountLimitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_limits_with_options_async(
        self,
        request: ecs_20160314_models.DescribeAccountLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeAccountLimitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
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
            action='DescribeAccountLimits',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeAccountLimitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_limits(
        self,
        request: ecs_20160314_models.DescribeAccountLimitsRequest,
    ) -> ecs_20160314_models.DescribeAccountLimitsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_limits_with_options(request, runtime)

    async def describe_account_limits_async(
        self,
        request: ecs_20160314_models.DescribeAccountLimitsRequest,
    ) -> ecs_20160314_models.DescribeAccountLimitsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_limits_with_options_async(request, runtime)

    def describe_account_quota_attributes_with_options(
        self,
        request: ecs_20160314_models.DescribeAccountQuotaAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeAccountQuotaAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeAccountQuotaAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeAccountQuotaAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_quota_attributes_with_options_async(
        self,
        request: ecs_20160314_models.DescribeAccountQuotaAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeAccountQuotaAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeAccountQuotaAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeAccountQuotaAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_quota_attributes(
        self,
        request: ecs_20160314_models.DescribeAccountQuotaAttributesRequest,
    ) -> ecs_20160314_models.DescribeAccountQuotaAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_quota_attributes_with_options(request, runtime)

    async def describe_account_quota_attributes_async(
        self,
        request: ecs_20160314_models.DescribeAccountQuotaAttributesRequest,
    ) -> ecs_20160314_models.DescribeAccountQuotaAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_quota_attributes_with_options_async(request, runtime)

    def describe_auto_provisioning_group_capacities_with_options(
        self,
        request: ecs_20160314_models.DescribeAutoProvisioningGroupCapacitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeAutoProvisioningGroupCapacitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_provisioning_group_id):
            query['AutoProvisioningGroupId'] = request.auto_provisioning_group_id
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
            action='DescribeAutoProvisioningGroupCapacities',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeAutoProvisioningGroupCapacitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_provisioning_group_capacities_with_options_async(
        self,
        request: ecs_20160314_models.DescribeAutoProvisioningGroupCapacitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeAutoProvisioningGroupCapacitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_provisioning_group_id):
            query['AutoProvisioningGroupId'] = request.auto_provisioning_group_id
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
            action='DescribeAutoProvisioningGroupCapacities',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeAutoProvisioningGroupCapacitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_provisioning_group_capacities(
        self,
        request: ecs_20160314_models.DescribeAutoProvisioningGroupCapacitiesRequest,
    ) -> ecs_20160314_models.DescribeAutoProvisioningGroupCapacitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_provisioning_group_capacities_with_options(request, runtime)

    async def describe_auto_provisioning_group_capacities_async(
        self,
        request: ecs_20160314_models.DescribeAutoProvisioningGroupCapacitiesRequest,
    ) -> ecs_20160314_models.DescribeAutoProvisioningGroupCapacitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_provisioning_group_capacities_with_options_async(request, runtime)

    def describe_bandwidth_price_with_options(
        self,
        request: ecs_20160314_models.DescribeBandwidthPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeBandwidthPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.price_unit):
            query['PriceUnit'] = request.price_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBandwidthPrice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeBandwidthPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bandwidth_price_with_options_async(
        self,
        request: ecs_20160314_models.DescribeBandwidthPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeBandwidthPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.price_unit):
            query['PriceUnit'] = request.price_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBandwidthPrice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeBandwidthPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bandwidth_price(
        self,
        request: ecs_20160314_models.DescribeBandwidthPriceRequest,
    ) -> ecs_20160314_models.DescribeBandwidthPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_price_with_options(request, runtime)

    async def describe_bandwidth_price_async(
        self,
        request: ecs_20160314_models.DescribeBandwidthPriceRequest,
    ) -> ecs_20160314_models.DescribeBandwidthPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bandwidth_price_with_options_async(request, runtime)

    def describe_capacity_reservations_with_options(
        self,
        request: ecs_20160314_models.DescribeCapacityReservationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeCapacityReservationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity_reservation_ids):
            query['CapacityReservationIds'] = request.capacity_reservation_ids
        if not UtilClient.is_unset(request.capacity_reservation_name):
            query['CapacityReservationName'] = request.capacity_reservation_name
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCapacityReservations',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeCapacityReservationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_capacity_reservations_with_options_async(
        self,
        request: ecs_20160314_models.DescribeCapacityReservationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeCapacityReservationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity_reservation_ids):
            query['CapacityReservationIds'] = request.capacity_reservation_ids
        if not UtilClient.is_unset(request.capacity_reservation_name):
            query['CapacityReservationName'] = request.capacity_reservation_name
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCapacityReservations',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeCapacityReservationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_capacity_reservations(
        self,
        request: ecs_20160314_models.DescribeCapacityReservationsRequest,
    ) -> ecs_20160314_models.DescribeCapacityReservationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_capacity_reservations_with_options(request, runtime)

    async def describe_capacity_reservations_async(
        self,
        request: ecs_20160314_models.DescribeCapacityReservationsRequest,
    ) -> ecs_20160314_models.DescribeCapacityReservationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_capacity_reservations_with_options_async(request, runtime)

    def describe_customer_issue_category_with_options(
        self,
        request: ecs_20160314_models.DescribeCustomerIssueCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeCustomerIssueCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomerIssueCategory',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeCustomerIssueCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_customer_issue_category_with_options_async(
        self,
        request: ecs_20160314_models.DescribeCustomerIssueCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeCustomerIssueCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomerIssueCategory',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeCustomerIssueCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_customer_issue_category(
        self,
        request: ecs_20160314_models.DescribeCustomerIssueCategoryRequest,
    ) -> ecs_20160314_models.DescribeCustomerIssueCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_customer_issue_category_with_options(request, runtime)

    async def describe_customer_issue_category_async(
        self,
        request: ecs_20160314_models.DescribeCustomerIssueCategoryRequest,
    ) -> ecs_20160314_models.DescribeCustomerIssueCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_customer_issue_category_with_options_async(request, runtime)

    def describe_dedicated_host_auto_renew_with_options(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostAutoRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDedicatedHostAutoRenewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostAutoRenew',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDedicatedHostAutoRenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_host_auto_renew_with_options_async(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostAutoRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDedicatedHostAutoRenewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostAutoRenew',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDedicatedHostAutoRenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_host_auto_renew(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostAutoRenewRequest,
    ) -> ecs_20160314_models.DescribeDedicatedHostAutoRenewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_auto_renew_with_options(request, runtime)

    async def describe_dedicated_host_auto_renew_async(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostAutoRenewRequest,
    ) -> ecs_20160314_models.DescribeDedicatedHostAutoRenewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_auto_renew_with_options_async(request, runtime)

    def describe_dedicated_host_clusters_with_options(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDedicatedHostClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_ids):
            query['DedicatedHostClusterIds'] = request.dedicated_host_cluster_ids
        if not UtilClient.is_unset(request.dedicated_host_cluster_name):
            query['DedicatedHostClusterName'] = request.dedicated_host_cluster_name
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostClusters',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDedicatedHostClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_host_clusters_with_options_async(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDedicatedHostClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_ids):
            query['DedicatedHostClusterIds'] = request.dedicated_host_cluster_ids
        if not UtilClient.is_unset(request.dedicated_host_cluster_name):
            query['DedicatedHostClusterName'] = request.dedicated_host_cluster_name
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostClusters',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDedicatedHostClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_host_clusters(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostClustersRequest,
    ) -> ecs_20160314_models.DescribeDedicatedHostClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_clusters_with_options(request, runtime)

    async def describe_dedicated_host_clusters_async(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostClustersRequest,
    ) -> ecs_20160314_models.DescribeDedicatedHostClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_clusters_with_options_async(request, runtime)

    def describe_dedicated_host_types_with_options(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDedicatedHostTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_type):
            query['DedicatedHostType'] = request.dedicated_host_type
        if not UtilClient.is_unset(request.generation):
            query['Generation'] = request.generation
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
        if not UtilClient.is_unset(request.support_instance_type_family):
            query['SupportInstanceTypeFamily'] = request.support_instance_type_family
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostTypes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDedicatedHostTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_host_types_with_options_async(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDedicatedHostTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_type):
            query['DedicatedHostType'] = request.dedicated_host_type
        if not UtilClient.is_unset(request.generation):
            query['Generation'] = request.generation
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
        if not UtilClient.is_unset(request.support_instance_type_family):
            query['SupportInstanceTypeFamily'] = request.support_instance_type_family
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostTypes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDedicatedHostTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_host_types(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostTypesRequest,
    ) -> ecs_20160314_models.DescribeDedicatedHostTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_types_with_options(request, runtime)

    async def describe_dedicated_host_types_async(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostTypesRequest,
    ) -> ecs_20160314_models.DescribeDedicatedHostTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_types_with_options_async(request, runtime)

    def describe_dedicated_hosts_with_options(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_ids):
            query['DedicatedHostIds'] = request.dedicated_host_ids
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.dedicated_host_type):
            query['DedicatedHostType'] = request.dedicated_host_type
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHosts',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDedicatedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_hosts_with_options_async(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_ids):
            query['DedicatedHostIds'] = request.dedicated_host_ids
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.dedicated_host_type):
            query['DedicatedHostType'] = request.dedicated_host_type
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHosts',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDedicatedHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_hosts(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostsRequest,
    ) -> ecs_20160314_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    async def describe_dedicated_hosts_async(
        self,
        request: ecs_20160314_models.DescribeDedicatedHostsRequest,
    ) -> ecs_20160314_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_hosts_with_options_async(request, runtime)

    def describe_diagnose_with_options(
        self,
        request: ecs_20160314_models.DescribeDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDiagnoseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnose_action):
            query['DiagnoseAction'] = request.diagnose_action
        if not UtilClient.is_unset(request.diagnose_id):
            query['DiagnoseId'] = request.diagnose_id
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnose',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnose_with_options_async(
        self,
        request: ecs_20160314_models.DescribeDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDiagnoseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnose_action):
            query['DiagnoseAction'] = request.diagnose_action
        if not UtilClient.is_unset(request.diagnose_id):
            query['DiagnoseId'] = request.diagnose_id
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnose',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDiagnoseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnose(
        self,
        request: ecs_20160314_models.DescribeDiagnoseRequest,
    ) -> ecs_20160314_models.DescribeDiagnoseResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnose_with_options(request, runtime)

    async def describe_diagnose_async(
        self,
        request: ecs_20160314_models.DescribeDiagnoseRequest,
    ) -> ecs_20160314_models.DescribeDiagnoseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnose_with_options_async(request, runtime)

    def describe_diagnosis_operate_records_with_options(
        self,
        request: ecs_20160314_models.DescribeDiagnosisOperateRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDiagnosisOperateRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.operate_record_type):
            query['OperateRecordType'] = request.operate_record_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisOperateRecords',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDiagnosisOperateRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_operate_records_with_options_async(
        self,
        request: ecs_20160314_models.DescribeDiagnosisOperateRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDiagnosisOperateRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.operate_record_type):
            query['OperateRecordType'] = request.operate_record_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisOperateRecords',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDiagnosisOperateRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_operate_records(
        self,
        request: ecs_20160314_models.DescribeDiagnosisOperateRecordsRequest,
    ) -> ecs_20160314_models.DescribeDiagnosisOperateRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_operate_records_with_options(request, runtime)

    async def describe_diagnosis_operate_records_async(
        self,
        request: ecs_20160314_models.DescribeDiagnosisOperateRecordsRequest,
    ) -> ecs_20160314_models.DescribeDiagnosisOperateRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_operate_records_with_options_async(request, runtime)

    def describe_diagnostic_reports_with_options(
        self,
        request: ecs_20160314_models.DescribeDiagnosticReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDiagnosticReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.source_system):
            query['SourceSystem'] = request.source_system
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReports',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDiagnosticReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnostic_reports_with_options_async(
        self,
        request: ecs_20160314_models.DescribeDiagnosticReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDiagnosticReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.source_system):
            query['SourceSystem'] = request.source_system
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReports',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDiagnosticReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnostic_reports(
        self,
        request: ecs_20160314_models.DescribeDiagnosticReportsRequest,
    ) -> ecs_20160314_models.DescribeDiagnosticReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_reports_with_options(request, runtime)

    async def describe_diagnostic_reports_async(
        self,
        request: ecs_20160314_models.DescribeDiagnosticReportsRequest,
    ) -> ecs_20160314_models.DescribeDiagnosticReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnostic_reports_with_options_async(request, runtime)

    def describe_disk_replica_pairs_with_options(
        self,
        request: ecs_20160314_models.DescribeDiskReplicaPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDiskReplicaPairsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='DescribeDiskReplicaPairs',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDiskReplicaPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_replica_pairs_with_options_async(
        self,
        request: ecs_20160314_models.DescribeDiskReplicaPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeDiskReplicaPairsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='DescribeDiskReplicaPairs',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeDiskReplicaPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_replica_pairs(
        self,
        request: ecs_20160314_models.DescribeDiskReplicaPairsRequest,
    ) -> ecs_20160314_models.DescribeDiskReplicaPairsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_replica_pairs_with_options(request, runtime)

    async def describe_disk_replica_pairs_async(
        self,
        request: ecs_20160314_models.DescribeDiskReplicaPairsRequest,
    ) -> ecs_20160314_models.DescribeDiskReplicaPairsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_replica_pairs_with_options_async(request, runtime)

    def describe_ecs_scenario_facade_with_options(
        self,
        request: ecs_20160314_models.DescribeEcsScenarioFacadeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeEcsScenarioFacadeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ext_map):
            query['ExtMap'] = request.ext_map
        if not UtilClient.is_unset(request.ext_param):
            query['ExtParam'] = request.ext_param
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scenario_list):
            query['ScenarioList'] = request.scenario_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEcsScenarioFacade',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeEcsScenarioFacadeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ecs_scenario_facade_with_options_async(
        self,
        request: ecs_20160314_models.DescribeEcsScenarioFacadeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeEcsScenarioFacadeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ext_map):
            query['ExtMap'] = request.ext_map
        if not UtilClient.is_unset(request.ext_param):
            query['ExtParam'] = request.ext_param
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scenario_list):
            query['ScenarioList'] = request.scenario_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEcsScenarioFacade',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeEcsScenarioFacadeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ecs_scenario_facade(
        self,
        request: ecs_20160314_models.DescribeEcsScenarioFacadeRequest,
    ) -> ecs_20160314_models.DescribeEcsScenarioFacadeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ecs_scenario_facade_with_options(request, runtime)

    async def describe_ecs_scenario_facade_async(
        self,
        request: ecs_20160314_models.DescribeEcsScenarioFacadeRequest,
    ) -> ecs_20160314_models.DescribeEcsScenarioFacadeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ecs_scenario_facade_with_options_async(request, runtime)

    def describe_eni_qos_group_info_with_options(
        self,
        request: ecs_20160314_models.DescribeEniQosGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeEniQosGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_group_name):
            query['QosGroupName'] = request.qos_group_name
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
            action='DescribeEniQosGroupInfo',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeEniQosGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eni_qos_group_info_with_options_async(
        self,
        request: ecs_20160314_models.DescribeEniQosGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeEniQosGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_group_name):
            query['QosGroupName'] = request.qos_group_name
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
            action='DescribeEniQosGroupInfo',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeEniQosGroupInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eni_qos_group_info(
        self,
        request: ecs_20160314_models.DescribeEniQosGroupInfoRequest,
    ) -> ecs_20160314_models.DescribeEniQosGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eni_qos_group_info_with_options(request, runtime)

    async def describe_eni_qos_group_info_async(
        self,
        request: ecs_20160314_models.DescribeEniQosGroupInfoRequest,
    ) -> ecs_20160314_models.DescribeEniQosGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eni_qos_group_info_with_options_async(request, runtime)

    def describe_function_feedback_with_options(
        self,
        request: ecs_20160314_models.DescribeFunctionFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeFunctionFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
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
            action='DescribeFunctionFeedback',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeFunctionFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_function_feedback_with_options_async(
        self,
        request: ecs_20160314_models.DescribeFunctionFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeFunctionFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
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
            action='DescribeFunctionFeedback',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeFunctionFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_function_feedback(
        self,
        request: ecs_20160314_models.DescribeFunctionFeedbackRequest,
    ) -> ecs_20160314_models.DescribeFunctionFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_function_feedback_with_options(request, runtime)

    async def describe_function_feedback_async(
        self,
        request: ecs_20160314_models.DescribeFunctionFeedbackRequest,
    ) -> ecs_20160314_models.DescribeFunctionFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_function_feedback_with_options_async(request, runtime)

    def describe_havs_instance_types_with_options(
        self,
        request: ecs_20160314_models.DescribeHavsInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeHavsInstanceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeHavsInstanceTypes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeHavsInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_havs_instance_types_with_options_async(
        self,
        request: ecs_20160314_models.DescribeHavsInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeHavsInstanceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeHavsInstanceTypes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeHavsInstanceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_havs_instance_types(
        self,
        request: ecs_20160314_models.DescribeHavsInstanceTypesRequest,
    ) -> ecs_20160314_models.DescribeHavsInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_havs_instance_types_with_options(request, runtime)

    async def describe_havs_instance_types_async(
        self,
        request: ecs_20160314_models.DescribeHavsInstanceTypesRequest,
    ) -> ecs_20160314_models.DescribeHavsInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_havs_instance_types_with_options_async(request, runtime)

    def describe_image_agreement_with_options(
        self,
        request: ecs_20160314_models.DescribeImageAgreementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeImageAgreementResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_type):
            query['AgreementType'] = request.agreement_type
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
            action='DescribeImageAgreement',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeImageAgreementResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_agreement_with_options_async(
        self,
        request: ecs_20160314_models.DescribeImageAgreementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeImageAgreementResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agreement_type):
            query['AgreementType'] = request.agreement_type
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
            action='DescribeImageAgreement',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeImageAgreementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_agreement(
        self,
        request: ecs_20160314_models.DescribeImageAgreementRequest,
    ) -> ecs_20160314_models.DescribeImageAgreementResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_agreement_with_options(request, runtime)

    async def describe_image_agreement_async(
        self,
        request: ecs_20160314_models.DescribeImageAgreementRequest,
    ) -> ecs_20160314_models.DescribeImageAgreementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_agreement_with_options_async(request, runtime)

    def describe_image_caches_with_options(
        self,
        request: ecs_20160314_models.DescribeImageCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeImageCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageCaches',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeImageCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_caches_with_options_async(
        self,
        request: ecs_20160314_models.DescribeImageCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeImageCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageCaches',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeImageCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_caches(
        self,
        request: ecs_20160314_models.DescribeImageCachesRequest,
    ) -> ecs_20160314_models.DescribeImageCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_caches_with_options(request, runtime)

    async def describe_image_caches_async(
        self,
        request: ecs_20160314_models.DescribeImageCachesRequest,
    ) -> ecs_20160314_models.DescribeImageCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_caches_with_options_async(request, runtime)

    def describe_image_families_with_options(
        self,
        request: ecs_20160314_models.DescribeImageFamiliesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeImageFamiliesResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageFamilies',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeImageFamiliesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_families_with_options_async(
        self,
        request: ecs_20160314_models.DescribeImageFamiliesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeImageFamiliesResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageFamilies',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeImageFamiliesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_families(
        self,
        request: ecs_20160314_models.DescribeImageFamiliesRequest,
    ) -> ecs_20160314_models.DescribeImageFamiliesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_families_with_options(request, runtime)

    async def describe_image_families_async(
        self,
        request: ecs_20160314_models.DescribeImageFamiliesRequest,
    ) -> ecs_20160314_models.DescribeImageFamiliesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_families_with_options_async(request, runtime)

    def describe_instance_auto_reboot_time_with_options(
        self,
        request: ecs_20160314_models.DescribeInstanceAutoRebootTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceAutoRebootTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_reboot_time_from):
            query['AutoRebootTimeFrom'] = request.auto_reboot_time_from
        if not UtilClient.is_unset(request.auto_reboot_time_to):
            query['AutoRebootTimeTo'] = request.auto_reboot_time_to
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
            action='DescribeInstanceAutoRebootTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceAutoRebootTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_auto_reboot_time_with_options_async(
        self,
        request: ecs_20160314_models.DescribeInstanceAutoRebootTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceAutoRebootTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_reboot_time_from):
            query['AutoRebootTimeFrom'] = request.auto_reboot_time_from
        if not UtilClient.is_unset(request.auto_reboot_time_to):
            query['AutoRebootTimeTo'] = request.auto_reboot_time_to
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
            action='DescribeInstanceAutoRebootTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceAutoRebootTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_auto_reboot_time(
        self,
        request: ecs_20160314_models.DescribeInstanceAutoRebootTimeRequest,
    ) -> ecs_20160314_models.DescribeInstanceAutoRebootTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_reboot_time_with_options(request, runtime)

    async def describe_instance_auto_reboot_time_async(
        self,
        request: ecs_20160314_models.DescribeInstanceAutoRebootTimeRequest,
    ) -> ecs_20160314_models.DescribeInstanceAutoRebootTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_reboot_time_with_options_async(request, runtime)

    def describe_instance_health_status_with_options(
        self,
        request: ecs_20160314_models.DescribeInstanceHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceHealthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceHealthStatus',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_health_status_with_options_async(
        self,
        request: ecs_20160314_models.DescribeInstanceHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceHealthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceHealthStatus',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_health_status(
        self,
        request: ecs_20160314_models.DescribeInstanceHealthStatusRequest,
    ) -> ecs_20160314_models.DescribeInstanceHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_health_status_with_options(request, runtime)

    async def describe_instance_health_status_async(
        self,
        request: ecs_20160314_models.DescribeInstanceHealthStatusRequest,
    ) -> ecs_20160314_models.DescribeInstanceHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_health_status_with_options_async(request, runtime)

    def describe_instance_maintenance_attributes_with_options(
        self,
        request: ecs_20160314_models.DescribeInstanceMaintenanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceMaintenanceAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeInstanceMaintenanceAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceMaintenanceAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_maintenance_attributes_with_options_async(
        self,
        request: ecs_20160314_models.DescribeInstanceMaintenanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceMaintenanceAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeInstanceMaintenanceAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceMaintenanceAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_maintenance_attributes(
        self,
        request: ecs_20160314_models.DescribeInstanceMaintenanceAttributesRequest,
    ) -> ecs_20160314_models.DescribeInstanceMaintenanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_maintenance_attributes_with_options(request, runtime)

    async def describe_instance_maintenance_attributes_async(
        self,
        request: ecs_20160314_models.DescribeInstanceMaintenanceAttributesRequest,
    ) -> ecs_20160314_models.DescribeInstanceMaintenanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_maintenance_attributes_with_options_async(request, runtime)

    def describe_instance_modification_price_with_options(
        self,
        request: ecs_20160314_models.DescribeInstanceModificationPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceModificationPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceModificationPrice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceModificationPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_modification_price_with_options_async(
        self,
        request: ecs_20160314_models.DescribeInstanceModificationPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceModificationPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceModificationPrice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceModificationPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_modification_price(
        self,
        request: ecs_20160314_models.DescribeInstanceModificationPriceRequest,
    ) -> ecs_20160314_models.DescribeInstanceModificationPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_modification_price_with_options(request, runtime)

    async def describe_instance_modification_price_async(
        self,
        request: ecs_20160314_models.DescribeInstanceModificationPriceRequest,
    ) -> ecs_20160314_models.DescribeInstanceModificationPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_modification_price_with_options_async(request, runtime)

    def describe_instance_need_reboot_with_options(
        self,
        request: ecs_20160314_models.DescribeInstanceNeedRebootRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceNeedRebootResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
            action='DescribeInstanceNeedReboot',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceNeedRebootResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_need_reboot_with_options_async(
        self,
        request: ecs_20160314_models.DescribeInstanceNeedRebootRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceNeedRebootResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
            action='DescribeInstanceNeedReboot',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceNeedRebootResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_need_reboot(
        self,
        request: ecs_20160314_models.DescribeInstanceNeedRebootRequest,
    ) -> ecs_20160314_models.DescribeInstanceNeedRebootResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_need_reboot_with_options(request, runtime)

    async def describe_instance_need_reboot_async(
        self,
        request: ecs_20160314_models.DescribeInstanceNeedRebootRequest,
    ) -> ecs_20160314_models.DescribeInstanceNeedRebootResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_need_reboot_with_options_async(request, runtime)

    def describe_instance_performance_restrict_history_with_options(
        self,
        request: ecs_20160314_models.DescribeInstancePerformanceRestrictHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstancePerformanceRestrictHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeInstancePerformanceRestrictHistory',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstancePerformanceRestrictHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_performance_restrict_history_with_options_async(
        self,
        request: ecs_20160314_models.DescribeInstancePerformanceRestrictHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstancePerformanceRestrictHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeInstancePerformanceRestrictHistory',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstancePerformanceRestrictHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_performance_restrict_history(
        self,
        request: ecs_20160314_models.DescribeInstancePerformanceRestrictHistoryRequest,
    ) -> ecs_20160314_models.DescribeInstancePerformanceRestrictHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_performance_restrict_history_with_options(request, runtime)

    async def describe_instance_performance_restrict_history_async(
        self,
        request: ecs_20160314_models.DescribeInstancePerformanceRestrictHistoryRequest,
    ) -> ecs_20160314_models.DescribeInstancePerformanceRestrictHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_performance_restrict_history_with_options_async(request, runtime)

    def describe_instance_type_resource_with_options(
        self,
        request: ecs_20160314_models.DescribeInstanceTypeResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceTypeResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.instance_type_families):
            query['InstanceTypeFamilies'] = request.instance_type_families
        if not UtilClient.is_unset(request.instance_type_match_mode):
            query['InstanceTypeMatchMode'] = request.instance_type_match_mode
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.memories):
            query['Memories'] = request.memories
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
        if not UtilClient.is_unset(request.search_types):
            query['SearchTypes'] = request.search_types
        if not UtilClient.is_unset(request.zone_ids):
            query['ZoneIds'] = request.zone_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTypeResource',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceTypeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_type_resource_with_options_async(
        self,
        request: ecs_20160314_models.DescribeInstanceTypeResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeInstanceTypeResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.instance_type_families):
            query['InstanceTypeFamilies'] = request.instance_type_families
        if not UtilClient.is_unset(request.instance_type_match_mode):
            query['InstanceTypeMatchMode'] = request.instance_type_match_mode
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.memories):
            query['Memories'] = request.memories
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
        if not UtilClient.is_unset(request.search_types):
            query['SearchTypes'] = request.search_types
        if not UtilClient.is_unset(request.zone_ids):
            query['ZoneIds'] = request.zone_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTypeResource',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeInstanceTypeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_type_resource(
        self,
        request: ecs_20160314_models.DescribeInstanceTypeResourceRequest,
    ) -> ecs_20160314_models.DescribeInstanceTypeResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_type_resource_with_options(request, runtime)

    async def describe_instance_type_resource_async(
        self,
        request: ecs_20160314_models.DescribeInstanceTypeResourceRequest,
    ) -> ecs_20160314_models.DescribeInstanceTypeResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_type_resource_with_options_async(request, runtime)

    def describe_kmskey_attribute_with_options(
        self,
        request: ecs_20160314_models.DescribeKMSKeyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeKMSKeyAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
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
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKMSKeyAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeKMSKeyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kmskey_attribute_with_options_async(
        self,
        request: ecs_20160314_models.DescribeKMSKeyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeKMSKeyAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
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
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKMSKeyAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeKMSKeyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kmskey_attribute(
        self,
        request: ecs_20160314_models.DescribeKMSKeyAttributeRequest,
    ) -> ecs_20160314_models.DescribeKMSKeyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_kmskey_attribute_with_options(request, runtime)

    async def describe_kmskey_attribute_async(
        self,
        request: ecs_20160314_models.DescribeKMSKeyAttributeRequest,
    ) -> ecs_20160314_models.DescribeKMSKeyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_kmskey_attribute_with_options_async(request, runtime)

    def describe_kmskeys_with_options(
        self,
        request: ecs_20160314_models.DescribeKMSKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeKMSKeysResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKMSKeys',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeKMSKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kmskeys_with_options_async(
        self,
        request: ecs_20160314_models.DescribeKMSKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeKMSKeysResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKMSKeys',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeKMSKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kmskeys(
        self,
        request: ecs_20160314_models.DescribeKMSKeysRequest,
    ) -> ecs_20160314_models.DescribeKMSKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_kmskeys_with_options(request, runtime)

    async def describe_kmskeys_async(
        self,
        request: ecs_20160314_models.DescribeKMSKeysRequest,
    ) -> ecs_20160314_models.DescribeKMSKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_kmskeys_with_options_async(request, runtime)

    def describe_linked_kmskeys_with_options(
        self,
        request: ecs_20160314_models.DescribeLinkedKMSKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeLinkedKMSKeysResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLinkedKMSKeys',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeLinkedKMSKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_linked_kmskeys_with_options_async(
        self,
        request: ecs_20160314_models.DescribeLinkedKMSKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeLinkedKMSKeysResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.operator):
            query['operator'] = request.operator
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLinkedKMSKeys',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeLinkedKMSKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_linked_kmskeys(
        self,
        request: ecs_20160314_models.DescribeLinkedKMSKeysRequest,
    ) -> ecs_20160314_models.DescribeLinkedKMSKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_linked_kmskeys_with_options(request, runtime)

    async def describe_linked_kmskeys_async(
        self,
        request: ecs_20160314_models.DescribeLinkedKMSKeysRequest,
    ) -> ecs_20160314_models.DescribeLinkedKMSKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_linked_kmskeys_with_options_async(request, runtime)

    def describe_local_disk_repair_activities_with_options(
        self,
        request: ecs_20160314_models.DescribeLocalDiskRepairActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeLocalDiskRepairActivitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.include_history):
            query['IncludeHistory'] = request.include_history
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeLocalDiskRepairActivities',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeLocalDiskRepairActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_local_disk_repair_activities_with_options_async(
        self,
        request: ecs_20160314_models.DescribeLocalDiskRepairActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeLocalDiskRepairActivitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.include_history):
            query['IncludeHistory'] = request.include_history
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeLocalDiskRepairActivities',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeLocalDiskRepairActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_local_disk_repair_activities(
        self,
        request: ecs_20160314_models.DescribeLocalDiskRepairActivitiesRequest,
    ) -> ecs_20160314_models.DescribeLocalDiskRepairActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_local_disk_repair_activities_with_options(request, runtime)

    async def describe_local_disk_repair_activities_async(
        self,
        request: ecs_20160314_models.DescribeLocalDiskRepairActivitiesRequest,
    ) -> ecs_20160314_models.DescribeLocalDiskRepairActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_local_disk_repair_activities_with_options_async(request, runtime)

    def describe_migration_instances_with_options(
        self,
        request: ecs_20160314_models.DescribeMigrationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeMigrationInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_migration_type):
            query['BusinessMigrationType'] = request.business_migration_type
        if not UtilClient.is_unset(request.hostname):
            query['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.migration_plan_id):
            query['MigrationPlanId'] = request.migration_plan_id
        if not UtilClient.is_unset(request.migration_status):
            query['MigrationStatus'] = request.migration_status
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeMigrationInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_instances_with_options_async(
        self,
        request: ecs_20160314_models.DescribeMigrationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeMigrationInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_migration_type):
            query['BusinessMigrationType'] = request.business_migration_type
        if not UtilClient.is_unset(request.hostname):
            query['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.migration_plan_id):
            query['MigrationPlanId'] = request.migration_plan_id
        if not UtilClient.is_unset(request.migration_status):
            query['MigrationStatus'] = request.migration_status
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeMigrationInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_instances(
        self,
        request: ecs_20160314_models.DescribeMigrationInstancesRequest,
    ) -> ecs_20160314_models.DescribeMigrationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_instances_with_options(request, runtime)

    async def describe_migration_instances_async(
        self,
        request: ecs_20160314_models.DescribeMigrationInstancesRequest,
    ) -> ecs_20160314_models.DescribeMigrationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_instances_with_options_async(request, runtime)

    def describe_migration_plans_with_options(
        self,
        request: ecs_20160314_models.DescribeMigrationPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeMigrationPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_plan_id):
            query['MigrationPlanId'] = request.migration_plan_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationPlans',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeMigrationPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_plans_with_options_async(
        self,
        request: ecs_20160314_models.DescribeMigrationPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeMigrationPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_plan_id):
            query['MigrationPlanId'] = request.migration_plan_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationPlans',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeMigrationPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_plans(
        self,
        request: ecs_20160314_models.DescribeMigrationPlansRequest,
    ) -> ecs_20160314_models.DescribeMigrationPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_plans_with_options(request, runtime)

    async def describe_migration_plans_async(
        self,
        request: ecs_20160314_models.DescribeMigrationPlansRequest,
    ) -> ecs_20160314_models.DescribeMigrationPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_plans_with_options_async(request, runtime)

    def describe_migration_preferences_with_options(
        self,
        request: ecs_20160314_models.DescribeMigrationPreferencesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeMigrationPreferencesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_network_type):
            query['MigrationNetworkType'] = request.migration_network_type
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
            action='DescribeMigrationPreferences',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeMigrationPreferencesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_preferences_with_options_async(
        self,
        request: ecs_20160314_models.DescribeMigrationPreferencesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeMigrationPreferencesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_network_type):
            query['MigrationNetworkType'] = request.migration_network_type
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
            action='DescribeMigrationPreferences',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeMigrationPreferencesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_preferences(
        self,
        request: ecs_20160314_models.DescribeMigrationPreferencesRequest,
    ) -> ecs_20160314_models.DescribeMigrationPreferencesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_preferences_with_options(request, runtime)

    async def describe_migration_preferences_async(
        self,
        request: ecs_20160314_models.DescribeMigrationPreferencesRequest,
    ) -> ecs_20160314_models.DescribeMigrationPreferencesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_preferences_with_options_async(request, runtime)

    def describe_network_insights_analysis_result_with_options(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsAnalysisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeNetworkInsightsAnalysisResultResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkInsightsAnalysisResult',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeNetworkInsightsAnalysisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_insights_analysis_result_with_options_async(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsAnalysisResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeNetworkInsightsAnalysisResultResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkInsightsAnalysisResult',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeNetworkInsightsAnalysisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_insights_analysis_result(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsAnalysisResultRequest,
    ) -> ecs_20160314_models.DescribeNetworkInsightsAnalysisResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_insights_analysis_result_with_options(request, runtime)

    async def describe_network_insights_analysis_result_async(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsAnalysisResultRequest,
    ) -> ecs_20160314_models.DescribeNetworkInsightsAnalysisResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_insights_analysis_result_with_options_async(request, runtime)

    def describe_network_insights_analysises_with_options(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsAnalysisesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeNetworkInsightsAnalysisesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkInsightsAnalysises',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeNetworkInsightsAnalysisesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_insights_analysises_with_options_async(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsAnalysisesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeNetworkInsightsAnalysisesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkInsightsAnalysises',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeNetworkInsightsAnalysisesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_insights_analysises(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsAnalysisesRequest,
    ) -> ecs_20160314_models.DescribeNetworkInsightsAnalysisesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_insights_analysises_with_options(request, runtime)

    async def describe_network_insights_analysises_async(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsAnalysisesRequest,
    ) -> ecs_20160314_models.DescribeNetworkInsightsAnalysisesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_insights_analysises_with_options_async(request, runtime)

    def describe_network_insights_paths_with_options(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeNetworkInsightsPathsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_insights_path_id):
            query['NetworkInsightsPathId'] = request.network_insights_path_id
        if not UtilClient.is_unset(request.network_path_found):
            query['NetworkPathFound'] = request.network_path_found
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkInsightsPaths',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeNetworkInsightsPathsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_insights_paths_with_options_async(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeNetworkInsightsPathsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_insights_path_id):
            query['NetworkInsightsPathId'] = request.network_insights_path_id
        if not UtilClient.is_unset(request.network_path_found):
            query['NetworkPathFound'] = request.network_path_found
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkInsightsPaths',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeNetworkInsightsPathsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_insights_paths(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsPathsRequest,
    ) -> ecs_20160314_models.DescribeNetworkInsightsPathsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_insights_paths_with_options(request, runtime)

    async def describe_network_insights_paths_async(
        self,
        request: ecs_20160314_models.DescribeNetworkInsightsPathsRequest,
    ) -> ecs_20160314_models.DescribeNetworkInsightsPathsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_insights_paths_with_options_async(request, runtime)

    def describe_order_auto_reboot_time_with_options(
        self,
        request: ecs_20160314_models.DescribeOrderAutoRebootTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeOrderAutoRebootTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
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
            action='DescribeOrderAutoRebootTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeOrderAutoRebootTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_order_auto_reboot_time_with_options_async(
        self,
        request: ecs_20160314_models.DescribeOrderAutoRebootTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeOrderAutoRebootTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
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
            action='DescribeOrderAutoRebootTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeOrderAutoRebootTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_order_auto_reboot_time(
        self,
        request: ecs_20160314_models.DescribeOrderAutoRebootTimeRequest,
    ) -> ecs_20160314_models.DescribeOrderAutoRebootTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_order_auto_reboot_time_with_options(request, runtime)

    async def describe_order_auto_reboot_time_async(
        self,
        request: ecs_20160314_models.DescribeOrderAutoRebootTimeRequest,
    ) -> ecs_20160314_models.DescribeOrderAutoRebootTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_order_auto_reboot_time_with_options_async(request, runtime)

    def describe_pre_paid_resource_refund_price_with_options(
        self,
        request: ecs_20160314_models.DescribePrePaidResourceRefundPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribePrePaidResourceRefundPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrePaidResourceRefundPrice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribePrePaidResourceRefundPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pre_paid_resource_refund_price_with_options_async(
        self,
        request: ecs_20160314_models.DescribePrePaidResourceRefundPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribePrePaidResourceRefundPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrePaidResourceRefundPrice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribePrePaidResourceRefundPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pre_paid_resource_refund_price(
        self,
        request: ecs_20160314_models.DescribePrePaidResourceRefundPriceRequest,
    ) -> ecs_20160314_models.DescribePrePaidResourceRefundPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_paid_resource_refund_price_with_options(request, runtime)

    async def describe_pre_paid_resource_refund_price_async(
        self,
        request: ecs_20160314_models.DescribePrePaidResourceRefundPriceRequest,
    ) -> ecs_20160314_models.DescribePrePaidResourceRefundPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pre_paid_resource_refund_price_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: ecs_20160314_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.default_vpc):
            query['DefaultVpc'] = request.default_vpc
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.need_spot_price):
            query['NeedSpotPrice'] = request.need_spot_price
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
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
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: ecs_20160314_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.default_vpc):
            query['DefaultVpc'] = request.default_vpc
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.need_spot_price):
            query['NeedSpotPrice'] = request.need_spot_price
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
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
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: ecs_20160314_models.DescribePriceRequest,
    ) -> ecs_20160314_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: ecs_20160314_models.DescribePriceRequest,
    ) -> ecs_20160314_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_private_pools_with_options(
        self,
        request: ecs_20160314_models.DescribePrivatePoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribePrivatePoolsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time_type):
            query['StartTimeType'] = request.start_time_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrivatePools',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribePrivatePoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_private_pools_with_options_async(
        self,
        request: ecs_20160314_models.DescribePrivatePoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribePrivatePoolsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time_type):
            query['StartTimeType'] = request.start_time_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrivatePools',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribePrivatePoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_private_pools(
        self,
        request: ecs_20160314_models.DescribePrivatePoolsRequest,
    ) -> ecs_20160314_models.DescribePrivatePoolsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_private_pools_with_options(request, runtime)

    async def describe_private_pools_async(
        self,
        request: ecs_20160314_models.DescribePrivatePoolsRequest,
    ) -> ecs_20160314_models.DescribePrivatePoolsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_private_pools_with_options_async(request, runtime)

    def describe_recommend_product_with_options(
        self,
        request: ecs_20160314_models.DescribeRecommendProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeRecommendProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.instance_type_support_ipv_6):
            query['InstanceTypeSupportIPv6'] = request.instance_type_support_ipv_6
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.max_price):
            query['MaxPrice'] = request.max_price
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority_strategy):
            query['PriorityStrategy'] = request.priority_strategy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk_category):
            query['SystemDiskCategory'] = request.system_disk_category
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_match_mode):
            query['ZoneMatchMode'] = request.zone_match_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecommendProduct',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeRecommendProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recommend_product_with_options_async(
        self,
        request: ecs_20160314_models.DescribeRecommendProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeRecommendProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.instance_type_support_ipv_6):
            query['InstanceTypeSupportIPv6'] = request.instance_type_support_ipv_6
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.max_price):
            query['MaxPrice'] = request.max_price
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority_strategy):
            query['PriorityStrategy'] = request.priority_strategy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk_category):
            query['SystemDiskCategory'] = request.system_disk_category
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_match_mode):
            query['ZoneMatchMode'] = request.zone_match_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecommendProduct',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeRecommendProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recommend_product(
        self,
        request: ecs_20160314_models.DescribeRecommendProductRequest,
    ) -> ecs_20160314_models.DescribeRecommendProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_product_with_options(request, runtime)

    async def describe_recommend_product_async(
        self,
        request: ecs_20160314_models.DescribeRecommendProductRequest,
    ) -> ecs_20160314_models.DescribeRecommendProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_recommend_product_with_options_async(request, runtime)

    def describe_reservation_demand_committed_amount_with_options(
        self,
        request: ecs_20160314_models.DescribeReservationDemandCommittedAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservationDemandCommittedAmountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demand_plan):
            query['DemandPlan'] = request.demand_plan
        if not UtilClient.is_unset(request.instance_family):
            query['InstanceFamily'] = request.instance_family
        if not UtilClient.is_unset(request.instance_family_set):
            query['InstanceFamilySet'] = request.instance_family_set
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.plan_type):
            query['PlanType'] = request.plan_type
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.purchase_method):
            query['PurchaseMethod'] = request.purchase_method
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReservationDemandCommittedAmount',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservationDemandCommittedAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reservation_demand_committed_amount_with_options_async(
        self,
        request: ecs_20160314_models.DescribeReservationDemandCommittedAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservationDemandCommittedAmountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demand_plan):
            query['DemandPlan'] = request.demand_plan
        if not UtilClient.is_unset(request.instance_family):
            query['InstanceFamily'] = request.instance_family
        if not UtilClient.is_unset(request.instance_family_set):
            query['InstanceFamilySet'] = request.instance_family_set
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.plan_type):
            query['PlanType'] = request.plan_type
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.purchase_method):
            query['PurchaseMethod'] = request.purchase_method
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReservationDemandCommittedAmount',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservationDemandCommittedAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reservation_demand_committed_amount(
        self,
        request: ecs_20160314_models.DescribeReservationDemandCommittedAmountRequest,
    ) -> ecs_20160314_models.DescribeReservationDemandCommittedAmountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reservation_demand_committed_amount_with_options(request, runtime)

    async def describe_reservation_demand_committed_amount_async(
        self,
        request: ecs_20160314_models.DescribeReservationDemandCommittedAmountRequest,
    ) -> ecs_20160314_models.DescribeReservationDemandCommittedAmountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reservation_demand_committed_amount_with_options_async(request, runtime)

    def describe_reservation_demands_with_options(
        self,
        request: ecs_20160314_models.DescribeReservationDemandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservationDemandsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReservationDemands',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservationDemandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reservation_demands_with_options_async(
        self,
        request: ecs_20160314_models.DescribeReservationDemandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservationDemandsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReservationDemands',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservationDemandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reservation_demands(
        self,
        request: ecs_20160314_models.DescribeReservationDemandsRequest,
    ) -> ecs_20160314_models.DescribeReservationDemandsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reservation_demands_with_options(request, runtime)

    async def describe_reservation_demands_async(
        self,
        request: ecs_20160314_models.DescribeReservationDemandsRequest,
    ) -> ecs_20160314_models.DescribeReservationDemandsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reservation_demands_with_options_async(request, runtime)

    def describe_reserved_instance_allocations_with_options(
        self,
        request: ecs_20160314_models.DescribeReservedInstanceAllocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservedInstanceAllocationsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
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
            action='DescribeReservedInstanceAllocations',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservedInstanceAllocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reserved_instance_allocations_with_options_async(
        self,
        request: ecs_20160314_models.DescribeReservedInstanceAllocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservedInstanceAllocationsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
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
            action='DescribeReservedInstanceAllocations',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservedInstanceAllocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reserved_instance_allocations(
        self,
        request: ecs_20160314_models.DescribeReservedInstanceAllocationsRequest,
    ) -> ecs_20160314_models.DescribeReservedInstanceAllocationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reserved_instance_allocations_with_options(request, runtime)

    async def describe_reserved_instance_allocations_async(
        self,
        request: ecs_20160314_models.DescribeReservedInstanceAllocationsRequest,
    ) -> ecs_20160314_models.DescribeReservedInstanceAllocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reserved_instance_allocations_with_options_async(request, runtime)

    def describe_reserved_instance_categories_with_options(
        self,
        request: ecs_20160314_models.DescribeReservedInstanceCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservedInstanceCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReservedInstanceCategories',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservedInstanceCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reserved_instance_categories_with_options_async(
        self,
        request: ecs_20160314_models.DescribeReservedInstanceCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservedInstanceCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReservedInstanceCategories',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservedInstanceCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reserved_instance_categories(
        self,
        request: ecs_20160314_models.DescribeReservedInstanceCategoriesRequest,
    ) -> ecs_20160314_models.DescribeReservedInstanceCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reserved_instance_categories_with_options(request, runtime)

    async def describe_reserved_instance_categories_async(
        self,
        request: ecs_20160314_models.DescribeReservedInstanceCategoriesRequest,
    ) -> ecs_20160314_models.DescribeReservedInstanceCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reserved_instance_categories_with_options_async(request, runtime)

    def describe_reserved_instance_price_with_options(
        self,
        request: ecs_20160314_models.DescribeReservedInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservedInstancePriceResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
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
            action='DescribeReservedInstancePrice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservedInstancePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reserved_instance_price_with_options_async(
        self,
        request: ecs_20160314_models.DescribeReservedInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservedInstancePriceResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
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
            action='DescribeReservedInstancePrice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservedInstancePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reserved_instance_price(
        self,
        request: ecs_20160314_models.DescribeReservedInstancePriceRequest,
    ) -> ecs_20160314_models.DescribeReservedInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reserved_instance_price_with_options(request, runtime)

    async def describe_reserved_instance_price_async(
        self,
        request: ecs_20160314_models.DescribeReservedInstancePriceRequest,
    ) -> ecs_20160314_models.DescribeReservedInstancePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reserved_instance_price_with_options_async(request, runtime)

    def describe_reserved_instances_with_options(
        self,
        request: ecs_20160314_models.DescribeReservedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservedInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_type):
            query['AllocationType'] = request.allocation_type
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReservedInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservedInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reserved_instances_with_options_async(
        self,
        request: ecs_20160314_models.DescribeReservedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeReservedInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_type):
            query['AllocationType'] = request.allocation_type
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReservedInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeReservedInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reserved_instances(
        self,
        request: ecs_20160314_models.DescribeReservedInstancesRequest,
    ) -> ecs_20160314_models.DescribeReservedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reserved_instances_with_options(request, runtime)

    async def describe_reserved_instances_async(
        self,
        request: ecs_20160314_models.DescribeReservedInstancesRequest,
    ) -> ecs_20160314_models.DescribeReservedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reserved_instances_with_options_async(request, runtime)

    def describe_resource_aggregations_with_options(
        self,
        request: ecs_20160314_models.DescribeResourceAggregationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceAggregationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregators):
            query['Aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceAggregations',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceAggregationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_aggregations_with_options_async(
        self,
        request: ecs_20160314_models.DescribeResourceAggregationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceAggregationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregators):
            query['Aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceAggregations',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceAggregationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_aggregations(
        self,
        request: ecs_20160314_models.DescribeResourceAggregationsRequest,
    ) -> ecs_20160314_models.DescribeResourceAggregationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_aggregations_with_options(request, runtime)

    async def describe_resource_aggregations_async(
        self,
        request: ecs_20160314_models.DescribeResourceAggregationsRequest,
    ) -> ecs_20160314_models.DescribeResourceAggregationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_aggregations_with_options_async(request, runtime)

    def describe_resource_allocation_with_options(
        self,
        request: ecs_20160314_models.DescribeResourceAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceAllocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.data_disk_category):
            query['DataDiskCategory'] = request.data_disk_category
        if not UtilClient.is_unset(request.default_target_capacity_type):
            query['DefaultTargetCapacityType'] = request.default_target_capacity_type
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_type_model):
            query['InstanceTypeModel'] = request.instance_type_model
        if not UtilClient.is_unset(request.instance_type_support_ipv_6):
            query['InstanceTypeSupportIPv6'] = request.instance_type_support_ipv_6
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.max_price):
            query['MaxPrice'] = request.max_price
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.post_paid_base_capacity):
            query['PostPaidBaseCapacity'] = request.post_paid_base_capacity
        if not UtilClient.is_unset(request.priority_strategy):
            query['PriorityStrategy'] = request.priority_strategy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_amount_type):
            query['ResourceAmountType'] = request.resource_amount_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_base_capacity):
            query['SpotBaseCapacity'] = request.spot_base_capacity
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.strict_satisfied_target_capacity):
            query['StrictSatisfiedTargetCapacity'] = request.strict_satisfied_target_capacity
        if not UtilClient.is_unset(request.system_disk_category):
            query['SystemDiskCategory'] = request.system_disk_category
        if not UtilClient.is_unset(request.target_capacity):
            query['TargetCapacity'] = request.target_capacity
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceAllocation',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_allocation_with_options_async(
        self,
        request: ecs_20160314_models.DescribeResourceAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceAllocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.data_disk_category):
            query['DataDiskCategory'] = request.data_disk_category
        if not UtilClient.is_unset(request.default_target_capacity_type):
            query['DefaultTargetCapacityType'] = request.default_target_capacity_type
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_type_model):
            query['InstanceTypeModel'] = request.instance_type_model
        if not UtilClient.is_unset(request.instance_type_support_ipv_6):
            query['InstanceTypeSupportIPv6'] = request.instance_type_support_ipv_6
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.max_price):
            query['MaxPrice'] = request.max_price
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.post_paid_base_capacity):
            query['PostPaidBaseCapacity'] = request.post_paid_base_capacity
        if not UtilClient.is_unset(request.priority_strategy):
            query['PriorityStrategy'] = request.priority_strategy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_amount_type):
            query['ResourceAmountType'] = request.resource_amount_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_base_capacity):
            query['SpotBaseCapacity'] = request.spot_base_capacity
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.strict_satisfied_target_capacity):
            query['StrictSatisfiedTargetCapacity'] = request.strict_satisfied_target_capacity
        if not UtilClient.is_unset(request.system_disk_category):
            query['SystemDiskCategory'] = request.system_disk_category
        if not UtilClient.is_unset(request.target_capacity):
            query['TargetCapacity'] = request.target_capacity
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceAllocation',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_allocation(
        self,
        request: ecs_20160314_models.DescribeResourceAllocationRequest,
    ) -> ecs_20160314_models.DescribeResourceAllocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_allocation_with_options(request, runtime)

    async def describe_resource_allocation_async(
        self,
        request: ecs_20160314_models.DescribeResourceAllocationRequest,
    ) -> ecs_20160314_models.DescribeResourceAllocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_allocation_with_options_async(request, runtime)

    def describe_resource_display_with_options(
        self,
        request: ecs_20160314_models.DescribeResourceDisplayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceDisplayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.first_biz_level):
            query['FirstBizLevel'] = request.first_biz_level
        if not UtilClient.is_unset(request.instance_category_type):
            query['InstanceCategoryType'] = request.instance_category_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.second_biz_level):
            query['SecondBizLevel'] = request.second_biz_level
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceDisplay',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceDisplayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_display_with_options_async(
        self,
        request: ecs_20160314_models.DescribeResourceDisplayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceDisplayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.first_biz_level):
            query['FirstBizLevel'] = request.first_biz_level
        if not UtilClient.is_unset(request.instance_category_type):
            query['InstanceCategoryType'] = request.instance_category_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.second_biz_level):
            query['SecondBizLevel'] = request.second_biz_level
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceDisplay',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceDisplayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_display(
        self,
        request: ecs_20160314_models.DescribeResourceDisplayRequest,
    ) -> ecs_20160314_models.DescribeResourceDisplayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_display_with_options(request, runtime)

    async def describe_resource_display_async(
        self,
        request: ecs_20160314_models.DescribeResourceDisplayRequest,
    ) -> ecs_20160314_models.DescribeResourceDisplayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_display_with_options_async(request, runtime)

    def describe_resource_filter_attributes_with_options(
        self,
        request: ecs_20160314_models.DescribeResourceFilterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceFilterAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceFilterAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceFilterAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_filter_attributes_with_options_async(
        self,
        request: ecs_20160314_models.DescribeResourceFilterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceFilterAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceFilterAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceFilterAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_filter_attributes(
        self,
        request: ecs_20160314_models.DescribeResourceFilterAttributesRequest,
    ) -> ecs_20160314_models.DescribeResourceFilterAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_filter_attributes_with_options(request, runtime)

    async def describe_resource_filter_attributes_async(
        self,
        request: ecs_20160314_models.DescribeResourceFilterAttributesRequest,
    ) -> ecs_20160314_models.DescribeResourceFilterAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_filter_attributes_with_options_async(request, runtime)

    def describe_resource_recommend_filters_with_options(
        self,
        request: ecs_20160314_models.DescribeResourceRecommendFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceRecommendFiltersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_name):
            query['AttributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.attribute_value):
            query['AttributeValue'] = request.attribute_value
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceRecommendFilters',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceRecommendFiltersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_recommend_filters_with_options_async(
        self,
        request: ecs_20160314_models.DescribeResourceRecommendFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceRecommendFiltersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_name):
            query['AttributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.attribute_value):
            query['AttributeValue'] = request.attribute_value
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceRecommendFilters',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceRecommendFiltersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_recommend_filters(
        self,
        request: ecs_20160314_models.DescribeResourceRecommendFiltersRequest,
    ) -> ecs_20160314_models.DescribeResourceRecommendFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_recommend_filters_with_options(request, runtime)

    async def describe_resource_recommend_filters_async(
        self,
        request: ecs_20160314_models.DescribeResourceRecommendFiltersRequest,
    ) -> ecs_20160314_models.DescribeResourceRecommendFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_recommend_filters_with_options_async(request, runtime)

    def describe_resource_solutions_with_options(
        self,
        request: ecs_20160314_models.DescribeResourceSolutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceSolutionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_type_model):
            query['InstanceTypeModel'] = request.instance_type_model
        if not UtilClient.is_unset(request.instance_type_support_ipv_6):
            query['InstanceTypeSupportIPv6'] = request.instance_type_support_ipv_6
        if not UtilClient.is_unset(request.match_open_instances):
            query['MatchOpenInstances'] = request.match_open_instances
        if not UtilClient.is_unset(request.max_price):
            query['MaxPrice'] = request.max_price
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_amount_type):
            query['ResourceAmountType'] = request.resource_amount_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk_category):
            query['SystemDiskCategory'] = request.system_disk_category
        if not UtilClient.is_unset(request.target_capacity):
            query['TargetCapacity'] = request.target_capacity
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceSolutions',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceSolutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_solutions_with_options_async(
        self,
        request: ecs_20160314_models.DescribeResourceSolutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourceSolutionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_type_model):
            query['InstanceTypeModel'] = request.instance_type_model
        if not UtilClient.is_unset(request.instance_type_support_ipv_6):
            query['InstanceTypeSupportIPv6'] = request.instance_type_support_ipv_6
        if not UtilClient.is_unset(request.match_open_instances):
            query['MatchOpenInstances'] = request.match_open_instances
        if not UtilClient.is_unset(request.max_price):
            query['MaxPrice'] = request.max_price
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_amount_type):
            query['ResourceAmountType'] = request.resource_amount_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk_category):
            query['SystemDiskCategory'] = request.system_disk_category
        if not UtilClient.is_unset(request.target_capacity):
            query['TargetCapacity'] = request.target_capacity
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceSolutions',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourceSolutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_solutions(
        self,
        request: ecs_20160314_models.DescribeResourceSolutionsRequest,
    ) -> ecs_20160314_models.DescribeResourceSolutionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_solutions_with_options(request, runtime)

    async def describe_resource_solutions_async(
        self,
        request: ecs_20160314_models.DescribeResourceSolutionsRequest,
    ) -> ecs_20160314_models.DescribeResourceSolutionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_solutions_with_options_async(request, runtime)

    def describe_resources_with_options(
        self,
        request: ecs_20160314_models.DescribeResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResources',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resources_with_options_async(
        self,
        request: ecs_20160314_models.DescribeResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.global_):
            query['Global'] = request.global_
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResources',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resources(
        self,
        request: ecs_20160314_models.DescribeResourcesRequest,
    ) -> ecs_20160314_models.DescribeResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resources_with_options(request, runtime)

    async def describe_resources_async(
        self,
        request: ecs_20160314_models.DescribeResourcesRequest,
    ) -> ecs_20160314_models.DescribeResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resources_with_options_async(request, runtime)

    def describe_ri_utilization_with_options(
        self,
        request: ecs_20160314_models.DescribeRiUtilizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeRiUtilizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
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
            action='DescribeRiUtilization',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeRiUtilizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ri_utilization_with_options_async(
        self,
        request: ecs_20160314_models.DescribeRiUtilizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeRiUtilizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
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
            action='DescribeRiUtilization',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeRiUtilizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ri_utilization(
        self,
        request: ecs_20160314_models.DescribeRiUtilizationRequest,
    ) -> ecs_20160314_models.DescribeRiUtilizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ri_utilization_with_options(request, runtime)

    async def describe_ri_utilization_async(
        self,
        request: ecs_20160314_models.DescribeRiUtilizationRequest,
    ) -> ecs_20160314_models.DescribeRiUtilizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ri_utilization_with_options_async(request, runtime)

    def describe_scene_purchase_recommend_with_options(
        self,
        request: ecs_20160314_models.DescribeScenePurchaseRecommendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeScenePurchaseRecommendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScenePurchaseRecommend',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeScenePurchaseRecommendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_purchase_recommend_with_options_async(
        self,
        request: ecs_20160314_models.DescribeScenePurchaseRecommendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeScenePurchaseRecommendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScenePurchaseRecommend',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeScenePurchaseRecommendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_purchase_recommend(
        self,
        request: ecs_20160314_models.DescribeScenePurchaseRecommendRequest,
    ) -> ecs_20160314_models.DescribeScenePurchaseRecommendResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_purchase_recommend_with_options(request, runtime)

    async def describe_scene_purchase_recommend_async(
        self,
        request: ecs_20160314_models.DescribeScenePurchaseRecommendRequest,
    ) -> ecs_20160314_models.DescribeScenePurchaseRecommendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_purchase_recommend_with_options_async(request, runtime)

    def describe_scene_resource_recommend_with_options(
        self,
        request: ecs_20160314_models.DescribeSceneResourceRecommendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeSceneResourceRecommendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneResourceRecommend',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeSceneResourceRecommendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scene_resource_recommend_with_options_async(
        self,
        request: ecs_20160314_models.DescribeSceneResourceRecommendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeSceneResourceRecommendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneResourceRecommend',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeSceneResourceRecommendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scene_resource_recommend(
        self,
        request: ecs_20160314_models.DescribeSceneResourceRecommendRequest,
    ) -> ecs_20160314_models.DescribeSceneResourceRecommendResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_resource_recommend_with_options(request, runtime)

    async def describe_scene_resource_recommend_async(
        self,
        request: ecs_20160314_models.DescribeSceneResourceRecommendRequest,
    ) -> ecs_20160314_models.DescribeSceneResourceRecommendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scene_resource_recommend_with_options_async(request, runtime)

    def describe_spot_instance_advice_with_options(
        self,
        request: ecs_20160314_models.DescribeSpotInstanceAdviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeSpotInstanceAdviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.min_cores):
            query['MinCores'] = request.min_cores
        if not UtilClient.is_unset(request.min_memory):
            query['MinMemory'] = request.min_memory
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpotInstanceAdvice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeSpotInstanceAdviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spot_instance_advice_with_options_async(
        self,
        request: ecs_20160314_models.DescribeSpotInstanceAdviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeSpotInstanceAdviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.min_cores):
            query['MinCores'] = request.min_cores
        if not UtilClient.is_unset(request.min_memory):
            query['MinMemory'] = request.min_memory
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpotInstanceAdvice',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeSpotInstanceAdviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spot_instance_advice(
        self,
        request: ecs_20160314_models.DescribeSpotInstanceAdviceRequest,
    ) -> ecs_20160314_models.DescribeSpotInstanceAdviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_spot_instance_advice_with_options(request, runtime)

    async def describe_spot_instance_advice_async(
        self,
        request: ecs_20160314_models.DescribeSpotInstanceAdviceRequest,
    ) -> ecs_20160314_models.DescribeSpotInstanceAdviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_spot_instance_advice_with_options_async(request, runtime)

    def describe_storage_capacity_unit_allocations_with_options(
        self,
        request: ecs_20160314_models.DescribeStorageCapacityUnitAllocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeStorageCapacityUnitAllocationsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.storage_capacity_unit_id):
            query['StorageCapacityUnitId'] = request.storage_capacity_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageCapacityUnitAllocations',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeStorageCapacityUnitAllocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_capacity_unit_allocations_with_options_async(
        self,
        request: ecs_20160314_models.DescribeStorageCapacityUnitAllocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeStorageCapacityUnitAllocationsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.storage_capacity_unit_id):
            query['StorageCapacityUnitId'] = request.storage_capacity_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageCapacityUnitAllocations',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeStorageCapacityUnitAllocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_capacity_unit_allocations(
        self,
        request: ecs_20160314_models.DescribeStorageCapacityUnitAllocationsRequest,
    ) -> ecs_20160314_models.DescribeStorageCapacityUnitAllocationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_capacity_unit_allocations_with_options(request, runtime)

    async def describe_storage_capacity_unit_allocations_async(
        self,
        request: ecs_20160314_models.DescribeStorageCapacityUnitAllocationsRequest,
    ) -> ecs_20160314_models.DescribeStorageCapacityUnitAllocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_capacity_unit_allocations_with_options_async(request, runtime)

    def describe_storage_capacity_unit_deduct_factor_with_options(
        self,
        request: ecs_20160314_models.DescribeStorageCapacityUnitDeductFactorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeStorageCapacityUnitDeductFactorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deduct_field):
            query['DeductField'] = request.deduct_field
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageCapacityUnitDeductFactor',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeStorageCapacityUnitDeductFactorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_capacity_unit_deduct_factor_with_options_async(
        self,
        request: ecs_20160314_models.DescribeStorageCapacityUnitDeductFactorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeStorageCapacityUnitDeductFactorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deduct_field):
            query['DeductField'] = request.deduct_field
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageCapacityUnitDeductFactor',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeStorageCapacityUnitDeductFactorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_capacity_unit_deduct_factor(
        self,
        request: ecs_20160314_models.DescribeStorageCapacityUnitDeductFactorRequest,
    ) -> ecs_20160314_models.DescribeStorageCapacityUnitDeductFactorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_capacity_unit_deduct_factor_with_options(request, runtime)

    async def describe_storage_capacity_unit_deduct_factor_async(
        self,
        request: ecs_20160314_models.DescribeStorageCapacityUnitDeductFactorRequest,
    ) -> ecs_20160314_models.DescribeStorageCapacityUnitDeductFactorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_capacity_unit_deduct_factor_with_options_async(request, runtime)

    def describe_storage_set_details_with_options(
        self,
        request: ecs_20160314_models.DescribeStorageSetDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeStorageSetDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
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
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageSetDetails',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeStorageSetDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_set_details_with_options_async(
        self,
        request: ecs_20160314_models.DescribeStorageSetDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeStorageSetDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
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
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageSetDetails',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeStorageSetDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_set_details(
        self,
        request: ecs_20160314_models.DescribeStorageSetDetailsRequest,
    ) -> ecs_20160314_models.DescribeStorageSetDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_set_details_with_options(request, runtime)

    async def describe_storage_set_details_async(
        self,
        request: ecs_20160314_models.DescribeStorageSetDetailsRequest,
    ) -> ecs_20160314_models.DescribeStorageSetDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_set_details_with_options_async(request, runtime)

    def describe_storage_sets_with_options(
        self,
        request: ecs_20160314_models.DescribeStorageSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeStorageSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.storage_set_ids):
            query['StorageSetIds'] = request.storage_set_ids
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageSets',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeStorageSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_sets_with_options_async(
        self,
        request: ecs_20160314_models.DescribeStorageSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeStorageSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.storage_set_ids):
            query['StorageSetIds'] = request.storage_set_ids
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageSets',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeStorageSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_sets(
        self,
        request: ecs_20160314_models.DescribeStorageSetsRequest,
    ) -> ecs_20160314_models.DescribeStorageSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_sets_with_options(request, runtime)

    async def describe_storage_sets_async(
        self,
        request: ecs_20160314_models.DescribeStorageSetsRequest,
    ) -> ecs_20160314_models.DescribeStorageSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_sets_with_options_async(request, runtime)

    def describe_transition_vswitches_with_options(
        self,
        request: ecs_20160314_models.DescribeTransitionVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeTransitionVSwitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransitionVSwitches',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeTransitionVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transition_vswitches_with_options_async(
        self,
        request: ecs_20160314_models.DescribeTransitionVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeTransitionVSwitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransitionVSwitches',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeTransitionVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transition_vswitches(
        self,
        request: ecs_20160314_models.DescribeTransitionVSwitchesRequest,
    ) -> ecs_20160314_models.DescribeTransitionVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_transition_vswitches_with_options(request, runtime)

    async def describe_transition_vswitches_async(
        self,
        request: ecs_20160314_models.DescribeTransitionVSwitchesRequest,
    ) -> ecs_20160314_models.DescribeTransitionVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transition_vswitches_with_options_async(request, runtime)

    def describe_transition_vpc_and_vswitch_with_options(
        self,
        request: ecs_20160314_models.DescribeTransitionVpcAndVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeTransitionVpcAndVSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransitionVpcAndVSwitch',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeTransitionVpcAndVSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transition_vpc_and_vswitch_with_options_async(
        self,
        request: ecs_20160314_models.DescribeTransitionVpcAndVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeTransitionVpcAndVSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransitionVpcAndVSwitch',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeTransitionVpcAndVSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transition_vpc_and_vswitch(
        self,
        request: ecs_20160314_models.DescribeTransitionVpcAndVSwitchRequest,
    ) -> ecs_20160314_models.DescribeTransitionVpcAndVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_transition_vpc_and_vswitch_with_options(request, runtime)

    async def describe_transition_vpc_and_vswitch_async(
        self,
        request: ecs_20160314_models.DescribeTransitionVpcAndVSwitchRequest,
    ) -> ecs_20160314_models.DescribeTransitionVpcAndVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transition_vpc_and_vswitch_with_options_async(request, runtime)

    def describe_transition_vpcs_with_options(
        self,
        request: ecs_20160314_models.DescribeTransitionVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeTransitionVpcsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransitionVpcs',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeTransitionVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transition_vpcs_with_options_async(
        self,
        request: ecs_20160314_models.DescribeTransitionVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeTransitionVpcsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransitionVpcs',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeTransitionVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transition_vpcs(
        self,
        request: ecs_20160314_models.DescribeTransitionVpcsRequest,
    ) -> ecs_20160314_models.DescribeTransitionVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_transition_vpcs_with_options(request, runtime)

    async def describe_transition_vpcs_async(
        self,
        request: ecs_20160314_models.DescribeTransitionVpcsRequest,
    ) -> ecs_20160314_models.DescribeTransitionVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transition_vpcs_with_options_async(request, runtime)

    def describe_user_available_ip_service_providers_with_options(
        self,
        request: ecs_20160314_models.DescribeUserAvailableIpServiceProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeUserAvailableIpServiceProvidersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
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
            action='DescribeUserAvailableIpServiceProviders',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeUserAvailableIpServiceProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_available_ip_service_providers_with_options_async(
        self,
        request: ecs_20160314_models.DescribeUserAvailableIpServiceProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeUserAvailableIpServiceProvidersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
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
            action='DescribeUserAvailableIpServiceProviders',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeUserAvailableIpServiceProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_available_ip_service_providers(
        self,
        request: ecs_20160314_models.DescribeUserAvailableIpServiceProvidersRequest,
    ) -> ecs_20160314_models.DescribeUserAvailableIpServiceProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_available_ip_service_providers_with_options(request, runtime)

    async def describe_user_available_ip_service_providers_async(
        self,
        request: ecs_20160314_models.DescribeUserAvailableIpServiceProvidersRequest,
    ) -> ecs_20160314_models.DescribeUserAvailableIpServiceProvidersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_available_ip_service_providers_with_options_async(request, runtime)

    def describe_user_quota_applications_with_options(
        self,
        request: ecs_20160314_models.DescribeUserQuotaApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeUserQuotaApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.quota_type):
            query['QuotaType'] = request.quota_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserQuotaApplications',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeUserQuotaApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_quota_applications_with_options_async(
        self,
        request: ecs_20160314_models.DescribeUserQuotaApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeUserQuotaApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.quota_type):
            query['QuotaType'] = request.quota_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserQuotaApplications',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeUserQuotaApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_quota_applications(
        self,
        request: ecs_20160314_models.DescribeUserQuotaApplicationsRequest,
    ) -> ecs_20160314_models.DescribeUserQuotaApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_quota_applications_with_options(request, runtime)

    async def describe_user_quota_applications_async(
        self,
        request: ecs_20160314_models.DescribeUserQuotaApplicationsRequest,
    ) -> ecs_20160314_models.DescribeUserQuotaApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_quota_applications_with_options_async(request, runtime)

    def describe_vpc_havs_instances_with_options(
        self,
        request: ecs_20160314_models.DescribeVpcHavsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeVpcHavsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result_size):
            query['MaxResultSize'] = request.max_result_size
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
        if not UtilClient.is_unset(request.vpc_id_list):
            query['VpcIdList'] = request.vpc_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcHavsInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeVpcHavsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_havs_instances_with_options_async(
        self,
        request: ecs_20160314_models.DescribeVpcHavsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeVpcHavsInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result_size):
            query['MaxResultSize'] = request.max_result_size
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
        if not UtilClient.is_unset(request.vpc_id_list):
            query['VpcIdList'] = request.vpc_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcHavsInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeVpcHavsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_havs_instances(
        self,
        request: ecs_20160314_models.DescribeVpcHavsInstancesRequest,
    ) -> ecs_20160314_models.DescribeVpcHavsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_havs_instances_with_options(request, runtime)

    async def describe_vpc_havs_instances_async(
        self,
        request: ecs_20160314_models.DescribeVpcHavsInstancesRequest,
    ) -> ecs_20160314_models.DescribeVpcHavsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_havs_instances_with_options_async(request, runtime)

    def describe_waiting_orders_with_options(
        self,
        request: ecs_20160314_models.DescribeWaitingOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeWaitingOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.waiting_order_id):
            query['WaitingOrderId'] = request.waiting_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWaitingOrders',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeWaitingOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waiting_orders_with_options_async(
        self,
        request: ecs_20160314_models.DescribeWaitingOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.DescribeWaitingOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.waiting_order_id):
            query['WaitingOrderId'] = request.waiting_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWaitingOrders',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.DescribeWaitingOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waiting_orders(
        self,
        request: ecs_20160314_models.DescribeWaitingOrdersRequest,
    ) -> ecs_20160314_models.DescribeWaitingOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_waiting_orders_with_options(request, runtime)

    async def describe_waiting_orders_async(
        self,
        request: ecs_20160314_models.DescribeWaitingOrdersRequest,
    ) -> ecs_20160314_models.DescribeWaitingOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_waiting_orders_with_options_async(request, runtime)

    def feedback_diagnose_with_options(
        self,
        request: ecs_20160314_models.FeedbackDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.FeedbackDiagnoseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnose_id):
            query['DiagnoseId'] = request.diagnose_id
        if not UtilClient.is_unset(request.mark):
            query['Mark'] = request.mark
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
        if not UtilClient.is_unset(request.star):
            query['Star'] = request.star
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FeedbackDiagnose',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.FeedbackDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_diagnose_with_options_async(
        self,
        request: ecs_20160314_models.FeedbackDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.FeedbackDiagnoseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnose_id):
            query['DiagnoseId'] = request.diagnose_id
        if not UtilClient.is_unset(request.mark):
            query['Mark'] = request.mark
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
        if not UtilClient.is_unset(request.star):
            query['Star'] = request.star
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FeedbackDiagnose',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.FeedbackDiagnoseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def feedback_diagnose(
        self,
        request: ecs_20160314_models.FeedbackDiagnoseRequest,
    ) -> ecs_20160314_models.FeedbackDiagnoseResponse:
        runtime = util_models.RuntimeOptions()
        return self.feedback_diagnose_with_options(request, runtime)

    async def feedback_diagnose_async(
        self,
        request: ecs_20160314_models.FeedbackDiagnoseRequest,
    ) -> ecs_20160314_models.FeedbackDiagnoseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.feedback_diagnose_with_options_async(request, runtime)

    def get_launch_template_data_with_options(
        self,
        request: ecs_20160314_models.GetLaunchTemplateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.GetLaunchTemplateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='GetLaunchTemplateData',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.GetLaunchTemplateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_launch_template_data_with_options_async(
        self,
        request: ecs_20160314_models.GetLaunchTemplateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.GetLaunchTemplateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='GetLaunchTemplateData',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.GetLaunchTemplateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_launch_template_data(
        self,
        request: ecs_20160314_models.GetLaunchTemplateDataRequest,
    ) -> ecs_20160314_models.GetLaunchTemplateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_launch_template_data_with_options(request, runtime)

    async def get_launch_template_data_async(
        self,
        request: ecs_20160314_models.GetLaunchTemplateDataRequest,
    ) -> ecs_20160314_models.GetLaunchTemplateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_launch_template_data_with_options_async(request, runtime)

    def inner_describe_network_interface_in_group_with_options(
        self,
        request: ecs_20160314_models.InnerDescribeNetworkInterfaceInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.InnerDescribeNetworkInterfaceInGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InnerDescribeNetworkInterfaceInGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.InnerDescribeNetworkInterfaceInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def inner_describe_network_interface_in_group_with_options_async(
        self,
        request: ecs_20160314_models.InnerDescribeNetworkInterfaceInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.InnerDescribeNetworkInterfaceInGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InnerDescribeNetworkInterfaceInGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.InnerDescribeNetworkInterfaceInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inner_describe_network_interface_in_group(
        self,
        request: ecs_20160314_models.InnerDescribeNetworkInterfaceInGroupRequest,
    ) -> ecs_20160314_models.InnerDescribeNetworkInterfaceInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.inner_describe_network_interface_in_group_with_options(request, runtime)

    async def inner_describe_network_interface_in_group_async(
        self,
        request: ecs_20160314_models.InnerDescribeNetworkInterfaceInGroupRequest,
    ) -> ecs_20160314_models.InnerDescribeNetworkInterfaceInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.inner_describe_network_interface_in_group_with_options_async(request, runtime)

    def join_eni_qos_group_with_options(
        self,
        request: ecs_20160314_models.JoinEniQosGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.JoinEniQosGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_group_name):
            query['QosGroupName'] = request.qos_group_name
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
            action='JoinEniQosGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.JoinEniQosGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_eni_qos_group_with_options_async(
        self,
        request: ecs_20160314_models.JoinEniQosGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.JoinEniQosGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_group_name):
            query['QosGroupName'] = request.qos_group_name
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
            action='JoinEniQosGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.JoinEniQosGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_eni_qos_group(
        self,
        request: ecs_20160314_models.JoinEniQosGroupRequest,
    ) -> ecs_20160314_models.JoinEniQosGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_eni_qos_group_with_options(request, runtime)

    async def join_eni_qos_group_async(
        self,
        request: ecs_20160314_models.JoinEniQosGroupRequest,
    ) -> ecs_20160314_models.JoinEniQosGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_eni_qos_group_with_options_async(request, runtime)

    def leave_eni_qos_group_with_options(
        self,
        request: ecs_20160314_models.LeaveEniQosGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.LeaveEniQosGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
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
            action='LeaveEniQosGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.LeaveEniQosGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def leave_eni_qos_group_with_options_async(
        self,
        request: ecs_20160314_models.LeaveEniQosGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.LeaveEniQosGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
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
            action='LeaveEniQosGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.LeaveEniQosGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def leave_eni_qos_group(
        self,
        request: ecs_20160314_models.LeaveEniQosGroupRequest,
    ) -> ecs_20160314_models.LeaveEniQosGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.leave_eni_qos_group_with_options(request, runtime)

    async def leave_eni_qos_group_async(
        self,
        request: ecs_20160314_models.LeaveEniQosGroupRequest,
    ) -> ecs_20160314_models.LeaveEniQosGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.leave_eni_qos_group_with_options_async(request, runtime)

    def list_account_ecs_quotas_with_options(
        self,
        request: ecs_20160314_models.ListAccountEcsQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ListAccountEcsQuotasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_resource_name):
            query['QuotaResourceName'] = request.quota_resource_name
        if not UtilClient.is_unset(request.quota_resource_type):
            query['QuotaResourceType'] = request.quota_resource_type
        if not UtilClient.is_unset(request.quota_unit):
            query['QuotaUnit'] = request.quota_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountEcsQuotas',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ListAccountEcsQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_account_ecs_quotas_with_options_async(
        self,
        request: ecs_20160314_models.ListAccountEcsQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ListAccountEcsQuotasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_resource_name):
            query['QuotaResourceName'] = request.quota_resource_name
        if not UtilClient.is_unset(request.quota_resource_type):
            query['QuotaResourceType'] = request.quota_resource_type
        if not UtilClient.is_unset(request.quota_unit):
            query['QuotaUnit'] = request.quota_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountEcsQuotas',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ListAccountEcsQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_account_ecs_quotas(
        self,
        request: ecs_20160314_models.ListAccountEcsQuotasRequest,
    ) -> ecs_20160314_models.ListAccountEcsQuotasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_account_ecs_quotas_with_options(request, runtime)

    async def list_account_ecs_quotas_async(
        self,
        request: ecs_20160314_models.ListAccountEcsQuotasRequest,
    ) -> ecs_20160314_models.ListAccountEcsQuotasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_account_ecs_quotas_with_options_async(request, runtime)

    def list_service_settings_with_options(
        self,
        request: ecs_20160314_models.ListServiceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ListServiceSettingsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_assistant_delivery_settings):
            query['CloudAssistantDeliverySettings'] = request.cloud_assistant_delivery_settings
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
            action='ListServiceSettings',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ListServiceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_settings_with_options_async(
        self,
        request: ecs_20160314_models.ListServiceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ListServiceSettingsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_assistant_delivery_settings):
            query['CloudAssistantDeliverySettings'] = request.cloud_assistant_delivery_settings
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
            action='ListServiceSettings',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ListServiceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_settings(
        self,
        request: ecs_20160314_models.ListServiceSettingsRequest,
    ) -> ecs_20160314_models.ListServiceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_service_settings_with_options(request, runtime)

    async def list_service_settings_async(
        self,
        request: ecs_20160314_models.ListServiceSettingsRequest,
    ) -> ecs_20160314_models.ListServiceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_service_settings_with_options_async(request, runtime)

    def modify_capacity_reservation_with_options(
        self,
        request: ecs_20160314_models.ModifyCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyCapacityReservationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity_reservation_id):
            query['CapacityReservationId'] = request.capacity_reservation_id
        if not UtilClient.is_unset(request.instance_count):
            query['InstanceCount'] = request.instance_count
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
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCapacityReservation',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyCapacityReservationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_capacity_reservation_with_options_async(
        self,
        request: ecs_20160314_models.ModifyCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyCapacityReservationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity_reservation_id):
            query['CapacityReservationId'] = request.capacity_reservation_id
        if not UtilClient.is_unset(request.instance_count):
            query['InstanceCount'] = request.instance_count
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
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCapacityReservation',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyCapacityReservationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_capacity_reservation(
        self,
        request: ecs_20160314_models.ModifyCapacityReservationRequest,
    ) -> ecs_20160314_models.ModifyCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_capacity_reservation_with_options(request, runtime)

    async def modify_capacity_reservation_async(
        self,
        request: ecs_20160314_models.ModifyCapacityReservationRequest,
    ) -> ecs_20160314_models.ModifyCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_capacity_reservation_with_options_async(request, runtime)

    def modify_dedicated_host_attribute_with_options(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_on_maintenance):
            query['ActionOnMaintenance'] = request.action_on_maintenance
        if not UtilClient.is_unset(request.auto_placement):
            query['AutoPlacement'] = request.auto_placement
        if not UtilClient.is_unset(request.cpu_over_commit_ratio):
            query['CpuOverCommitRatio'] = request.cpu_over_commit_ratio
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.network_attributes):
            query['NetworkAttributes'] = request.network_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDedicatedHostAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_attribute_with_options_async(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_on_maintenance):
            query['ActionOnMaintenance'] = request.action_on_maintenance
        if not UtilClient.is_unset(request.auto_placement):
            query['AutoPlacement'] = request.auto_placement
        if not UtilClient.is_unset(request.cpu_over_commit_ratio):
            query['CpuOverCommitRatio'] = request.cpu_over_commit_ratio
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.network_attributes):
            query['NetworkAttributes'] = request.network_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDedicatedHostAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_attribute(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAttributeRequest,
    ) -> ecs_20160314_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    async def modify_dedicated_host_attribute_async(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAttributeRequest,
    ) -> ecs_20160314_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_auto_release_time_with_options(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyDedicatedHostAutoReleaseTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDedicatedHostAutoReleaseTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_auto_release_time_with_options_async(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyDedicatedHostAutoReleaseTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDedicatedHostAutoReleaseTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_auto_release_time(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAutoReleaseTimeRequest,
    ) -> ecs_20160314_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_auto_release_time_with_options(request, runtime)

    async def modify_dedicated_host_auto_release_time_async(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAutoReleaseTimeRequest,
    ) -> ecs_20160314_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_auto_release_time_with_options_async(request, runtime)

    def modify_dedicated_host_auto_renew_attribute_with_options(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAutoRenewAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDedicatedHostAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_auto_renew_attribute_with_options_async(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAutoRenewAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDedicatedHostAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_auto_renew_attribute(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAutoRenewAttributeRequest,
    ) -> ecs_20160314_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_auto_renew_attribute_with_options(request, runtime)

    async def modify_dedicated_host_auto_renew_attribute_async(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostAutoRenewAttributeRequest,
    ) -> ecs_20160314_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_auto_renew_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_cluster_attribute_with_options(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDedicatedHostClusterAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_cluster_name):
            query['DedicatedHostClusterName'] = request.dedicated_host_cluster_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
            action='ModifyDedicatedHostClusterAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDedicatedHostClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_cluster_attribute_with_options_async(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDedicatedHostClusterAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_cluster_name):
            query['DedicatedHostClusterName'] = request.dedicated_host_cluster_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
            action='ModifyDedicatedHostClusterAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDedicatedHostClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_cluster_attribute(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostClusterAttributeRequest,
    ) -> ecs_20160314_models.ModifyDedicatedHostClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_cluster_attribute_with_options(request, runtime)

    async def modify_dedicated_host_cluster_attribute_async(
        self,
        request: ecs_20160314_models.ModifyDedicatedHostClusterAttributeRequest,
    ) -> ecs_20160314_models.ModifyDedicatedHostClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_cluster_attribute_with_options_async(request, runtime)

    def modify_diagnose_with_options(
        self,
        request: ecs_20160314_models.ModifyDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDiagnoseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnose_id):
            query['DiagnoseId'] = request.diagnose_id
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiagnose',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_diagnose_with_options_async(
        self,
        request: ecs_20160314_models.ModifyDiagnoseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDiagnoseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnose_id):
            query['DiagnoseId'] = request.diagnose_id
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiagnose',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDiagnoseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_diagnose(
        self,
        request: ecs_20160314_models.ModifyDiagnoseRequest,
    ) -> ecs_20160314_models.ModifyDiagnoseResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_diagnose_with_options(request, runtime)

    async def modify_diagnose_async(
        self,
        request: ecs_20160314_models.ModifyDiagnoseRequest,
    ) -> ecs_20160314_models.ModifyDiagnoseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_diagnose_with_options_async(request, runtime)

    def modify_disk_spec_with_options(
        self,
        request: ecs_20160314_models.ModifyDiskSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDiskSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskSpec',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDiskSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_spec_with_options_async(
        self,
        request: ecs_20160314_models.ModifyDiskSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyDiskSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskSpec',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyDiskSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_spec(
        self,
        request: ecs_20160314_models.ModifyDiskSpecRequest,
    ) -> ecs_20160314_models.ModifyDiskSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_spec_with_options(request, runtime)

    async def modify_disk_spec_async(
        self,
        request: ecs_20160314_models.ModifyDiskSpecRequest,
    ) -> ecs_20160314_models.ModifyDiskSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_spec_with_options_async(request, runtime)

    def modify_eni_qos_group_with_options(
        self,
        request: ecs_20160314_models.ModifyEniQosGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyEniQosGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_group_name):
            query['QosGroupName'] = request.qos_group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rx):
            query['Rx'] = request.rx
        if not UtilClient.is_unset(request.rx_pps):
            query['RxPps'] = request.rx_pps
        if not UtilClient.is_unset(request.tx):
            query['Tx'] = request.tx
        if not UtilClient.is_unset(request.tx_pps):
            query['TxPps'] = request.tx_pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEniQosGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyEniQosGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_eni_qos_group_with_options_async(
        self,
        request: ecs_20160314_models.ModifyEniQosGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyEniQosGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_group_name):
            query['QosGroupName'] = request.qos_group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rx):
            query['Rx'] = request.rx
        if not UtilClient.is_unset(request.rx_pps):
            query['RxPps'] = request.rx_pps
        if not UtilClient.is_unset(request.tx):
            query['Tx'] = request.tx
        if not UtilClient.is_unset(request.tx_pps):
            query['TxPps'] = request.tx_pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEniQosGroup',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyEniQosGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_eni_qos_group(
        self,
        request: ecs_20160314_models.ModifyEniQosGroupRequest,
    ) -> ecs_20160314_models.ModifyEniQosGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_eni_qos_group_with_options(request, runtime)

    async def modify_eni_qos_group_async(
        self,
        request: ecs_20160314_models.ModifyEniQosGroupRequest,
    ) -> ecs_20160314_models.ModifyEniQosGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_eni_qos_group_with_options_async(request, runtime)

    def modify_image_advanced_attribute_with_options(
        self,
        request: ecs_20160314_models.ModifyImageAdvancedAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyImageAdvancedAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.support_io_optimized):
            query['SupportIoOptimized'] = request.support_io_optimized
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageAdvancedAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyImageAdvancedAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_image_advanced_attribute_with_options_async(
        self,
        request: ecs_20160314_models.ModifyImageAdvancedAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyImageAdvancedAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.support_io_optimized):
            query['SupportIoOptimized'] = request.support_io_optimized
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageAdvancedAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyImageAdvancedAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_image_advanced_attribute(
        self,
        request: ecs_20160314_models.ModifyImageAdvancedAttributeRequest,
    ) -> ecs_20160314_models.ModifyImageAdvancedAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_advanced_attribute_with_options(request, runtime)

    async def modify_image_advanced_attribute_async(
        self,
        request: ecs_20160314_models.ModifyImageAdvancedAttributeRequest,
    ) -> ecs_20160314_models.ModifyImageAdvancedAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_advanced_attribute_with_options_async(request, runtime)

    def modify_instance_auto_reboot_time_with_options(
        self,
        request: ecs_20160314_models.ModifyInstanceAutoRebootTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyInstanceAutoRebootTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_reboot_time):
            query['AutoRebootTime'] = request.auto_reboot_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
            action='ModifyInstanceAutoRebootTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyInstanceAutoRebootTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_auto_reboot_time_with_options_async(
        self,
        request: ecs_20160314_models.ModifyInstanceAutoRebootTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyInstanceAutoRebootTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_reboot_time):
            query['AutoRebootTime'] = request.auto_reboot_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
            action='ModifyInstanceAutoRebootTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyInstanceAutoRebootTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_auto_reboot_time(
        self,
        request: ecs_20160314_models.ModifyInstanceAutoRebootTimeRequest,
    ) -> ecs_20160314_models.ModifyInstanceAutoRebootTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_reboot_time_with_options(request, runtime)

    async def modify_instance_auto_reboot_time_async(
        self,
        request: ecs_20160314_models.ModifyInstanceAutoRebootTimeRequest,
    ) -> ecs_20160314_models.ModifyInstanceAutoRebootTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_reboot_time_with_options_async(request, runtime)

    def modify_instance_capacity_reservation_attributes_with_options(
        self,
        request: ecs_20160314_models.ModifyInstanceCapacityReservationAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyInstanceCapacityReservationAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity_reservation_id):
            query['CapacityReservationId'] = request.capacity_reservation_id
        if not UtilClient.is_unset(request.capacity_reservation_preference):
            query['CapacityReservationPreference'] = request.capacity_reservation_preference
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyInstanceCapacityReservationAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyInstanceCapacityReservationAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_capacity_reservation_attributes_with_options_async(
        self,
        request: ecs_20160314_models.ModifyInstanceCapacityReservationAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyInstanceCapacityReservationAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity_reservation_id):
            query['CapacityReservationId'] = request.capacity_reservation_id
        if not UtilClient.is_unset(request.capacity_reservation_preference):
            query['CapacityReservationPreference'] = request.capacity_reservation_preference
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyInstanceCapacityReservationAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyInstanceCapacityReservationAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_capacity_reservation_attributes(
        self,
        request: ecs_20160314_models.ModifyInstanceCapacityReservationAttributesRequest,
    ) -> ecs_20160314_models.ModifyInstanceCapacityReservationAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_capacity_reservation_attributes_with_options(request, runtime)

    async def modify_instance_capacity_reservation_attributes_async(
        self,
        request: ecs_20160314_models.ModifyInstanceCapacityReservationAttributesRequest,
    ) -> ecs_20160314_models.ModifyInstanceCapacityReservationAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_capacity_reservation_attributes_with_options_async(request, runtime)

    def modify_instance_charge_type_with_options(
        self,
        request: ecs_20160314_models.ModifyInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.include_data_disks):
            query['IncludeDataDisks'] = request.include_data_disks
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.is_detail_fee):
            query['IsDetailFee'] = request.is_detail_fee
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
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
            action='ModifyInstanceChargeType',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_charge_type_with_options_async(
        self,
        request: ecs_20160314_models.ModifyInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.include_data_disks):
            query['IncludeDataDisks'] = request.include_data_disks
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.is_detail_fee):
            query['IsDetailFee'] = request.is_detail_fee
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
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
            action='ModifyInstanceChargeType',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyInstanceChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_charge_type(
        self,
        request: ecs_20160314_models.ModifyInstanceChargeTypeRequest,
    ) -> ecs_20160314_models.ModifyInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_charge_type_with_options(request, runtime)

    async def modify_instance_charge_type_async(
        self,
        request: ecs_20160314_models.ModifyInstanceChargeTypeRequest,
    ) -> ecs_20160314_models.ModifyInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_charge_type_with_options_async(request, runtime)

    def modify_instance_deployment_with_options(
        self,
        request: ecs_20160314_models.ModifyInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.migration_type):
            query['MigrationType'] = request.migration_type
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
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceDeployment',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyInstanceDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_deployment_with_options_async(
        self,
        request: ecs_20160314_models.ModifyInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.migration_type):
            query['MigrationType'] = request.migration_type
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
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceDeployment',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyInstanceDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_deployment(
        self,
        request: ecs_20160314_models.ModifyInstanceDeploymentRequest,
    ) -> ecs_20160314_models.ModifyInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_deployment_with_options(request, runtime)

    async def modify_instance_deployment_async(
        self,
        request: ecs_20160314_models.ModifyInstanceDeploymentRequest,
    ) -> ecs_20160314_models.ModifyInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_deployment_with_options_async(request, runtime)

    def modify_instance_maintenance_attributes_with_options(
        self,
        request: ecs_20160314_models.ModifyInstanceMaintenanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyInstanceMaintenanceAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_on_maintenance):
            query['ActionOnMaintenance'] = request.action_on_maintenance
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.live_migration):
            query['LiveMigration'] = request.live_migration
        if not UtilClient.is_unset(request.maintenance_window):
            query['MaintenanceWindow'] = request.maintenance_window
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
            action='ModifyInstanceMaintenanceAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyInstanceMaintenanceAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_maintenance_attributes_with_options_async(
        self,
        request: ecs_20160314_models.ModifyInstanceMaintenanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyInstanceMaintenanceAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_on_maintenance):
            query['ActionOnMaintenance'] = request.action_on_maintenance
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.live_migration):
            query['LiveMigration'] = request.live_migration
        if not UtilClient.is_unset(request.maintenance_window):
            query['MaintenanceWindow'] = request.maintenance_window
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
            action='ModifyInstanceMaintenanceAttributes',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyInstanceMaintenanceAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_maintenance_attributes(
        self,
        request: ecs_20160314_models.ModifyInstanceMaintenanceAttributesRequest,
    ) -> ecs_20160314_models.ModifyInstanceMaintenanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintenance_attributes_with_options(request, runtime)

    async def modify_instance_maintenance_attributes_async(
        self,
        request: ecs_20160314_models.ModifyInstanceMaintenanceAttributesRequest,
    ) -> ecs_20160314_models.ModifyInstanceMaintenanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_maintenance_attributes_with_options_async(request, runtime)

    def modify_migratable_instances_with_options(
        self,
        request: ecs_20160314_models.ModifyMigratableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyMigratableInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_migration_type):
            query['BusinessMigrationType'] = request.business_migration_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMigratableInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyMigratableInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_migratable_instances_with_options_async(
        self,
        request: ecs_20160314_models.ModifyMigratableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyMigratableInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_migration_type):
            query['BusinessMigrationType'] = request.business_migration_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMigratableInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyMigratableInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_migratable_instances(
        self,
        request: ecs_20160314_models.ModifyMigratableInstancesRequest,
    ) -> ecs_20160314_models.ModifyMigratableInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_migratable_instances_with_options(request, runtime)

    async def modify_migratable_instances_async(
        self,
        request: ecs_20160314_models.ModifyMigratableInstancesRequest,
    ) -> ecs_20160314_models.ModifyMigratableInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_migratable_instances_with_options_async(request, runtime)

    def modify_migration_instances_with_options(
        self,
        request: ecs_20160314_models.ModifyMigrationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyMigrationInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_migration_time):
            query['GlobalMigrationTime'] = request.global_migration_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
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
            action='ModifyMigrationInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyMigrationInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_migration_instances_with_options_async(
        self,
        request: ecs_20160314_models.ModifyMigrationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyMigrationInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_migration_time):
            query['GlobalMigrationTime'] = request.global_migration_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
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
            action='ModifyMigrationInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyMigrationInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_migration_instances(
        self,
        request: ecs_20160314_models.ModifyMigrationInstancesRequest,
    ) -> ecs_20160314_models.ModifyMigrationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_migration_instances_with_options(request, runtime)

    async def modify_migration_instances_async(
        self,
        request: ecs_20160314_models.ModifyMigrationInstancesRequest,
    ) -> ecs_20160314_models.ModifyMigrationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_migration_instances_with_options_async(request, runtime)

    def modify_migration_plan_with_options(
        self,
        request: ecs_20160314_models.ModifyMigrationPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyMigrationPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_plan_id):
            query['MigrationPlanId'] = request.migration_plan_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
            action='ModifyMigrationPlan',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyMigrationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_migration_plan_with_options_async(
        self,
        request: ecs_20160314_models.ModifyMigrationPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyMigrationPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_plan_id):
            query['MigrationPlanId'] = request.migration_plan_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
            action='ModifyMigrationPlan',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyMigrationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_migration_plan(
        self,
        request: ecs_20160314_models.ModifyMigrationPlanRequest,
    ) -> ecs_20160314_models.ModifyMigrationPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_migration_plan_with_options(request, runtime)

    async def modify_migration_plan_async(
        self,
        request: ecs_20160314_models.ModifyMigrationPlanRequest,
    ) -> ecs_20160314_models.ModifyMigrationPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_migration_plan_with_options_async(request, runtime)

    def modify_order_auto_reboot_time_with_options(
        self,
        request: ecs_20160314_models.ModifyOrderAutoRebootTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyOrderAutoRebootTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_reboot_time):
            query['AutoRebootTime'] = request.auto_reboot_time
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
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
            action='ModifyOrderAutoRebootTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyOrderAutoRebootTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_order_auto_reboot_time_with_options_async(
        self,
        request: ecs_20160314_models.ModifyOrderAutoRebootTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyOrderAutoRebootTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_reboot_time):
            query['AutoRebootTime'] = request.auto_reboot_time
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
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
            action='ModifyOrderAutoRebootTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyOrderAutoRebootTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_order_auto_reboot_time(
        self,
        request: ecs_20160314_models.ModifyOrderAutoRebootTimeRequest,
    ) -> ecs_20160314_models.ModifyOrderAutoRebootTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_order_auto_reboot_time_with_options(request, runtime)

    async def modify_order_auto_reboot_time_async(
        self,
        request: ecs_20160314_models.ModifyOrderAutoRebootTimeRequest,
    ) -> ecs_20160314_models.ModifyOrderAutoRebootTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_order_auto_reboot_time_with_options_async(request, runtime)

    def modify_private_pool_with_options(
        self,
        request: ecs_20160314_models.ModifyPrivatePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyPrivatePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_time_type):
            query['EndTimeType'] = request.end_time_type
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPrivatePool',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyPrivatePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_private_pool_with_options_async(
        self,
        request: ecs_20160314_models.ModifyPrivatePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyPrivatePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_time_type):
            query['EndTimeType'] = request.end_time_type
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPrivatePool',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyPrivatePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_private_pool(
        self,
        request: ecs_20160314_models.ModifyPrivatePoolRequest,
    ) -> ecs_20160314_models.ModifyPrivatePoolResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_private_pool_with_options(request, runtime)

    async def modify_private_pool_async(
        self,
        request: ecs_20160314_models.ModifyPrivatePoolRequest,
    ) -> ecs_20160314_models.ModifyPrivatePoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_private_pool_with_options_async(request, runtime)

    def modify_reservation_demand_with_options(
        self,
        request: ecs_20160314_models.ModifyReservationDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyReservationDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.confirm_type):
            query['ConfirmType'] = request.confirm_type
        if not UtilClient.is_unset(request.coupon_auto):
            query['CouponAuto'] = request.coupon_auto
        if not UtilClient.is_unset(request.coupon_type):
            query['CouponType'] = request.coupon_type
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_cpu_core_count):
            query['InstanceCpuCoreCount'] = request.instance_cpu_core_count
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.match_criteria):
            query['MatchCriteria'] = request.match_criteria
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_description):
            query['ReservedInstanceDescription'] = request.reserved_instance_description
        if not UtilClient.is_unset(request.reserved_instance_group_id):
            query['ReservedInstanceGroupId'] = request.reserved_instance_group_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.reserved_instance_offering_type):
            query['ReservedInstanceOfferingType'] = request.reserved_instance_offering_type
        if not UtilClient.is_unset(request.reserved_instance_scope):
            query['ReservedInstanceScope'] = request.reserved_instance_scope
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_supply_type):
            query['ResourceSupplyType'] = request.resource_supply_type
        if not UtilClient.is_unset(request.saving_plan_description):
            query['SavingPlanDescription'] = request.saving_plan_description
        if not UtilClient.is_unset(request.saving_plan_hour_fee):
            query['SavingPlanHourFee'] = request.saving_plan_hour_fee
        if not UtilClient.is_unset(request.saving_plan_id):
            query['SavingPlanId'] = request.saving_plan_id
        if not UtilClient.is_unset(request.saving_plan_instance_type_family_group):
            query['SavingPlanInstanceTypeFamilyGroup'] = request.saving_plan_instance_type_family_group
        if not UtilClient.is_unset(request.saving_plan_name):
            query['SavingPlanName'] = request.saving_plan_name
        if not UtilClient.is_unset(request.saving_plan_pay_mode):
            query['SavingPlanPayMode'] = request.saving_plan_pay_mode
        if not UtilClient.is_unset(request.saving_plan_saving_type):
            query['SavingPlanSavingType'] = request.saving_plan_saving_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_ids):
            query['ZoneIds'] = request.zone_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyReservationDemand',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyReservationDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_reservation_demand_with_options_async(
        self,
        request: ecs_20160314_models.ModifyReservationDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyReservationDemandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.confirm_type):
            query['ConfirmType'] = request.confirm_type
        if not UtilClient.is_unset(request.coupon_auto):
            query['CouponAuto'] = request.coupon_auto
        if not UtilClient.is_unset(request.coupon_type):
            query['CouponType'] = request.coupon_type
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_cpu_core_count):
            query['InstanceCpuCoreCount'] = request.instance_cpu_core_count
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.match_criteria):
            query['MatchCriteria'] = request.match_criteria
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_description):
            query['ReservedInstanceDescription'] = request.reserved_instance_description
        if not UtilClient.is_unset(request.reserved_instance_group_id):
            query['ReservedInstanceGroupId'] = request.reserved_instance_group_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.reserved_instance_offering_type):
            query['ReservedInstanceOfferingType'] = request.reserved_instance_offering_type
        if not UtilClient.is_unset(request.reserved_instance_scope):
            query['ReservedInstanceScope'] = request.reserved_instance_scope
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_supply_type):
            query['ResourceSupplyType'] = request.resource_supply_type
        if not UtilClient.is_unset(request.saving_plan_description):
            query['SavingPlanDescription'] = request.saving_plan_description
        if not UtilClient.is_unset(request.saving_plan_hour_fee):
            query['SavingPlanHourFee'] = request.saving_plan_hour_fee
        if not UtilClient.is_unset(request.saving_plan_id):
            query['SavingPlanId'] = request.saving_plan_id
        if not UtilClient.is_unset(request.saving_plan_instance_type_family_group):
            query['SavingPlanInstanceTypeFamilyGroup'] = request.saving_plan_instance_type_family_group
        if not UtilClient.is_unset(request.saving_plan_name):
            query['SavingPlanName'] = request.saving_plan_name
        if not UtilClient.is_unset(request.saving_plan_pay_mode):
            query['SavingPlanPayMode'] = request.saving_plan_pay_mode
        if not UtilClient.is_unset(request.saving_plan_saving_type):
            query['SavingPlanSavingType'] = request.saving_plan_saving_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_ids):
            query['ZoneIds'] = request.zone_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyReservationDemand',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyReservationDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_reservation_demand(
        self,
        request: ecs_20160314_models.ModifyReservationDemandRequest,
    ) -> ecs_20160314_models.ModifyReservationDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_reservation_demand_with_options(request, runtime)

    async def modify_reservation_demand_async(
        self,
        request: ecs_20160314_models.ModifyReservationDemandRequest,
    ) -> ecs_20160314_models.ModifyReservationDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_reservation_demand_with_options_async(request, runtime)

    def modify_reserved_instance_attribute_with_options(
        self,
        request: ecs_20160314_models.ModifyReservedInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyReservedInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyReservedInstanceAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyReservedInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_reserved_instance_attribute_with_options_async(
        self,
        request: ecs_20160314_models.ModifyReservedInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyReservedInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyReservedInstanceAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyReservedInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_reserved_instance_attribute(
        self,
        request: ecs_20160314_models.ModifyReservedInstanceAttributeRequest,
    ) -> ecs_20160314_models.ModifyReservedInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_reserved_instance_attribute_with_options(request, runtime)

    async def modify_reserved_instance_attribute_async(
        self,
        request: ecs_20160314_models.ModifyReservedInstanceAttributeRequest,
    ) -> ecs_20160314_models.ModifyReservedInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_reserved_instance_attribute_with_options_async(request, runtime)

    def modify_reserved_instances_with_options(
        self,
        request: ecs_20160314_models.ModifyReservedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyReservedInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration):
            query['Configuration'] = request.configuration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
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
            action='ModifyReservedInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyReservedInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_reserved_instances_with_options_async(
        self,
        request: ecs_20160314_models.ModifyReservedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyReservedInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration):
            query['Configuration'] = request.configuration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
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
            action='ModifyReservedInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyReservedInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_reserved_instances(
        self,
        request: ecs_20160314_models.ModifyReservedInstancesRequest,
    ) -> ecs_20160314_models.ModifyReservedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_reserved_instances_with_options(request, runtime)

    async def modify_reserved_instances_async(
        self,
        request: ecs_20160314_models.ModifyReservedInstancesRequest,
    ) -> ecs_20160314_models.ModifyReservedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_reserved_instances_with_options_async(request, runtime)

    def modify_resource_diagnosis_status_with_options(
        self,
        request: ecs_20160314_models.ModifyResourceDiagnosisStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyResourceDiagnosisStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnosis_status):
            query['DiagnosisStatus'] = request.diagnosis_status
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceDiagnosisStatus',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyResourceDiagnosisStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_diagnosis_status_with_options_async(
        self,
        request: ecs_20160314_models.ModifyResourceDiagnosisStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyResourceDiagnosisStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnosis_status):
            query['DiagnosisStatus'] = request.diagnosis_status
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceDiagnosisStatus',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyResourceDiagnosisStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_diagnosis_status(
        self,
        request: ecs_20160314_models.ModifyResourceDiagnosisStatusRequest,
    ) -> ecs_20160314_models.ModifyResourceDiagnosisStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_diagnosis_status_with_options(request, runtime)

    async def modify_resource_diagnosis_status_async(
        self,
        request: ecs_20160314_models.ModifyResourceDiagnosisStatusRequest,
    ) -> ecs_20160314_models.ModifyResourceDiagnosisStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_diagnosis_status_with_options_async(request, runtime)

    def modify_resource_meta_with_options(
        self,
        request: ecs_20160314_models.ModifyResourceMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyResourceMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.meta):
            query['Meta'] = request.meta
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceMeta',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyResourceMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_meta_with_options_async(
        self,
        request: ecs_20160314_models.ModifyResourceMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyResourceMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.meta):
            query['Meta'] = request.meta
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceMeta',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyResourceMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_meta(
        self,
        request: ecs_20160314_models.ModifyResourceMetaRequest,
    ) -> ecs_20160314_models.ModifyResourceMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_meta_with_options(request, runtime)

    async def modify_resource_meta_async(
        self,
        request: ecs_20160314_models.ModifyResourceMetaRequest,
    ) -> ecs_20160314_models.ModifyResourceMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_meta_with_options_async(request, runtime)

    def modify_storage_set_attribute_with_options(
        self,
        request: ecs_20160314_models.ModifyStorageSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyStorageSetAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStorageSetAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyStorageSetAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_storage_set_attribute_with_options_async(
        self,
        request: ecs_20160314_models.ModifyStorageSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyStorageSetAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStorageSetAttribute',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyStorageSetAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_storage_set_attribute(
        self,
        request: ecs_20160314_models.ModifyStorageSetAttributeRequest,
    ) -> ecs_20160314_models.ModifyStorageSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_set_attribute_with_options(request, runtime)

    async def modify_storage_set_attribute_async(
        self,
        request: ecs_20160314_models.ModifyStorageSetAttributeRequest,
    ) -> ecs_20160314_models.ModifyStorageSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_storage_set_attribute_with_options_async(request, runtime)

    def modify_waiting_order_with_options(
        self,
        request: ecs_20160314_models.ModifyWaitingOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyWaitingOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.waiting_order_id):
            query['WaitingOrderId'] = request.waiting_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWaitingOrder',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyWaitingOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_waiting_order_with_options_async(
        self,
        request: ecs_20160314_models.ModifyWaitingOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ModifyWaitingOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.waiting_order_id):
            query['WaitingOrderId'] = request.waiting_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWaitingOrder',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ModifyWaitingOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_waiting_order(
        self,
        request: ecs_20160314_models.ModifyWaitingOrderRequest,
    ) -> ecs_20160314_models.ModifyWaitingOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_waiting_order_with_options(request, runtime)

    async def modify_waiting_order_async(
        self,
        request: ecs_20160314_models.ModifyWaitingOrderRequest,
    ) -> ecs_20160314_models.ModifyWaitingOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_waiting_order_with_options_async(request, runtime)

    def purchase_reserved_instances_offering_with_options(
        self,
        request: ecs_20160314_models.PurchaseReservedInstancesOfferingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.PurchaseReservedInstancesOfferingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseReservedInstancesOffering',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.PurchaseReservedInstancesOfferingResponse(),
            self.call_api(params, req, runtime)
        )

    async def purchase_reserved_instances_offering_with_options_async(
        self,
        request: ecs_20160314_models.PurchaseReservedInstancesOfferingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.PurchaseReservedInstancesOfferingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseReservedInstancesOffering',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.PurchaseReservedInstancesOfferingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purchase_reserved_instances_offering(
        self,
        request: ecs_20160314_models.PurchaseReservedInstancesOfferingRequest,
    ) -> ecs_20160314_models.PurchaseReservedInstancesOfferingResponse:
        runtime = util_models.RuntimeOptions()
        return self.purchase_reserved_instances_offering_with_options(request, runtime)

    async def purchase_reserved_instances_offering_async(
        self,
        request: ecs_20160314_models.PurchaseReservedInstancesOfferingRequest,
    ) -> ecs_20160314_models.PurchaseReservedInstancesOfferingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purchase_reserved_instances_offering_with_options_async(request, runtime)

    def purchase_saving_plan_offering_with_options(
        self,
        request: ecs_20160314_models.PurchaseSavingPlanOfferingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.PurchaseSavingPlanOfferingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.committed_amount):
            query['CommittedAmount'] = request.committed_amount
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_family):
            query['InstanceFamily'] = request.instance_family
        if not UtilClient.is_unset(request.instance_family_set):
            query['InstanceFamilySet'] = request.instance_family_set
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.plan_type):
            query['PlanType'] = request.plan_type
        if not UtilClient.is_unset(request.purchase_method):
            query['PurchaseMethod'] = request.purchase_method
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseSavingPlanOffering',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.PurchaseSavingPlanOfferingResponse(),
            self.call_api(params, req, runtime)
        )

    async def purchase_saving_plan_offering_with_options_async(
        self,
        request: ecs_20160314_models.PurchaseSavingPlanOfferingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.PurchaseSavingPlanOfferingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.committed_amount):
            query['CommittedAmount'] = request.committed_amount
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_family):
            query['InstanceFamily'] = request.instance_family
        if not UtilClient.is_unset(request.instance_family_set):
            query['InstanceFamilySet'] = request.instance_family_set
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.plan_type):
            query['PlanType'] = request.plan_type
        if not UtilClient.is_unset(request.purchase_method):
            query['PurchaseMethod'] = request.purchase_method
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseSavingPlanOffering',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.PurchaseSavingPlanOfferingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purchase_saving_plan_offering(
        self,
        request: ecs_20160314_models.PurchaseSavingPlanOfferingRequest,
    ) -> ecs_20160314_models.PurchaseSavingPlanOfferingResponse:
        runtime = util_models.RuntimeOptions()
        return self.purchase_saving_plan_offering_with_options(request, runtime)

    async def purchase_saving_plan_offering_async(
        self,
        request: ecs_20160314_models.PurchaseSavingPlanOfferingRequest,
    ) -> ecs_20160314_models.PurchaseSavingPlanOfferingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purchase_saving_plan_offering_with_options_async(request, runtime)

    def purchase_storage_capacity_unit_with_options(
        self,
        request: ecs_20160314_models.PurchaseStorageCapacityUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.PurchaseStorageCapacityUnitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.extend_params):
            query['ExtendParams'] = request.extend_params
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseStorageCapacityUnit',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.PurchaseStorageCapacityUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def purchase_storage_capacity_unit_with_options_async(
        self,
        request: ecs_20160314_models.PurchaseStorageCapacityUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.PurchaseStorageCapacityUnitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.extend_params):
            query['ExtendParams'] = request.extend_params
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseStorageCapacityUnit',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.PurchaseStorageCapacityUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purchase_storage_capacity_unit(
        self,
        request: ecs_20160314_models.PurchaseStorageCapacityUnitRequest,
    ) -> ecs_20160314_models.PurchaseStorageCapacityUnitResponse:
        runtime = util_models.RuntimeOptions()
        return self.purchase_storage_capacity_unit_with_options(request, runtime)

    async def purchase_storage_capacity_unit_async(
        self,
        request: ecs_20160314_models.PurchaseStorageCapacityUnitRequest,
    ) -> ecs_20160314_models.PurchaseStorageCapacityUnitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purchase_storage_capacity_unit_with_options_async(request, runtime)

    def query_eni_qos_group_by_eni_with_options(
        self,
        request: ecs_20160314_models.QueryEniQosGroupByEniRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.QueryEniQosGroupByEniResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
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
            action='QueryEniQosGroupByEni',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.QueryEniQosGroupByEniResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_eni_qos_group_by_eni_with_options_async(
        self,
        request: ecs_20160314_models.QueryEniQosGroupByEniRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.QueryEniQosGroupByEniResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
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
            action='QueryEniQosGroupByEni',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.QueryEniQosGroupByEniResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_eni_qos_group_by_eni(
        self,
        request: ecs_20160314_models.QueryEniQosGroupByEniRequest,
    ) -> ecs_20160314_models.QueryEniQosGroupByEniResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_eni_qos_group_by_eni_with_options(request, runtime)

    async def query_eni_qos_group_by_eni_async(
        self,
        request: ecs_20160314_models.QueryEniQosGroupByEniRequest,
    ) -> ecs_20160314_models.QueryEniQosGroupByEniResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_eni_qos_group_by_eni_with_options_async(request, runtime)

    def query_eni_qos_group_by_instance_with_options(
        self,
        request: ecs_20160314_models.QueryEniQosGroupByInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.QueryEniQosGroupByInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='QueryEniQosGroupByInstance',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.QueryEniQosGroupByInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_eni_qos_group_by_instance_with_options_async(
        self,
        request: ecs_20160314_models.QueryEniQosGroupByInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.QueryEniQosGroupByInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='QueryEniQosGroupByInstance',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.QueryEniQosGroupByInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_eni_qos_group_by_instance(
        self,
        request: ecs_20160314_models.QueryEniQosGroupByInstanceRequest,
    ) -> ecs_20160314_models.QueryEniQosGroupByInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_eni_qos_group_by_instance_with_options(request, runtime)

    async def query_eni_qos_group_by_instance_async(
        self,
        request: ecs_20160314_models.QueryEniQosGroupByInstanceRequest,
    ) -> ecs_20160314_models.QueryEniQosGroupByInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_eni_qos_group_by_instance_with_options_async(request, runtime)

    def re_add_migration_task_in_plan_with_options(
        self,
        request: ecs_20160314_models.ReAddMigrationTaskInPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ReAddMigrationTaskInPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.migration_plan_id):
            query['MigrationPlanId'] = request.migration_plan_id
        if not UtilClient.is_unset(request.migration_time):
            query['MigrationTime'] = request.migration_time
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
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
            action='ReAddMigrationTaskInPlan',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ReAddMigrationTaskInPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_add_migration_task_in_plan_with_options_async(
        self,
        request: ecs_20160314_models.ReAddMigrationTaskInPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ReAddMigrationTaskInPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.migration_plan_id):
            query['MigrationPlanId'] = request.migration_plan_id
        if not UtilClient.is_unset(request.migration_time):
            query['MigrationTime'] = request.migration_time
        if not UtilClient.is_unset(request.network_migration_type):
            query['NetworkMigrationType'] = request.network_migration_type
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
            action='ReAddMigrationTaskInPlan',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ReAddMigrationTaskInPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_add_migration_task_in_plan(
        self,
        request: ecs_20160314_models.ReAddMigrationTaskInPlanRequest,
    ) -> ecs_20160314_models.ReAddMigrationTaskInPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_add_migration_task_in_plan_with_options(request, runtime)

    async def re_add_migration_task_in_plan_async(
        self,
        request: ecs_20160314_models.ReAddMigrationTaskInPlanRequest,
    ) -> ecs_20160314_models.ReAddMigrationTaskInPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_add_migration_task_in_plan_with_options_async(request, runtime)

    def release_capacity_reservation_with_options(
        self,
        request: ecs_20160314_models.ReleaseCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ReleaseCapacityReservationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity_reservation_id):
            query['CapacityReservationId'] = request.capacity_reservation_id
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
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCapacityReservation',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ReleaseCapacityReservationResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_capacity_reservation_with_options_async(
        self,
        request: ecs_20160314_models.ReleaseCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ReleaseCapacityReservationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity_reservation_id):
            query['CapacityReservationId'] = request.capacity_reservation_id
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
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCapacityReservation',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ReleaseCapacityReservationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_capacity_reservation(
        self,
        request: ecs_20160314_models.ReleaseCapacityReservationRequest,
    ) -> ecs_20160314_models.ReleaseCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_capacity_reservation_with_options(request, runtime)

    async def release_capacity_reservation_async(
        self,
        request: ecs_20160314_models.ReleaseCapacityReservationRequest,
    ) -> ecs_20160314_models.ReleaseCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_capacity_reservation_with_options_async(request, runtime)

    def release_dedicated_host_with_options(
        self,
        request: ecs_20160314_models.ReleaseDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ReleaseDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
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
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseDedicatedHost',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ReleaseDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_dedicated_host_with_options_async(
        self,
        request: ecs_20160314_models.ReleaseDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ReleaseDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
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
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseDedicatedHost',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ReleaseDedicatedHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_dedicated_host(
        self,
        request: ecs_20160314_models.ReleaseDedicatedHostRequest,
    ) -> ecs_20160314_models.ReleaseDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_dedicated_host_with_options(request, runtime)

    async def release_dedicated_host_async(
        self,
        request: ecs_20160314_models.ReleaseDedicatedHostRequest,
    ) -> ecs_20160314_models.ReleaseDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_dedicated_host_with_options_async(request, runtime)

    def renew_dedicated_hosts_with_options(
        self,
        request: ecs_20160314_models.RenewDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.RenewDedicatedHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_host_ids):
            query['DedicatedHostIds'] = request.dedicated_host_ids
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
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
            action='RenewDedicatedHosts',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.RenewDedicatedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_dedicated_hosts_with_options_async(
        self,
        request: ecs_20160314_models.RenewDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.RenewDedicatedHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_host_ids):
            query['DedicatedHostIds'] = request.dedicated_host_ids
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
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
            action='RenewDedicatedHosts',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.RenewDedicatedHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_dedicated_hosts(
        self,
        request: ecs_20160314_models.RenewDedicatedHostsRequest,
    ) -> ecs_20160314_models.RenewDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_dedicated_hosts_with_options(request, runtime)

    async def renew_dedicated_hosts_async(
        self,
        request: ecs_20160314_models.RenewDedicatedHostsRequest,
    ) -> ecs_20160314_models.RenewDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_dedicated_hosts_with_options_async(request, runtime)

    def review_diagnostic_report_with_options(
        self,
        request: ecs_20160314_models.ReviewDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ReviewDiagnosticReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_system):
            query['SourceSystem'] = request.source_system
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReviewDiagnosticReport',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ReviewDiagnosticReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def review_diagnostic_report_with_options_async(
        self,
        request: ecs_20160314_models.ReviewDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.ReviewDiagnosticReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_system):
            query['SourceSystem'] = request.source_system
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReviewDiagnosticReport',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.ReviewDiagnosticReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def review_diagnostic_report(
        self,
        request: ecs_20160314_models.ReviewDiagnosticReportRequest,
    ) -> ecs_20160314_models.ReviewDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.review_diagnostic_report_with_options(request, runtime)

    async def review_diagnostic_report_async(
        self,
        request: ecs_20160314_models.ReviewDiagnosticReportRequest,
    ) -> ecs_20160314_models.ReviewDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.review_diagnostic_report_with_options_async(request, runtime)

    def run_instances_with_options(
        self,
        request: ecs_20160314_models.RunInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.RunInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.default_vpc):
            query['DefaultVpc'] = request.default_vpc
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_group_no):
            query['DeploymentSetGroupNo'] = request.deployment_set_group_no
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_names):
            query['HostNames'] = request.host_names
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not UtilClient.is_unset(request.http_put_response_hop_limit):
            query['HttpPutResponseHopLimit'] = request.http_put_response_hop_limit
        if not UtilClient.is_unset(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_options):
            query['ImageOptions'] = request.image_options
        if not UtilClient.is_unset(request.instance):
            query['Instance'] = request.instance
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.max_amount):
            query['MaxAmount'] = request.max_amount
        if not UtilClient.is_unset(request.min_amount):
            query['MinAmount'] = request.min_amount
        if not UtilClient.is_unset(request.network_interface):
            query['NetworkInterface'] = request.network_interface
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.node_controller_id):
            query['NodeControllerId'] = request.node_controller_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.recycle_bin_resource_id):
            query['RecycleBinResourceId'] = request.recycle_bin_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relation_order_id):
            query['RelationOrderId'] = request.relation_order_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.security_group_rule):
            query['SecurityGroupRule'] = request.security_group_rule
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.unique_suffix):
            query['UniqueSuffix'] = request.unique_suffix
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.hibernation_options):
            query['HibernationOptions'] = request.hibernation_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        if not UtilClient.is_unset(request.security_options):
            query['SecurityOptions'] = request.security_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.RunInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_instances_with_options_async(
        self,
        request: ecs_20160314_models.RunInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.RunInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.default_vpc):
            query['DefaultVpc'] = request.default_vpc
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_group_no):
            query['DeploymentSetGroupNo'] = request.deployment_set_group_no
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_names):
            query['HostNames'] = request.host_names
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not UtilClient.is_unset(request.http_put_response_hop_limit):
            query['HttpPutResponseHopLimit'] = request.http_put_response_hop_limit
        if not UtilClient.is_unset(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_options):
            query['ImageOptions'] = request.image_options
        if not UtilClient.is_unset(request.instance):
            query['Instance'] = request.instance
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.max_amount):
            query['MaxAmount'] = request.max_amount
        if not UtilClient.is_unset(request.min_amount):
            query['MinAmount'] = request.min_amount
        if not UtilClient.is_unset(request.network_interface):
            query['NetworkInterface'] = request.network_interface
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.node_controller_id):
            query['NodeControllerId'] = request.node_controller_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.recycle_bin_resource_id):
            query['RecycleBinResourceId'] = request.recycle_bin_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.relation_order_id):
            query['RelationOrderId'] = request.relation_order_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.security_group_rule):
            query['SecurityGroupRule'] = request.security_group_rule
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.unique_suffix):
            query['UniqueSuffix'] = request.unique_suffix
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.hibernation_options):
            query['HibernationOptions'] = request.hibernation_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        if not UtilClient.is_unset(request.security_options):
            query['SecurityOptions'] = request.security_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunInstances',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.RunInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_instances(
        self,
        request: ecs_20160314_models.RunInstancesRequest,
    ) -> ecs_20160314_models.RunInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_instances_with_options(request, runtime)

    async def run_instances_async(
        self,
        request: ecs_20160314_models.RunInstancesRequest,
    ) -> ecs_20160314_models.RunInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_instances_with_options_async(request, runtime)

    def set_instance_auto_release_time_with_options(
        self,
        request: ecs_20160314_models.SetInstanceAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.SetInstanceAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='SetInstanceAutoReleaseTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.SetInstanceAutoReleaseTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_instance_auto_release_time_with_options_async(
        self,
        request: ecs_20160314_models.SetInstanceAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.SetInstanceAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='SetInstanceAutoReleaseTime',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.SetInstanceAutoReleaseTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_instance_auto_release_time(
        self,
        request: ecs_20160314_models.SetInstanceAutoReleaseTimeRequest,
    ) -> ecs_20160314_models.SetInstanceAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_instance_auto_release_time_with_options(request, runtime)

    async def set_instance_auto_release_time_async(
        self,
        request: ecs_20160314_models.SetInstanceAutoReleaseTimeRequest,
    ) -> ecs_20160314_models.SetInstanceAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_instance_auto_release_time_with_options_async(request, runtime)

    def start_network_insights_analysis_with_options(
        self,
        request: ecs_20160314_models.StartNetworkInsightsAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.StartNetworkInsightsAnalysisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.network_insights_path_id):
            query['NetworkInsightsPathId'] = request.network_insights_path_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartNetworkInsightsAnalysis',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.StartNetworkInsightsAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_network_insights_analysis_with_options_async(
        self,
        request: ecs_20160314_models.StartNetworkInsightsAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.StartNetworkInsightsAnalysisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.network_insights_path_id):
            query['NetworkInsightsPathId'] = request.network_insights_path_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartNetworkInsightsAnalysis',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.StartNetworkInsightsAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_network_insights_analysis(
        self,
        request: ecs_20160314_models.StartNetworkInsightsAnalysisRequest,
    ) -> ecs_20160314_models.StartNetworkInsightsAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_network_insights_analysis_with_options(request, runtime)

    async def start_network_insights_analysis_async(
        self,
        request: ecs_20160314_models.StartNetworkInsightsAnalysisRequest,
    ) -> ecs_20160314_models.StartNetworkInsightsAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_network_insights_analysis_with_options_async(request, runtime)

    def update_service_settings_with_options(
        self,
        request: ecs_20160314_models.UpdateServiceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.UpdateServiceSettingsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.cloud_assistant_delivery_settings):
            query['CloudAssistantDeliverySettings'] = request.cloud_assistant_delivery_settings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceSettings',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.UpdateServiceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_settings_with_options_async(
        self,
        request: ecs_20160314_models.UpdateServiceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.UpdateServiceSettingsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.cloud_assistant_delivery_settings):
            query['CloudAssistantDeliverySettings'] = request.cloud_assistant_delivery_settings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceSettings',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.UpdateServiceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_settings(
        self,
        request: ecs_20160314_models.UpdateServiceSettingsRequest,
    ) -> ecs_20160314_models.UpdateServiceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_service_settings_with_options(request, runtime)

    async def update_service_settings_async(
        self,
        request: ecs_20160314_models.UpdateServiceSettingsRequest,
    ) -> ecs_20160314_models.UpdateServiceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_service_settings_with_options_async(request, runtime)

    def unmount_pedisk_with_options(
        self,
        request: ecs_20160314_models.UnmountPEDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.UnmountPEDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_system):
            query['SourceSystem'] = request.source_system
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='unmountPEDisk',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.UnmountPEDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def unmount_pedisk_with_options_async(
        self,
        request: ecs_20160314_models.UnmountPEDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20160314_models.UnmountPEDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_system):
            query['SourceSystem'] = request.source_system
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='unmountPEDisk',
            version='2016-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20160314_models.UnmountPEDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unmount_pedisk(
        self,
        request: ecs_20160314_models.UnmountPEDiskRequest,
    ) -> ecs_20160314_models.UnmountPEDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.unmount_pedisk_with_options(request, runtime)

    async def unmount_pedisk_async(
        self,
        request: ecs_20160314_models.UnmountPEDiskRequest,
    ) -> ecs_20160314_models.UnmountPEDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unmount_pedisk_with_options_async(request, runtime)
