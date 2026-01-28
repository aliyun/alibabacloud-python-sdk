# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ebs20210730 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('ebs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_disk_replica_pair_with_options(
        self,
        request: main_models.AddDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_disk_replica_pair_with_options_async(
        self,
        request: main_models.AddDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_disk_replica_pair(
        self,
        request: main_models.AddDiskReplicaPairRequest,
    ) -> main_models.AddDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return self.add_disk_replica_pair_with_options(request, runtime)

    async def add_disk_replica_pair_async(
        self,
        request: main_models.AddDiskReplicaPairRequest,
    ) -> main_models.AddDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return await self.add_disk_replica_pair_with_options_async(request, runtime)

    def apply_lens_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyLensServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ApplyLensService',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyLensServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_lens_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyLensServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ApplyLensService',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyLensServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_lens_service(self) -> main_models.ApplyLensServiceResponse:
        runtime = RuntimeOptions()
        return self.apply_lens_service_with_options(runtime)

    async def apply_lens_service_async(self) -> main_models.ApplyLensServiceResponse:
        runtime = RuntimeOptions()
        return await self.apply_lens_service_with_options_async(runtime)

    def bind_enterprise_snapshot_policy_with_options(
        self,
        request: main_models.BindEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindEnterpriseSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_targets):
            query['DiskTargets'] = request.disk_targets
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_enterprise_snapshot_policy_with_options_async(
        self,
        request: main_models.BindEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindEnterpriseSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_targets):
            query['DiskTargets'] = request.disk_targets
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_enterprise_snapshot_policy(
        self,
        request: main_models.BindEnterpriseSnapshotPolicyRequest,
    ) -> main_models.BindEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.bind_enterprise_snapshot_policy_with_options(request, runtime)

    async def bind_enterprise_snapshot_policy_async(
        self,
        request: main_models.BindEnterpriseSnapshotPolicyRequest,
    ) -> main_models.BindEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.bind_enterprise_snapshot_policy_with_options_async(request, runtime)

    def cancel_lens_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CancelLensServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CancelLensService',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelLensServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_lens_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CancelLensServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CancelLensService',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelLensServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_lens_service(self) -> main_models.CancelLensServiceResponse:
        runtime = RuntimeOptions()
        return self.cancel_lens_service_with_options(runtime)

    async def cancel_lens_service_async(self) -> main_models.CancelLensServiceResponse:
        runtime = RuntimeOptions()
        return await self.cancel_lens_service_with_options_async(runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def clear_pair_drill_with_options(
        self,
        request: main_models.ClearPairDrillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearPairDrillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drill_id):
            query['DrillId'] = request.drill_id
        if not DaraCore.is_null(request.pair_id):
            query['PairId'] = request.pair_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearPairDrill',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearPairDrillResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_pair_drill_with_options_async(
        self,
        request: main_models.ClearPairDrillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearPairDrillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drill_id):
            query['DrillId'] = request.drill_id
        if not DaraCore.is_null(request.pair_id):
            query['PairId'] = request.pair_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearPairDrill',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearPairDrillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_pair_drill(
        self,
        request: main_models.ClearPairDrillRequest,
    ) -> main_models.ClearPairDrillResponse:
        runtime = RuntimeOptions()
        return self.clear_pair_drill_with_options(request, runtime)

    async def clear_pair_drill_async(
        self,
        request: main_models.ClearPairDrillRequest,
    ) -> main_models.ClearPairDrillResponse:
        runtime = RuntimeOptions()
        return await self.clear_pair_drill_with_options_async(request, runtime)

    def clear_replica_group_drill_with_options(
        self,
        request: main_models.ClearReplicaGroupDrillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearReplicaGroupDrillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drill_id):
            query['DrillId'] = request.drill_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearReplicaGroupDrill',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearReplicaGroupDrillResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_replica_group_drill_with_options_async(
        self,
        request: main_models.ClearReplicaGroupDrillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearReplicaGroupDrillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drill_id):
            query['DrillId'] = request.drill_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearReplicaGroupDrill',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearReplicaGroupDrillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_replica_group_drill(
        self,
        request: main_models.ClearReplicaGroupDrillRequest,
    ) -> main_models.ClearReplicaGroupDrillResponse:
        runtime = RuntimeOptions()
        return self.clear_replica_group_drill_with_options(request, runtime)

    async def clear_replica_group_drill_async(
        self,
        request: main_models.ClearReplicaGroupDrillRequest,
    ) -> main_models.ClearReplicaGroupDrillResponse:
        runtime = RuntimeOptions()
        return await self.clear_replica_group_drill_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: main_models.CreateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_tags):
            query['AppTags'] = request.app_tags
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_send_enabled):
            query['ReportSendEnabled'] = request.report_send_enabled
        if not DaraCore.is_null(request.subscribe_period):
            query['SubscribePeriod'] = request.subscribe_period
        if not DaraCore.is_null(request.subscribe_status):
            query['SubscribeStatus'] = request.subscribe_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApp',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: main_models.CreateAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_tags):
            query['AppTags'] = request.app_tags
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_send_enabled):
            query['ReportSendEnabled'] = request.report_send_enabled
        if not DaraCore.is_null(request.subscribe_period):
            query['SubscribePeriod'] = request.subscribe_period
        if not DaraCore.is_null(request.subscribe_status):
            query['SubscribeStatus'] = request.subscribe_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApp',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: main_models.CreateAppRequest,
    ) -> main_models.CreateAppResponse:
        runtime = RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: main_models.CreateAppRequest,
    ) -> main_models.CreateAppResponse:
        runtime = RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_dedicated_block_storage_cluster_with_options(
        self,
        request: main_models.CreateDedicatedBlockStorageClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDedicatedBlockStorageClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.azone):
            query['Azone'] = request.azone
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not DaraCore.is_null(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDedicatedBlockStorageCluster',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDedicatedBlockStorageClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_block_storage_cluster_with_options_async(
        self,
        request: main_models.CreateDedicatedBlockStorageClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDedicatedBlockStorageClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.azone):
            query['Azone'] = request.azone
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not DaraCore.is_null(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDedicatedBlockStorageCluster',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDedicatedBlockStorageClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_block_storage_cluster(
        self,
        request: main_models.CreateDedicatedBlockStorageClusterRequest,
    ) -> main_models.CreateDedicatedBlockStorageClusterResponse:
        runtime = RuntimeOptions()
        return self.create_dedicated_block_storage_cluster_with_options(request, runtime)

    async def create_dedicated_block_storage_cluster_async(
        self,
        request: main_models.CreateDedicatedBlockStorageClusterRequest,
    ) -> main_models.CreateDedicatedBlockStorageClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_dedicated_block_storage_cluster_with_options_async(request, runtime)

    def create_disk_replica_group_with_options(
        self,
        request: main_models.CreateDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not DaraCore.is_null(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not DaraCore.is_null(request.enable_rtc):
            query['EnableRtc'] = request.enable_rtc
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.rpo):
            query['RPO'] = request.rpo
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_disk_replica_group_with_options_async(
        self,
        request: main_models.CreateDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not DaraCore.is_null(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not DaraCore.is_null(request.enable_rtc):
            query['EnableRtc'] = request.enable_rtc
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.rpo):
            query['RPO'] = request.rpo
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_disk_replica_group(
        self,
        request: main_models.CreateDiskReplicaGroupRequest,
    ) -> main_models.CreateDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return self.create_disk_replica_group_with_options(request, runtime)

    async def create_disk_replica_group_async(
        self,
        request: main_models.CreateDiskReplicaGroupRequest,
    ) -> main_models.CreateDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_disk_replica_group_with_options_async(request, runtime)

    def create_disk_replica_pair_with_options(
        self,
        request: main_models.CreateDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_disk_id):
            query['DestinationDiskId'] = request.destination_disk_id
        if not DaraCore.is_null(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not DaraCore.is_null(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.enable_rtc):
            query['EnableRtc'] = request.enable_rtc
        if not DaraCore.is_null(request.pair_name):
            query['PairName'] = request.pair_name
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.rpo):
            query['RPO'] = request.rpo
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_disk_replica_pair_with_options_async(
        self,
        request: main_models.CreateDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_disk_id):
            query['DestinationDiskId'] = request.destination_disk_id
        if not DaraCore.is_null(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not DaraCore.is_null(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.enable_rtc):
            query['EnableRtc'] = request.enable_rtc
        if not DaraCore.is_null(request.pair_name):
            query['PairName'] = request.pair_name
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.rpo):
            query['RPO'] = request.rpo
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_disk_replica_pair(
        self,
        request: main_models.CreateDiskReplicaPairRequest,
    ) -> main_models.CreateDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return self.create_disk_replica_pair_with_options(request, runtime)

    async def create_disk_replica_pair_async(
        self,
        request: main_models.CreateDiskReplicaPairRequest,
    ) -> main_models.CreateDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return await self.create_disk_replica_pair_with_options_async(request, runtime)

    def create_enterprise_snapshot_policy_with_options(
        self,
        tmp_req: main_models.CreateEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnterpriseSnapshotPolicyResponse:
        tmp_req.validate()
        request = main_models.CreateEnterpriseSnapshotPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cross_region_copy_info):
            request.cross_region_copy_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.cross_region_copy_info, 'CrossRegionCopyInfo', 'json')
        if not DaraCore.is_null(tmp_req.retain_rule):
            request.retain_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.retain_rule, 'RetainRule', 'json')
        if not DaraCore.is_null(tmp_req.schedule):
            request.schedule_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        if not DaraCore.is_null(tmp_req.special_retain_rules):
            request.special_retain_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.special_retain_rules, 'SpecialRetainRules', 'json')
        if not DaraCore.is_null(tmp_req.storage_rule):
            request.storage_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.storage_rule, 'StorageRule', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_region_copy_info_shrink):
            query['CrossRegionCopyInfo'] = request.cross_region_copy_info_shrink
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.retain_rule_shrink):
            query['RetainRule'] = request.retain_rule_shrink
        if not DaraCore.is_null(request.schedule_shrink):
            query['Schedule'] = request.schedule_shrink
        if not DaraCore.is_null(request.special_retain_rules_shrink):
            query['SpecialRetainRules'] = request.special_retain_rules_shrink
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.storage_rule_shrink):
            query['StorageRule'] = request.storage_rule_shrink
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_enterprise_snapshot_policy_with_options_async(
        self,
        tmp_req: main_models.CreateEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnterpriseSnapshotPolicyResponse:
        tmp_req.validate()
        request = main_models.CreateEnterpriseSnapshotPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cross_region_copy_info):
            request.cross_region_copy_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.cross_region_copy_info, 'CrossRegionCopyInfo', 'json')
        if not DaraCore.is_null(tmp_req.retain_rule):
            request.retain_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.retain_rule, 'RetainRule', 'json')
        if not DaraCore.is_null(tmp_req.schedule):
            request.schedule_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        if not DaraCore.is_null(tmp_req.special_retain_rules):
            request.special_retain_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.special_retain_rules, 'SpecialRetainRules', 'json')
        if not DaraCore.is_null(tmp_req.storage_rule):
            request.storage_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.storage_rule, 'StorageRule', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_region_copy_info_shrink):
            query['CrossRegionCopyInfo'] = request.cross_region_copy_info_shrink
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.retain_rule_shrink):
            query['RetainRule'] = request.retain_rule_shrink
        if not DaraCore.is_null(request.schedule_shrink):
            query['Schedule'] = request.schedule_shrink
        if not DaraCore.is_null(request.special_retain_rules_shrink):
            query['SpecialRetainRules'] = request.special_retain_rules_shrink
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.storage_rule_shrink):
            query['StorageRule'] = request.storage_rule_shrink
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_enterprise_snapshot_policy(
        self,
        request: main_models.CreateEnterpriseSnapshotPolicyRequest,
    ) -> main_models.CreateEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_enterprise_snapshot_policy_with_options(request, runtime)

    async def create_enterprise_snapshot_policy_async(
        self,
        request: main_models.CreateEnterpriseSnapshotPolicyRequest,
    ) -> main_models.CreateEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_enterprise_snapshot_policy_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: main_models.DeleteAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApp',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: main_models.DeleteAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApp',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: main_models.DeleteAppRequest,
    ) -> main_models.DeleteAppResponse:
        runtime = RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: main_models.DeleteAppRequest,
    ) -> main_models.DeleteAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_disk_replica_group_with_options(
        self,
        request: main_models.DeleteDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_disk_replica_group_with_options_async(
        self,
        request: main_models.DeleteDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_disk_replica_group(
        self,
        request: main_models.DeleteDiskReplicaGroupRequest,
    ) -> main_models.DeleteDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_disk_replica_group_with_options(request, runtime)

    async def delete_disk_replica_group_async(
        self,
        request: main_models.DeleteDiskReplicaGroupRequest,
    ) -> main_models.DeleteDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_disk_replica_group_with_options_async(request, runtime)

    def delete_disk_replica_pair_with_options(
        self,
        request: main_models.DeleteDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_disk_replica_pair_with_options_async(
        self,
        request: main_models.DeleteDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_disk_replica_pair(
        self,
        request: main_models.DeleteDiskReplicaPairRequest,
    ) -> main_models.DeleteDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return self.delete_disk_replica_pair_with_options(request, runtime)

    async def delete_disk_replica_pair_async(
        self,
        request: main_models.DeleteDiskReplicaPairRequest,
    ) -> main_models.DeleteDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return await self.delete_disk_replica_pair_with_options_async(request, runtime)

    def delete_enterprise_snapshot_policy_with_options(
        self,
        request: main_models.DeleteEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnterpriseSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_enterprise_snapshot_policy_with_options_async(
        self,
        request: main_models.DeleteEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnterpriseSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_enterprise_snapshot_policy(
        self,
        request: main_models.DeleteEnterpriseSnapshotPolicyRequest,
    ) -> main_models.DeleteEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_enterprise_snapshot_policy_with_options(request, runtime)

    async def delete_enterprise_snapshot_policy_async(
        self,
        request: main_models.DeleteEnterpriseSnapshotPolicyRequest,
    ) -> main_models.DeleteEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_enterprise_snapshot_policy_with_options_async(request, runtime)

    def describe_dedicated_block_storage_cluster_disks_with_options(
        self,
        request: main_models.DescribeDedicatedBlockStorageClusterDisksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDedicatedBlockStorageClusterDisks',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDedicatedBlockStorageClusterDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_block_storage_cluster_disks_with_options_async(
        self,
        request: main_models.DescribeDedicatedBlockStorageClusterDisksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDedicatedBlockStorageClusterDisks',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDedicatedBlockStorageClusterDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_block_storage_cluster_disks(
        self,
        request: main_models.DescribeDedicatedBlockStorageClusterDisksRequest,
    ) -> main_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        runtime = RuntimeOptions()
        return self.describe_dedicated_block_storage_cluster_disks_with_options(request, runtime)

    async def describe_dedicated_block_storage_cluster_disks_async(
        self,
        request: main_models.DescribeDedicatedBlockStorageClusterDisksRequest,
    ) -> main_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        runtime = RuntimeOptions()
        return await self.describe_dedicated_block_storage_cluster_disks_with_options_async(request, runtime)

    def describe_dedicated_block_storage_clusters_with_options(
        self,
        request: main_models.DescribeDedicatedBlockStorageClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDedicatedBlockStorageClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedicated_block_storage_cluster_id):
            query['DedicatedBlockStorageClusterId'] = request.dedicated_block_storage_cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.azone_id):
            body['AzoneId'] = request.azone_id
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDedicatedBlockStorageClusters',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDedicatedBlockStorageClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_block_storage_clusters_with_options_async(
        self,
        request: main_models.DescribeDedicatedBlockStorageClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDedicatedBlockStorageClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedicated_block_storage_cluster_id):
            query['DedicatedBlockStorageClusterId'] = request.dedicated_block_storage_cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.azone_id):
            body['AzoneId'] = request.azone_id
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDedicatedBlockStorageClusters',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDedicatedBlockStorageClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_block_storage_clusters(
        self,
        request: main_models.DescribeDedicatedBlockStorageClustersRequest,
    ) -> main_models.DescribeDedicatedBlockStorageClustersResponse:
        runtime = RuntimeOptions()
        return self.describe_dedicated_block_storage_clusters_with_options(request, runtime)

    async def describe_dedicated_block_storage_clusters_async(
        self,
        request: main_models.DescribeDedicatedBlockStorageClustersRequest,
    ) -> main_models.DescribeDedicatedBlockStorageClustersResponse:
        runtime = RuntimeOptions()
        return await self.describe_dedicated_block_storage_clusters_with_options_async(request, runtime)

    def describe_disk_events_with_options(
        self,
        request: main_models.DescribeDiskEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskEvents',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_events_with_options_async(
        self,
        request: main_models.DescribeDiskEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskEvents',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_events(
        self,
        request: main_models.DescribeDiskEventsRequest,
    ) -> main_models.DescribeDiskEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_disk_events_with_options(request, runtime)

    async def describe_disk_events_async(
        self,
        request: main_models.DescribeDiskEventsRequest,
    ) -> main_models.DescribeDiskEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_disk_events_with_options_async(request, runtime)

    def describe_disk_monitor_data_with_options(
        self,
        request: main_models.DescribeDiskMonitorDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskMonitorDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskMonitorData',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_monitor_data_with_options_async(
        self,
        request: main_models.DescribeDiskMonitorDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskMonitorDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskMonitorData',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_monitor_data(
        self,
        request: main_models.DescribeDiskMonitorDataRequest,
    ) -> main_models.DescribeDiskMonitorDataResponse:
        runtime = RuntimeOptions()
        return self.describe_disk_monitor_data_with_options(request, runtime)

    async def describe_disk_monitor_data_async(
        self,
        request: main_models.DescribeDiskMonitorDataRequest,
    ) -> main_models.DescribeDiskMonitorDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_disk_monitor_data_with_options_async(request, runtime)

    def describe_disk_monitor_data_list_with_options(
        self,
        request: main_models.DescribeDiskMonitorDataListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskMonitorDataListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskMonitorDataList',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskMonitorDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_monitor_data_list_with_options_async(
        self,
        request: main_models.DescribeDiskMonitorDataListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskMonitorDataListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskMonitorDataList',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskMonitorDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_monitor_data_list(
        self,
        request: main_models.DescribeDiskMonitorDataListRequest,
    ) -> main_models.DescribeDiskMonitorDataListResponse:
        runtime = RuntimeOptions()
        return self.describe_disk_monitor_data_list_with_options(request, runtime)

    async def describe_disk_monitor_data_list_async(
        self,
        request: main_models.DescribeDiskMonitorDataListRequest,
    ) -> main_models.DescribeDiskMonitorDataListResponse:
        runtime = RuntimeOptions()
        return await self.describe_disk_monitor_data_list_with_options_async(request, runtime)

    def describe_disk_replica_groups_with_options(
        self,
        request: main_models.DescribeDiskReplicaGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskReplicaGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.site):
            query['Site'] = request.site
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskReplicaGroups',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskReplicaGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_replica_groups_with_options_async(
        self,
        request: main_models.DescribeDiskReplicaGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskReplicaGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.site):
            query['Site'] = request.site
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskReplicaGroups',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskReplicaGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_replica_groups(
        self,
        request: main_models.DescribeDiskReplicaGroupsRequest,
    ) -> main_models.DescribeDiskReplicaGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_disk_replica_groups_with_options(request, runtime)

    async def describe_disk_replica_groups_async(
        self,
        request: main_models.DescribeDiskReplicaGroupsRequest,
    ) -> main_models.DescribeDiskReplicaGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_disk_replica_groups_with_options_async(request, runtime)

    def describe_disk_replica_pair_progress_with_options(
        self,
        request: main_models.DescribeDiskReplicaPairProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskReplicaPairProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskReplicaPairProgress',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskReplicaPairProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_replica_pair_progress_with_options_async(
        self,
        request: main_models.DescribeDiskReplicaPairProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskReplicaPairProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskReplicaPairProgress',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskReplicaPairProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_replica_pair_progress(
        self,
        request: main_models.DescribeDiskReplicaPairProgressRequest,
    ) -> main_models.DescribeDiskReplicaPairProgressResponse:
        runtime = RuntimeOptions()
        return self.describe_disk_replica_pair_progress_with_options(request, runtime)

    async def describe_disk_replica_pair_progress_async(
        self,
        request: main_models.DescribeDiskReplicaPairProgressRequest,
    ) -> main_models.DescribeDiskReplicaPairProgressResponse:
        runtime = RuntimeOptions()
        return await self.describe_disk_replica_pair_progress_with_options_async(request, runtime)

    def describe_disk_replica_pairs_with_options(
        self,
        request: main_models.DescribeDiskReplicaPairsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskReplicaPairsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pair_ids):
            query['PairIds'] = request.pair_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.site):
            query['Site'] = request.site
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskReplicaPairs',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskReplicaPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_replica_pairs_with_options_async(
        self,
        request: main_models.DescribeDiskReplicaPairsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskReplicaPairsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pair_ids):
            query['PairIds'] = request.pair_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.site):
            query['Site'] = request.site
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskReplicaPairs',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskReplicaPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_replica_pairs(
        self,
        request: main_models.DescribeDiskReplicaPairsRequest,
    ) -> main_models.DescribeDiskReplicaPairsResponse:
        runtime = RuntimeOptions()
        return self.describe_disk_replica_pairs_with_options(request, runtime)

    async def describe_disk_replica_pairs_async(
        self,
        request: main_models.DescribeDiskReplicaPairsRequest,
    ) -> main_models.DescribeDiskReplicaPairsResponse:
        runtime = RuntimeOptions()
        return await self.describe_disk_replica_pairs_with_options_async(request, runtime)

    def describe_enterprise_snapshot_policy_with_options(
        self,
        request: main_models.DescribeEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnterpriseSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_enterprise_snapshot_policy_with_options_async(
        self,
        request: main_models.DescribeEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnterpriseSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_enterprise_snapshot_policy(
        self,
        request: main_models.DescribeEnterpriseSnapshotPolicyRequest,
    ) -> main_models.DescribeEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_enterprise_snapshot_policy_with_options(request, runtime)

    async def describe_enterprise_snapshot_policy_async(
        self,
        request: main_models.DescribeEnterpriseSnapshotPolicyRequest,
    ) -> main_models.DescribeEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_enterprise_snapshot_policy_with_options_async(request, runtime)

    def describe_events_with_options(
        self,
        request: main_models.DescribeEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_level):
            query['EventLevel'] = request.event_level
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEvents',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: main_models.DescribeEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_level):
            query['EventLevel'] = request.event_level
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEvents',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events(
        self,
        request: main_models.DescribeEventsRequest,
    ) -> main_models.DescribeEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    async def describe_events_async(
        self,
        request: main_models.DescribeEventsRequest,
    ) -> main_models.DescribeEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_events_with_options_async(request, runtime)

    def describe_lens_monitor_disks_with_options(
        self,
        request: main_models.DescribeLensMonitorDisksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLensMonitorDisksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not DaraCore.is_null(request.disk_id_pattern):
            query['DiskIdPattern'] = request.disk_id_pattern
        if not DaraCore.is_null(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not DaraCore.is_null(request.lens_tags):
            query['LensTags'] = request.lens_tags
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLensMonitorDisks',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLensMonitorDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lens_monitor_disks_with_options_async(
        self,
        request: main_models.DescribeLensMonitorDisksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLensMonitorDisksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not DaraCore.is_null(request.disk_id_pattern):
            query['DiskIdPattern'] = request.disk_id_pattern
        if not DaraCore.is_null(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not DaraCore.is_null(request.lens_tags):
            query['LensTags'] = request.lens_tags
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLensMonitorDisks',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLensMonitorDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lens_monitor_disks(
        self,
        request: main_models.DescribeLensMonitorDisksRequest,
    ) -> main_models.DescribeLensMonitorDisksResponse:
        runtime = RuntimeOptions()
        return self.describe_lens_monitor_disks_with_options(request, runtime)

    async def describe_lens_monitor_disks_async(
        self,
        request: main_models.DescribeLensMonitorDisksRequest,
    ) -> main_models.DescribeLensMonitorDisksResponse:
        runtime = RuntimeOptions()
        return await self.describe_lens_monitor_disks_with_options_async(request, runtime)

    def describe_lens_service_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLensServiceStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeLensServiceStatus',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLensServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lens_service_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLensServiceStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeLensServiceStatus',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLensServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lens_service_status(self) -> main_models.DescribeLensServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_lens_service_status_with_options(runtime)

    async def describe_lens_service_status_async(self) -> main_models.DescribeLensServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_lens_service_status_with_options_async(runtime)

    def describe_metric_data_with_options(
        self,
        tmp_req: main_models.DescribeMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricDataResponse:
        tmp_req.validate()
        request = main_models.DescribeMetricDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group_by_labels):
            request.group_by_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_by_labels, 'GroupByLabels', 'simple')
        query = {}
        if not DaraCore.is_null(request.aggre_ops):
            query['AggreOps'] = request.aggre_ops
        if not DaraCore.is_null(request.aggre_over_line_ops):
            query['AggreOverLineOps'] = request.aggre_over_line_ops
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_by_labels_shrink):
            query['GroupByLabels'] = request.group_by_labels_shrink
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricData',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_data_with_options_async(
        self,
        tmp_req: main_models.DescribeMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricDataResponse:
        tmp_req.validate()
        request = main_models.DescribeMetricDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group_by_labels):
            request.group_by_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_by_labels, 'GroupByLabels', 'simple')
        query = {}
        if not DaraCore.is_null(request.aggre_ops):
            query['AggreOps'] = request.aggre_ops
        if not DaraCore.is_null(request.aggre_over_line_ops):
            query['AggreOverLineOps'] = request.aggre_over_line_ops
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_by_labels_shrink):
            query['GroupByLabels'] = request.group_by_labels_shrink
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricData',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_data(
        self,
        request: main_models.DescribeMetricDataRequest,
    ) -> main_models.DescribeMetricDataResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_data_with_options(request, runtime)

    async def describe_metric_data_async(
        self,
        request: main_models.DescribeMetricDataRequest,
    ) -> main_models.DescribeMetricDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_data_with_options_async(request, runtime)

    def describe_pair_drills_with_options(
        self,
        request: main_models.DescribePairDrillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePairDrillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drill_id):
            query['DrillId'] = request.drill_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pair_id):
            query['PairId'] = request.pair_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePairDrills',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePairDrillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pair_drills_with_options_async(
        self,
        request: main_models.DescribePairDrillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePairDrillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drill_id):
            query['DrillId'] = request.drill_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pair_id):
            query['PairId'] = request.pair_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePairDrills',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePairDrillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pair_drills(
        self,
        request: main_models.DescribePairDrillsRequest,
    ) -> main_models.DescribePairDrillsResponse:
        runtime = RuntimeOptions()
        return self.describe_pair_drills_with_options(request, runtime)

    async def describe_pair_drills_async(
        self,
        request: main_models.DescribePairDrillsRequest,
    ) -> main_models.DescribePairDrillsResponse:
        runtime = RuntimeOptions()
        return await self.describe_pair_drills_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_replica_group_drills_with_options(
        self,
        request: main_models.DescribeReplicaGroupDrillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeReplicaGroupDrillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drill_id):
            query['DrillId'] = request.drill_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeReplicaGroupDrills',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeReplicaGroupDrillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_replica_group_drills_with_options_async(
        self,
        request: main_models.DescribeReplicaGroupDrillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeReplicaGroupDrillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drill_id):
            query['DrillId'] = request.drill_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeReplicaGroupDrills',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeReplicaGroupDrillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_replica_group_drills(
        self,
        request: main_models.DescribeReplicaGroupDrillsRequest,
    ) -> main_models.DescribeReplicaGroupDrillsResponse:
        runtime = RuntimeOptions()
        return self.describe_replica_group_drills_with_options(request, runtime)

    async def describe_replica_group_drills_async(
        self,
        request: main_models.DescribeReplicaGroupDrillsRequest,
    ) -> main_models.DescribeReplicaGroupDrillsResponse:
        runtime = RuntimeOptions()
        return await self.describe_replica_group_drills_with_options_async(request, runtime)

    def describe_solution_instance_configuration_with_options(
        self,
        request: main_models.DescribeSolutionInstanceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSolutionInstanceConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.solution_id):
            query['SolutionId'] = request.solution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSolutionInstanceConfiguration',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSolutionInstanceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_solution_instance_configuration_with_options_async(
        self,
        request: main_models.DescribeSolutionInstanceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSolutionInstanceConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.solution_id):
            query['SolutionId'] = request.solution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSolutionInstanceConfiguration',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSolutionInstanceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_solution_instance_configuration(
        self,
        request: main_models.DescribeSolutionInstanceConfigurationRequest,
    ) -> main_models.DescribeSolutionInstanceConfigurationResponse:
        runtime = RuntimeOptions()
        return self.describe_solution_instance_configuration_with_options(request, runtime)

    async def describe_solution_instance_configuration_async(
        self,
        request: main_models.DescribeSolutionInstanceConfigurationRequest,
    ) -> main_models.DescribeSolutionInstanceConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.describe_solution_instance_configuration_with_options_async(request, runtime)

    def describe_user_tag_keys_with_options(
        self,
        request: main_models.DescribeUserTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserTagKeysResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag_filter_key):
            body['TagFilterKey'] = request.tag_filter_key
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserTagKeys',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_tag_keys_with_options_async(
        self,
        request: main_models.DescribeUserTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserTagKeysResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag_filter_key):
            body['TagFilterKey'] = request.tag_filter_key
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserTagKeys',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_tag_keys(
        self,
        request: main_models.DescribeUserTagKeysRequest,
    ) -> main_models.DescribeUserTagKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_user_tag_keys_with_options(request, runtime)

    async def describe_user_tag_keys_async(
        self,
        request: main_models.DescribeUserTagKeysRequest,
    ) -> main_models.DescribeUserTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_tag_keys_with_options_async(request, runtime)

    def describe_user_tag_values_with_options(
        self,
        request: main_models.DescribeUserTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserTagValuesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag_filter_value):
            body['TagFilterValue'] = request.tag_filter_value
        if not DaraCore.is_null(request.tag_key):
            body['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserTagValues',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_tag_values_with_options_async(
        self,
        request: main_models.DescribeUserTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserTagValuesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag_filter_value):
            body['TagFilterValue'] = request.tag_filter_value
        if not DaraCore.is_null(request.tag_key):
            body['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserTagValues',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_tag_values(
        self,
        request: main_models.DescribeUserTagValuesRequest,
    ) -> main_models.DescribeUserTagValuesResponse:
        runtime = RuntimeOptions()
        return self.describe_user_tag_values_with_options(request, runtime)

    async def describe_user_tag_values_async(
        self,
        request: main_models.DescribeUserTagValuesRequest,
    ) -> main_models.DescribeUserTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_tag_values_with_options_async(request, runtime)

    def failover_disk_replica_group_with_options(
        self,
        request: main_models.FailoverDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FailoverDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FailoverDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FailoverDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def failover_disk_replica_group_with_options_async(
        self,
        request: main_models.FailoverDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FailoverDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FailoverDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FailoverDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def failover_disk_replica_group(
        self,
        request: main_models.FailoverDiskReplicaGroupRequest,
    ) -> main_models.FailoverDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return self.failover_disk_replica_group_with_options(request, runtime)

    async def failover_disk_replica_group_async(
        self,
        request: main_models.FailoverDiskReplicaGroupRequest,
    ) -> main_models.FailoverDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return await self.failover_disk_replica_group_with_options_async(request, runtime)

    def failover_disk_replica_pair_with_options(
        self,
        request: main_models.FailoverDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FailoverDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FailoverDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FailoverDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def failover_disk_replica_pair_with_options_async(
        self,
        request: main_models.FailoverDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FailoverDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FailoverDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FailoverDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def failover_disk_replica_pair(
        self,
        request: main_models.FailoverDiskReplicaPairRequest,
    ) -> main_models.FailoverDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return self.failover_disk_replica_pair_with_options(request, runtime)

    async def failover_disk_replica_pair_async(
        self,
        request: main_models.FailoverDiskReplicaPairRequest,
    ) -> main_models.FailoverDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return await self.failover_disk_replica_pair_with_options_async(request, runtime)

    def get_report_with_options(
        self,
        request: main_models.GetReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_id):
            body['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetReport',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_report_with_options_async(
        self,
        request: main_models.GetReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_id):
            body['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetReport',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_report(
        self,
        request: main_models.GetReportRequest,
    ) -> main_models.GetReportResponse:
        runtime = RuntimeOptions()
        return self.get_report_with_options(request, runtime)

    async def get_report_async(
        self,
        request: main_models.GetReportRequest,
    ) -> main_models.GetReportResponse:
        runtime = RuntimeOptions()
        return await self.get_report_with_options_async(request, runtime)

    def list_replica_edge_supported_with_options(
        self,
        request: main_models.ListReplicaEdgeSupportedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListReplicaEdgeSupportedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.azone):
            query['Azone'] = request.azone
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReplicaEdgeSupported',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReplicaEdgeSupportedResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_replica_edge_supported_with_options_async(
        self,
        request: main_models.ListReplicaEdgeSupportedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListReplicaEdgeSupportedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.azone):
            query['Azone'] = request.azone
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReplicaEdgeSupported',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReplicaEdgeSupportedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_replica_edge_supported(
        self,
        request: main_models.ListReplicaEdgeSupportedRequest,
    ) -> main_models.ListReplicaEdgeSupportedResponse:
        runtime = RuntimeOptions()
        return self.list_replica_edge_supported_with_options(request, runtime)

    async def list_replica_edge_supported_async(
        self,
        request: main_models.ListReplicaEdgeSupportedRequest,
    ) -> main_models.ListReplicaEdgeSupportedResponse:
        runtime = RuntimeOptions()
        return await self.list_replica_edge_supported_with_options_async(request, runtime)

    def list_reports_with_options(
        self,
        request: main_models.ListReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListReports',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_reports_with_options_async(
        self,
        request: main_models.ListReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListReports',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_reports(
        self,
        request: main_models.ListReportsRequest,
    ) -> main_models.ListReportsResponse:
        runtime = RuntimeOptions()
        return self.list_reports_with_options(request, runtime)

    async def list_reports_async(
        self,
        request: main_models.ListReportsRequest,
    ) -> main_models.ListReportsResponse:
        runtime = RuntimeOptions()
        return await self.list_reports_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: main_models.ModifyAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_tags):
            query['AppTags'] = request.app_tags
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_send_enabled):
            query['ReportSendEnabled'] = request.report_send_enabled
        if not DaraCore.is_null(request.subscribe_period):
            query['SubscribePeriod'] = request.subscribe_period
        if not DaraCore.is_null(request.subscribe_status):
            query['SubscribeStatus'] = request.subscribe_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApp',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: main_models.ModifyAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_tags):
            query['AppTags'] = request.app_tags
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_send_enabled):
            query['ReportSendEnabled'] = request.report_send_enabled
        if not DaraCore.is_null(request.subscribe_period):
            query['SubscribePeriod'] = request.subscribe_period
        if not DaraCore.is_null(request.subscribe_status):
            query['SubscribeStatus'] = request.subscribe_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApp',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: main_models.ModifyAppRequest,
    ) -> main_models.ModifyAppResponse:
        runtime = RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: main_models.ModifyAppRequest,
    ) -> main_models.ModifyAppResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_dedicated_block_storage_cluster_attribute_with_options(
        self,
        request: main_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not DaraCore.is_null(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDedicatedBlockStorageClusterAttribute',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDedicatedBlockStorageClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_block_storage_cluster_attribute_with_options_async(
        self,
        request: main_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not DaraCore.is_null(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDedicatedBlockStorageClusterAttribute',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDedicatedBlockStorageClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_block_storage_cluster_attribute(
        self,
        request: main_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
    ) -> main_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_dedicated_block_storage_cluster_attribute_with_options(request, runtime)

    async def modify_dedicated_block_storage_cluster_attribute_async(
        self,
        request: main_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
    ) -> main_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dedicated_block_storage_cluster_attribute_with_options_async(request, runtime)

    def modify_disk_replica_group_with_options(
        self,
        request: main_models.ModifyDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_rtc):
            query['EnableRtc'] = request.enable_rtc
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.rpo):
            query['RPO'] = request.rpo
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_replica_group_with_options_async(
        self,
        request: main_models.ModifyDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_rtc):
            query['EnableRtc'] = request.enable_rtc
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.rpo):
            query['RPO'] = request.rpo
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_replica_group(
        self,
        request: main_models.ModifyDiskReplicaGroupRequest,
    ) -> main_models.ModifyDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_disk_replica_group_with_options(request, runtime)

    async def modify_disk_replica_group_async(
        self,
        request: main_models.ModifyDiskReplicaGroupRequest,
    ) -> main_models.ModifyDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_disk_replica_group_with_options_async(request, runtime)

    def modify_disk_replica_pair_with_options(
        self,
        request: main_models.ModifyDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_rtc):
            query['EnableRtc'] = request.enable_rtc
        if not DaraCore.is_null(request.pair_name):
            query['PairName'] = request.pair_name
        if not DaraCore.is_null(request.rpo):
            query['RPO'] = request.rpo
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_replica_pair_with_options_async(
        self,
        request: main_models.ModifyDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_rtc):
            query['EnableRtc'] = request.enable_rtc
        if not DaraCore.is_null(request.pair_name):
            query['PairName'] = request.pair_name
        if not DaraCore.is_null(request.rpo):
            query['RPO'] = request.rpo
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_replica_pair(
        self,
        request: main_models.ModifyDiskReplicaPairRequest,
    ) -> main_models.ModifyDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return self.modify_disk_replica_pair_with_options(request, runtime)

    async def modify_disk_replica_pair_async(
        self,
        request: main_models.ModifyDiskReplicaPairRequest,
    ) -> main_models.ModifyDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return await self.modify_disk_replica_pair_with_options_async(request, runtime)

    def query_dedicated_block_storage_cluster_disk_throughput_status_with_options(
        self,
        request: main_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.qos_request_id):
            body['QosRequestId'] = request.qos_request_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryDedicatedBlockStorageClusterDiskThroughputStatus',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dedicated_block_storage_cluster_disk_throughput_status_with_options_async(
        self,
        request: main_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.qos_request_id):
            body['QosRequestId'] = request.qos_request_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryDedicatedBlockStorageClusterDiskThroughputStatus',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dedicated_block_storage_cluster_disk_throughput_status(
        self,
        request: main_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusRequest,
    ) -> main_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse:
        runtime = RuntimeOptions()
        return self.query_dedicated_block_storage_cluster_disk_throughput_status_with_options(request, runtime)

    async def query_dedicated_block_storage_cluster_disk_throughput_status_async(
        self,
        request: main_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusRequest,
    ) -> main_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_dedicated_block_storage_cluster_disk_throughput_status_with_options_async(request, runtime)

    def query_dedicated_block_storage_cluster_inventory_data_with_options(
        self,
        request: main_models.QueryDedicatedBlockStorageClusterInventoryDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDedicatedBlockStorageClusterInventoryDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.dbsc_id):
            body['DbscId'] = request.dbsc_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryDedicatedBlockStorageClusterInventoryData',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDedicatedBlockStorageClusterInventoryDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dedicated_block_storage_cluster_inventory_data_with_options_async(
        self,
        request: main_models.QueryDedicatedBlockStorageClusterInventoryDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDedicatedBlockStorageClusterInventoryDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.dbsc_id):
            body['DbscId'] = request.dbsc_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryDedicatedBlockStorageClusterInventoryData',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDedicatedBlockStorageClusterInventoryDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dedicated_block_storage_cluster_inventory_data(
        self,
        request: main_models.QueryDedicatedBlockStorageClusterInventoryDataRequest,
    ) -> main_models.QueryDedicatedBlockStorageClusterInventoryDataResponse:
        runtime = RuntimeOptions()
        return self.query_dedicated_block_storage_cluster_inventory_data_with_options(request, runtime)

    async def query_dedicated_block_storage_cluster_inventory_data_async(
        self,
        request: main_models.QueryDedicatedBlockStorageClusterInventoryDataRequest,
    ) -> main_models.QueryDedicatedBlockStorageClusterInventoryDataResponse:
        runtime = RuntimeOptions()
        return await self.query_dedicated_block_storage_cluster_inventory_data_with_options_async(request, runtime)

    def remove_disk_replica_pair_with_options(
        self,
        request: main_models.RemoveDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_disk_replica_pair_with_options_async(
        self,
        request: main_models.RemoveDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_disk_replica_pair(
        self,
        request: main_models.RemoveDiskReplicaPairRequest,
    ) -> main_models.RemoveDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return self.remove_disk_replica_pair_with_options(request, runtime)

    async def remove_disk_replica_pair_async(
        self,
        request: main_models.RemoveDiskReplicaPairRequest,
    ) -> main_models.RemoveDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return await self.remove_disk_replica_pair_with_options_async(request, runtime)

    def reprotect_disk_replica_group_with_options(
        self,
        request: main_models.ReprotectDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReprotectDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not DaraCore.is_null(request.reverse_replicate):
            query['ReverseReplicate'] = request.reverse_replicate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReprotectDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReprotectDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def reprotect_disk_replica_group_with_options_async(
        self,
        request: main_models.ReprotectDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReprotectDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not DaraCore.is_null(request.reverse_replicate):
            query['ReverseReplicate'] = request.reverse_replicate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReprotectDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReprotectDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reprotect_disk_replica_group(
        self,
        request: main_models.ReprotectDiskReplicaGroupRequest,
    ) -> main_models.ReprotectDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return self.reprotect_disk_replica_group_with_options(request, runtime)

    async def reprotect_disk_replica_group_async(
        self,
        request: main_models.ReprotectDiskReplicaGroupRequest,
    ) -> main_models.ReprotectDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return await self.reprotect_disk_replica_group_with_options_async(request, runtime)

    def reprotect_disk_replica_pair_with_options(
        self,
        request: main_models.ReprotectDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReprotectDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        if not DaraCore.is_null(request.reverse_replicate):
            query['ReverseReplicate'] = request.reverse_replicate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReprotectDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReprotectDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def reprotect_disk_replica_pair_with_options_async(
        self,
        request: main_models.ReprotectDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReprotectDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        if not DaraCore.is_null(request.reverse_replicate):
            query['ReverseReplicate'] = request.reverse_replicate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReprotectDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReprotectDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reprotect_disk_replica_pair(
        self,
        request: main_models.ReprotectDiskReplicaPairRequest,
    ) -> main_models.ReprotectDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return self.reprotect_disk_replica_pair_with_options(request, runtime)

    async def reprotect_disk_replica_pair_async(
        self,
        request: main_models.ReprotectDiskReplicaPairRequest,
    ) -> main_models.ReprotectDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return await self.reprotect_disk_replica_pair_with_options_async(request, runtime)

    def set_dedicated_block_storage_cluster_disk_throughput_with_options(
        self,
        request: main_models.SetDedicatedBlockStorageClusterDiskThroughputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDedicatedBlockStorageClusterDiskThroughputResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.bps):
            body['Bps'] = request.bps
        if not DaraCore.is_null(request.disk_id):
            body['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetDedicatedBlockStorageClusterDiskThroughput',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDedicatedBlockStorageClusterDiskThroughputResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dedicated_block_storage_cluster_disk_throughput_with_options_async(
        self,
        request: main_models.SetDedicatedBlockStorageClusterDiskThroughputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDedicatedBlockStorageClusterDiskThroughputResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.bps):
            body['Bps'] = request.bps
        if not DaraCore.is_null(request.disk_id):
            body['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetDedicatedBlockStorageClusterDiskThroughput',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDedicatedBlockStorageClusterDiskThroughputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dedicated_block_storage_cluster_disk_throughput(
        self,
        request: main_models.SetDedicatedBlockStorageClusterDiskThroughputRequest,
    ) -> main_models.SetDedicatedBlockStorageClusterDiskThroughputResponse:
        runtime = RuntimeOptions()
        return self.set_dedicated_block_storage_cluster_disk_throughput_with_options(request, runtime)

    async def set_dedicated_block_storage_cluster_disk_throughput_async(
        self,
        request: main_models.SetDedicatedBlockStorageClusterDiskThroughputRequest,
    ) -> main_models.SetDedicatedBlockStorageClusterDiskThroughputResponse:
        runtime = RuntimeOptions()
        return await self.set_dedicated_block_storage_cluster_disk_throughput_with_options_async(request, runtime)

    def start_disk_replica_group_with_options(
        self,
        request: main_models.StartDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.one_shot):
            query['OneShot'] = request.one_shot
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_disk_replica_group_with_options_async(
        self,
        request: main_models.StartDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.one_shot):
            query['OneShot'] = request.one_shot
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_disk_replica_group(
        self,
        request: main_models.StartDiskReplicaGroupRequest,
    ) -> main_models.StartDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return self.start_disk_replica_group_with_options(request, runtime)

    async def start_disk_replica_group_async(
        self,
        request: main_models.StartDiskReplicaGroupRequest,
    ) -> main_models.StartDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return await self.start_disk_replica_group_with_options_async(request, runtime)

    def start_disk_replica_pair_with_options(
        self,
        request: main_models.StartDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.one_shot):
            query['OneShot'] = request.one_shot
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_disk_replica_pair_with_options_async(
        self,
        request: main_models.StartDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.one_shot):
            query['OneShot'] = request.one_shot
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_disk_replica_pair(
        self,
        request: main_models.StartDiskReplicaPairRequest,
    ) -> main_models.StartDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return self.start_disk_replica_pair_with_options(request, runtime)

    async def start_disk_replica_pair_async(
        self,
        request: main_models.StartDiskReplicaPairRequest,
    ) -> main_models.StartDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return await self.start_disk_replica_pair_with_options_async(request, runtime)

    def start_pair_drill_with_options(
        self,
        request: main_models.StartPairDrillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartPairDrillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.pair_id):
            query['PairId'] = request.pair_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartPairDrill',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartPairDrillResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_pair_drill_with_options_async(
        self,
        request: main_models.StartPairDrillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartPairDrillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.pair_id):
            query['PairId'] = request.pair_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartPairDrill',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartPairDrillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_pair_drill(
        self,
        request: main_models.StartPairDrillRequest,
    ) -> main_models.StartPairDrillResponse:
        runtime = RuntimeOptions()
        return self.start_pair_drill_with_options(request, runtime)

    async def start_pair_drill_async(
        self,
        request: main_models.StartPairDrillRequest,
    ) -> main_models.StartPairDrillResponse:
        runtime = RuntimeOptions()
        return await self.start_pair_drill_with_options_async(request, runtime)

    def start_replica_group_drill_with_options(
        self,
        request: main_models.StartReplicaGroupDrillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartReplicaGroupDrillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartReplicaGroupDrill',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartReplicaGroupDrillResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_replica_group_drill_with_options_async(
        self,
        request: main_models.StartReplicaGroupDrillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartReplicaGroupDrillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartReplicaGroupDrill',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartReplicaGroupDrillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_replica_group_drill(
        self,
        request: main_models.StartReplicaGroupDrillRequest,
    ) -> main_models.StartReplicaGroupDrillResponse:
        runtime = RuntimeOptions()
        return self.start_replica_group_drill_with_options(request, runtime)

    async def start_replica_group_drill_async(
        self,
        request: main_models.StartReplicaGroupDrillRequest,
    ) -> main_models.StartReplicaGroupDrillResponse:
        runtime = RuntimeOptions()
        return await self.start_replica_group_drill_with_options_async(request, runtime)

    def stop_disk_replica_group_with_options(
        self,
        request: main_models.StopDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_disk_replica_group_with_options_async(
        self,
        request: main_models.StopDiskReplicaGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDiskReplicaGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDiskReplicaGroup',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_disk_replica_group(
        self,
        request: main_models.StopDiskReplicaGroupRequest,
    ) -> main_models.StopDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return self.stop_disk_replica_group_with_options(request, runtime)

    async def stop_disk_replica_group_async(
        self,
        request: main_models.StopDiskReplicaGroupRequest,
    ) -> main_models.StopDiskReplicaGroupResponse:
        runtime = RuntimeOptions()
        return await self.stop_disk_replica_group_with_options_async(request, runtime)

    def stop_disk_replica_pair_with_options(
        self,
        request: main_models.StopDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_disk_replica_pair_with_options_async(
        self,
        request: main_models.StopDiskReplicaPairRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDiskReplicaPairResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDiskReplicaPair',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_disk_replica_pair(
        self,
        request: main_models.StopDiskReplicaPairRequest,
    ) -> main_models.StopDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return self.stop_disk_replica_pair_with_options(request, runtime)

    async def stop_disk_replica_pair_async(
        self,
        request: main_models.StopDiskReplicaPairRequest,
    ) -> main_models.StopDiskReplicaPairResponse:
        runtime = RuntimeOptions()
        return await self.stop_disk_replica_pair_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unbind_enterprise_snapshot_policy_with_options(
        self,
        request: main_models.UnbindEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindEnterpriseSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_targets):
            query['DiskTargets'] = request.disk_targets
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_enterprise_snapshot_policy_with_options_async(
        self,
        request: main_models.UnbindEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindEnterpriseSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disk_targets):
            query['DiskTargets'] = request.disk_targets
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_enterprise_snapshot_policy(
        self,
        request: main_models.UnbindEnterpriseSnapshotPolicyRequest,
    ) -> main_models.UnbindEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.unbind_enterprise_snapshot_policy_with_options(request, runtime)

    async def unbind_enterprise_snapshot_policy_async(
        self,
        request: main_models.UnbindEnterpriseSnapshotPolicyRequest,
    ) -> main_models.UnbindEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.unbind_enterprise_snapshot_policy_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_enterprise_snapshot_policy_with_options(
        self,
        tmp_req: main_models.UpdateEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnterpriseSnapshotPolicyResponse:
        tmp_req.validate()
        request = main_models.UpdateEnterpriseSnapshotPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cross_region_copy_info):
            request.cross_region_copy_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.cross_region_copy_info, 'CrossRegionCopyInfo', 'json')
        if not DaraCore.is_null(tmp_req.retain_rule):
            request.retain_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.retain_rule, 'RetainRule', 'json')
        if not DaraCore.is_null(tmp_req.schedule):
            request.schedule_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        if not DaraCore.is_null(tmp_req.special_retain_rules):
            request.special_retain_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.special_retain_rules, 'SpecialRetainRules', 'json')
        if not DaraCore.is_null(tmp_req.storage_rule):
            request.storage_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.storage_rule, 'StorageRule', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_region_copy_info_shrink):
            query['CrossRegionCopyInfo'] = request.cross_region_copy_info_shrink
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retain_rule_shrink):
            query['RetainRule'] = request.retain_rule_shrink
        if not DaraCore.is_null(request.schedule_shrink):
            query['Schedule'] = request.schedule_shrink
        if not DaraCore.is_null(request.special_retain_rules_shrink):
            query['SpecialRetainRules'] = request.special_retain_rules_shrink
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.storage_rule_shrink):
            query['StorageRule'] = request.storage_rule_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_enterprise_snapshot_policy_with_options_async(
        self,
        tmp_req: main_models.UpdateEnterpriseSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnterpriseSnapshotPolicyResponse:
        tmp_req.validate()
        request = main_models.UpdateEnterpriseSnapshotPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cross_region_copy_info):
            request.cross_region_copy_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.cross_region_copy_info, 'CrossRegionCopyInfo', 'json')
        if not DaraCore.is_null(tmp_req.retain_rule):
            request.retain_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.retain_rule, 'RetainRule', 'json')
        if not DaraCore.is_null(tmp_req.schedule):
            request.schedule_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        if not DaraCore.is_null(tmp_req.special_retain_rules):
            request.special_retain_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.special_retain_rules, 'SpecialRetainRules', 'json')
        if not DaraCore.is_null(tmp_req.storage_rule):
            request.storage_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.storage_rule, 'StorageRule', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_region_copy_info_shrink):
            query['CrossRegionCopyInfo'] = request.cross_region_copy_info_shrink
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retain_rule_shrink):
            query['RetainRule'] = request.retain_rule_shrink
        if not DaraCore.is_null(request.schedule_shrink):
            query['Schedule'] = request.schedule_shrink
        if not DaraCore.is_null(request.special_retain_rules_shrink):
            query['SpecialRetainRules'] = request.special_retain_rules_shrink
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.storage_rule_shrink):
            query['StorageRule'] = request.storage_rule_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnterpriseSnapshotPolicy',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_enterprise_snapshot_policy(
        self,
        request: main_models.UpdateEnterpriseSnapshotPolicyRequest,
    ) -> main_models.UpdateEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_enterprise_snapshot_policy_with_options(request, runtime)

    async def update_enterprise_snapshot_policy_async(
        self,
        request: main_models.UpdateEnterpriseSnapshotPolicyRequest,
    ) -> main_models.UpdateEnterpriseSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_enterprise_snapshot_policy_with_options_async(request, runtime)

    def update_solution_instance_attribute_with_options(
        self,
        request: main_models.UpdateSolutionInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSolutionInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.solution_instance_id):
            query['SolutionInstanceId'] = request.solution_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSolutionInstanceAttribute',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSolutionInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_solution_instance_attribute_with_options_async(
        self,
        request: main_models.UpdateSolutionInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSolutionInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.solution_instance_id):
            query['SolutionInstanceId'] = request.solution_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSolutionInstanceAttribute',
            version = '2021-07-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSolutionInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_solution_instance_attribute(
        self,
        request: main_models.UpdateSolutionInstanceAttributeRequest,
    ) -> main_models.UpdateSolutionInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_solution_instance_attribute_with_options(request, runtime)

    async def update_solution_instance_attribute_async(
        self,
        request: main_models.UpdateSolutionInstanceAttributeRequest,
    ) -> main_models.UpdateSolutionInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_solution_instance_attribute_with_options_async(request, runtime)
