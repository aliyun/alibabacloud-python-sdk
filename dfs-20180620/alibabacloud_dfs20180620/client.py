# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dfs20180620 import models as main_models
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
        self._endpoint = self.get_endpoint('dfs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_vsc_mount_point_with_options(
        self,
        tmp_req: main_models.AttachVscMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachVscMountPointResponse:
        tmp_req.validate()
        request = main_models.AttachVscMountPointShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not DaraCore.is_null(tmp_req.vsc_ids):
            request.vsc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.vsc_ids, 'VscIds', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not DaraCore.is_null(request.use_assume_role_chk_server_perm):
            query['UseAssumeRoleChkServerPerm'] = request.use_assume_role_chk_server_perm
        if not DaraCore.is_null(request.vsc_ids_shrink):
            query['VscIds'] = request.vsc_ids_shrink
        if not DaraCore.is_null(request.vsc_name):
            query['VscName'] = request.vsc_name
        if not DaraCore.is_null(request.vsc_type):
            query['VscType'] = request.vsc_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachVscMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachVscMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_vsc_mount_point_with_options_async(
        self,
        tmp_req: main_models.AttachVscMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachVscMountPointResponse:
        tmp_req.validate()
        request = main_models.AttachVscMountPointShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not DaraCore.is_null(tmp_req.vsc_ids):
            request.vsc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.vsc_ids, 'VscIds', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not DaraCore.is_null(request.use_assume_role_chk_server_perm):
            query['UseAssumeRoleChkServerPerm'] = request.use_assume_role_chk_server_perm
        if not DaraCore.is_null(request.vsc_ids_shrink):
            query['VscIds'] = request.vsc_ids_shrink
        if not DaraCore.is_null(request.vsc_name):
            query['VscName'] = request.vsc_name
        if not DaraCore.is_null(request.vsc_type):
            query['VscType'] = request.vsc_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachVscMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachVscMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_vsc_mount_point(
        self,
        request: main_models.AttachVscMountPointRequest,
    ) -> main_models.AttachVscMountPointResponse:
        runtime = RuntimeOptions()
        return self.attach_vsc_mount_point_with_options(request, runtime)

    async def attach_vsc_mount_point_async(
        self,
        request: main_models.AttachVscMountPointRequest,
    ) -> main_models.AttachVscMountPointResponse:
        runtime = RuntimeOptions()
        return await self.attach_vsc_mount_point_with_options_async(request, runtime)

    def attach_vsc_to_mount_points_with_options(
        self,
        tmp_req: main_models.AttachVscToMountPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachVscToMountPointsResponse:
        tmp_req.validate()
        request = main_models.AttachVscToMountPointsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attach_infos):
            request.attach_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.attach_infos, 'AttachInfos', 'json')
        query = {}
        if not DaraCore.is_null(request.attach_infos_shrink):
            query['AttachInfos'] = request.attach_infos_shrink
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.use_assume_role_chk_server_perm):
            query['UseAssumeRoleChkServerPerm'] = request.use_assume_role_chk_server_perm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachVscToMountPoints',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachVscToMountPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_vsc_to_mount_points_with_options_async(
        self,
        tmp_req: main_models.AttachVscToMountPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachVscToMountPointsResponse:
        tmp_req.validate()
        request = main_models.AttachVscToMountPointsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attach_infos):
            request.attach_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.attach_infos, 'AttachInfos', 'json')
        query = {}
        if not DaraCore.is_null(request.attach_infos_shrink):
            query['AttachInfos'] = request.attach_infos_shrink
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.use_assume_role_chk_server_perm):
            query['UseAssumeRoleChkServerPerm'] = request.use_assume_role_chk_server_perm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachVscToMountPoints',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachVscToMountPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_vsc_to_mount_points(
        self,
        request: main_models.AttachVscToMountPointsRequest,
    ) -> main_models.AttachVscToMountPointsResponse:
        runtime = RuntimeOptions()
        return self.attach_vsc_to_mount_points_with_options(request, runtime)

    async def attach_vsc_to_mount_points_async(
        self,
        request: main_models.AttachVscToMountPointsRequest,
    ) -> main_models.AttachVscToMountPointsResponse:
        runtime = RuntimeOptions()
        return await self.attach_vsc_to_mount_points_with_options_async(request, runtime)

    def bind_vsc_mount_point_alias_with_options(
        self,
        request: main_models.BindVscMountPointAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindVscMountPointAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_prefix):
            query['AliasPrefix'] = request.alias_prefix
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindVscMountPointAlias',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindVscMountPointAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_vsc_mount_point_alias_with_options_async(
        self,
        request: main_models.BindVscMountPointAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindVscMountPointAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_prefix):
            query['AliasPrefix'] = request.alias_prefix
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindVscMountPointAlias',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindVscMountPointAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_vsc_mount_point_alias(
        self,
        request: main_models.BindVscMountPointAliasRequest,
    ) -> main_models.BindVscMountPointAliasResponse:
        runtime = RuntimeOptions()
        return self.bind_vsc_mount_point_alias_with_options(request, runtime)

    async def bind_vsc_mount_point_alias_async(
        self,
        request: main_models.BindVscMountPointAliasRequest,
    ) -> main_models.BindVscMountPointAliasResponse:
        runtime = RuntimeOptions()
        return await self.bind_vsc_mount_point_alias_with_options_async(request, runtime)

    def create_access_group_with_options(
        self,
        request: main_models.CreateAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessGroup',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_group_with_options_async(
        self,
        request: main_models.CreateAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessGroup',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_group(
        self,
        request: main_models.CreateAccessGroupRequest,
    ) -> main_models.CreateAccessGroupResponse:
        runtime = RuntimeOptions()
        return self.create_access_group_with_options(request, runtime)

    async def create_access_group_async(
        self,
        request: main_models.CreateAccessGroupRequest,
    ) -> main_models.CreateAccessGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_access_group_with_options_async(request, runtime)

    def create_access_rule_with_options(
        self,
        request: main_models.CreateAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.network_segment):
            query['NetworkSegment'] = request.network_segment
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessRule',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_rule_with_options_async(
        self,
        request: main_models.CreateAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.network_segment):
            query['NetworkSegment'] = request.network_segment
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessRule',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_rule(
        self,
        request: main_models.CreateAccessRuleRequest,
    ) -> main_models.CreateAccessRuleResponse:
        runtime = RuntimeOptions()
        return self.create_access_rule_with_options(request, runtime)

    async def create_access_rule_async(
        self,
        request: main_models.CreateAccessRuleRequest,
    ) -> main_models.CreateAccessRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_access_rule_with_options_async(request, runtime)

    def create_file_system_with_options(
        self,
        request: main_models.CreateFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_redundancy_type):
            query['DataRedundancyType'] = request.data_redundancy_type
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_name):
            query['FileSystemName'] = request.file_system_name
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.partition_number):
            query['PartitionNumber'] = request.partition_number
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.provisioned_throughput_in_mi_bps):
            query['ProvisionedThroughputInMiBps'] = request.provisioned_throughput_in_mi_bps
        if not DaraCore.is_null(request.space_capacity):
            query['SpaceCapacity'] = request.space_capacity
        if not DaraCore.is_null(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.throughput_mode):
            query['ThroughputMode'] = request.throughput_mode
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileSystem',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_system_with_options_async(
        self,
        request: main_models.CreateFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_redundancy_type):
            query['DataRedundancyType'] = request.data_redundancy_type
        if not DaraCore.is_null(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_name):
            query['FileSystemName'] = request.file_system_name
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.partition_number):
            query['PartitionNumber'] = request.partition_number
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.provisioned_throughput_in_mi_bps):
            query['ProvisionedThroughputInMiBps'] = request.provisioned_throughput_in_mi_bps
        if not DaraCore.is_null(request.space_capacity):
            query['SpaceCapacity'] = request.space_capacity
        if not DaraCore.is_null(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.throughput_mode):
            query['ThroughputMode'] = request.throughput_mode
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileSystem',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_system(
        self,
        request: main_models.CreateFileSystemRequest,
    ) -> main_models.CreateFileSystemResponse:
        runtime = RuntimeOptions()
        return self.create_file_system_with_options(request, runtime)

    async def create_file_system_async(
        self,
        request: main_models.CreateFileSystemRequest,
    ) -> main_models.CreateFileSystemResponse:
        runtime = RuntimeOptions()
        return await self.create_file_system_with_options_async(request, runtime)

    def create_mount_point_with_options(
        self,
        request: main_models.CreateMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMountPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.use_performance_mode):
            query['UsePerformanceMode'] = request.use_performance_mode
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mount_point_with_options_async(
        self,
        request: main_models.CreateMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMountPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.use_performance_mode):
            query['UsePerformanceMode'] = request.use_performance_mode
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mount_point(
        self,
        request: main_models.CreateMountPointRequest,
    ) -> main_models.CreateMountPointResponse:
        runtime = RuntimeOptions()
        return self.create_mount_point_with_options(request, runtime)

    async def create_mount_point_async(
        self,
        request: main_models.CreateMountPointRequest,
    ) -> main_models.CreateMountPointResponse:
        runtime = RuntimeOptions()
        return await self.create_mount_point_with_options_async(request, runtime)

    def create_qos_policy_with_options(
        self,
        tmp_req: main_models.CreateQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQosPolicyResponse:
        tmp_req.validate()
        request = main_models.CreateQosPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.flow_ids):
            request.flow_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.flow_ids, 'FlowIds', 'json')
        if not DaraCore.is_null(tmp_req.req_tags):
            request.req_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.req_tags, 'ReqTags', 'json')
        if not DaraCore.is_null(tmp_req.zone_ids):
            request.zone_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.zone_ids, 'ZoneIds', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.federation_id):
            query['FederationId'] = request.federation_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.flow_ids_shrink):
            query['FlowIds'] = request.flow_ids_shrink
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.max_ioband_width):
            query['MaxIOBandWidth'] = request.max_ioband_width
        if not DaraCore.is_null(request.max_iops):
            query['MaxIOps'] = request.max_iops
        if not DaraCore.is_null(request.max_meta_qps):
            query['MaxMetaQps'] = request.max_meta_qps
        if not DaraCore.is_null(request.req_tags_shrink):
            query['ReqTags'] = request.req_tags_shrink
        if not DaraCore.is_null(request.zone_ids_shrink):
            query['ZoneIds'] = request.zone_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQosPolicy',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_qos_policy_with_options_async(
        self,
        tmp_req: main_models.CreateQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQosPolicyResponse:
        tmp_req.validate()
        request = main_models.CreateQosPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.flow_ids):
            request.flow_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.flow_ids, 'FlowIds', 'json')
        if not DaraCore.is_null(tmp_req.req_tags):
            request.req_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.req_tags, 'ReqTags', 'json')
        if not DaraCore.is_null(tmp_req.zone_ids):
            request.zone_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.zone_ids, 'ZoneIds', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.federation_id):
            query['FederationId'] = request.federation_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.flow_ids_shrink):
            query['FlowIds'] = request.flow_ids_shrink
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.max_ioband_width):
            query['MaxIOBandWidth'] = request.max_ioband_width
        if not DaraCore.is_null(request.max_iops):
            query['MaxIOps'] = request.max_iops
        if not DaraCore.is_null(request.max_meta_qps):
            query['MaxMetaQps'] = request.max_meta_qps
        if not DaraCore.is_null(request.req_tags_shrink):
            query['ReqTags'] = request.req_tags_shrink
        if not DaraCore.is_null(request.zone_ids_shrink):
            query['ZoneIds'] = request.zone_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQosPolicy',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_qos_policy(
        self,
        request: main_models.CreateQosPolicyRequest,
    ) -> main_models.CreateQosPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_qos_policy_with_options(request, runtime)

    async def create_qos_policy_async(
        self,
        request: main_models.CreateQosPolicyRequest,
    ) -> main_models.CreateQosPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_qos_policy_with_options_async(request, runtime)

    def create_user_groups_mapping_with_options(
        self,
        tmp_req: main_models.CreateUserGroupsMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserGroupsMappingResponse:
        tmp_req.validate()
        request = main_models.CreateUserGroupsMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group_names):
            request.group_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_names, 'GroupNames', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserGroupsMapping',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserGroupsMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_groups_mapping_with_options_async(
        self,
        tmp_req: main_models.CreateUserGroupsMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserGroupsMappingResponse:
        tmp_req.validate()
        request = main_models.CreateUserGroupsMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group_names):
            request.group_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_names, 'GroupNames', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserGroupsMapping',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserGroupsMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_groups_mapping(
        self,
        request: main_models.CreateUserGroupsMappingRequest,
    ) -> main_models.CreateUserGroupsMappingResponse:
        runtime = RuntimeOptions()
        return self.create_user_groups_mapping_with_options(request, runtime)

    async def create_user_groups_mapping_async(
        self,
        request: main_models.CreateUserGroupsMappingRequest,
    ) -> main_models.CreateUserGroupsMappingResponse:
        runtime = RuntimeOptions()
        return await self.create_user_groups_mapping_with_options_async(request, runtime)

    def create_vsc_mount_point_with_options(
        self,
        tmp_req: main_models.CreateVscMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVscMountPointResponse:
        tmp_req.validate()
        request = main_models.CreateVscMountPointShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVscMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVscMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vsc_mount_point_with_options_async(
        self,
        tmp_req: main_models.CreateVscMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVscMountPointResponse:
        tmp_req.validate()
        request = main_models.CreateVscMountPointShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVscMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVscMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vsc_mount_point(
        self,
        request: main_models.CreateVscMountPointRequest,
    ) -> main_models.CreateVscMountPointResponse:
        runtime = RuntimeOptions()
        return self.create_vsc_mount_point_with_options(request, runtime)

    async def create_vsc_mount_point_async(
        self,
        request: main_models.CreateVscMountPointRequest,
    ) -> main_models.CreateVscMountPointResponse:
        runtime = RuntimeOptions()
        return await self.create_vsc_mount_point_with_options_async(request, runtime)

    def delete_access_group_with_options(
        self,
        request: main_models.DeleteAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessGroup',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_group_with_options_async(
        self,
        request: main_models.DeleteAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessGroup',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_group(
        self,
        request: main_models.DeleteAccessGroupRequest,
    ) -> main_models.DeleteAccessGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_access_group_with_options(request, runtime)

    async def delete_access_group_async(
        self,
        request: main_models.DeleteAccessGroupRequest,
    ) -> main_models.DeleteAccessGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_group_with_options_async(request, runtime)

    def delete_access_rule_with_options(
        self,
        request: main_models.DeleteAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessRule',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_rule_with_options_async(
        self,
        request: main_models.DeleteAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessRule',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_rule(
        self,
        request: main_models.DeleteAccessRuleRequest,
    ) -> main_models.DeleteAccessRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_access_rule_with_options(request, runtime)

    async def delete_access_rule_async(
        self,
        request: main_models.DeleteAccessRuleRequest,
    ) -> main_models.DeleteAccessRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_rule_with_options_async(request, runtime)

    def delete_file_system_with_options(
        self,
        request: main_models.DeleteFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFileSystem',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_system_with_options_async(
        self,
        request: main_models.DeleteFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFileSystem',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file_system(
        self,
        request: main_models.DeleteFileSystemRequest,
    ) -> main_models.DeleteFileSystemResponse:
        runtime = RuntimeOptions()
        return self.delete_file_system_with_options(request, runtime)

    async def delete_file_system_async(
        self,
        request: main_models.DeleteFileSystemRequest,
    ) -> main_models.DeleteFileSystemResponse:
        runtime = RuntimeOptions()
        return await self.delete_file_system_with_options_async(request, runtime)

    def delete_mount_point_with_options(
        self,
        request: main_models.DeleteMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMountPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mount_point_with_options_async(
        self,
        request: main_models.DeleteMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMountPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mount_point(
        self,
        request: main_models.DeleteMountPointRequest,
    ) -> main_models.DeleteMountPointResponse:
        runtime = RuntimeOptions()
        return self.delete_mount_point_with_options(request, runtime)

    async def delete_mount_point_async(
        self,
        request: main_models.DeleteMountPointRequest,
    ) -> main_models.DeleteMountPointResponse:
        runtime = RuntimeOptions()
        return await self.delete_mount_point_with_options_async(request, runtime)

    def delete_qos_policy_with_options(
        self,
        request: main_models.DeleteQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federation_id):
            query['FederationId'] = request.federation_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQosPolicy',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_qos_policy_with_options_async(
        self,
        request: main_models.DeleteQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federation_id):
            query['FederationId'] = request.federation_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQosPolicy',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_qos_policy(
        self,
        request: main_models.DeleteQosPolicyRequest,
    ) -> main_models.DeleteQosPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_qos_policy_with_options(request, runtime)

    async def delete_qos_policy_async(
        self,
        request: main_models.DeleteQosPolicyRequest,
    ) -> main_models.DeleteQosPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_qos_policy_with_options_async(request, runtime)

    def delete_user_groups_mapping_with_options(
        self,
        tmp_req: main_models.DeleteUserGroupsMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupsMappingResponse:
        tmp_req.validate()
        request = main_models.DeleteUserGroupsMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group_names):
            request.group_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_names, 'GroupNames', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroupsMapping',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserGroupsMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_groups_mapping_with_options_async(
        self,
        tmp_req: main_models.DeleteUserGroupsMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupsMappingResponse:
        tmp_req.validate()
        request = main_models.DeleteUserGroupsMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.group_names):
            request.group_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_names, 'GroupNames', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroupsMapping',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserGroupsMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_groups_mapping(
        self,
        request: main_models.DeleteUserGroupsMappingRequest,
    ) -> main_models.DeleteUserGroupsMappingResponse:
        runtime = RuntimeOptions()
        return self.delete_user_groups_mapping_with_options(request, runtime)

    async def delete_user_groups_mapping_async(
        self,
        request: main_models.DeleteUserGroupsMappingRequest,
    ) -> main_models.DeleteUserGroupsMappingResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_groups_mapping_with_options_async(request, runtime)

    def delete_vsc_mount_point_with_options(
        self,
        request: main_models.DeleteVscMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVscMountPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVscMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVscMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vsc_mount_point_with_options_async(
        self,
        request: main_models.DeleteVscMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVscMountPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVscMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVscMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vsc_mount_point(
        self,
        request: main_models.DeleteVscMountPointRequest,
    ) -> main_models.DeleteVscMountPointResponse:
        runtime = RuntimeOptions()
        return self.delete_vsc_mount_point_with_options(request, runtime)

    async def delete_vsc_mount_point_async(
        self,
        request: main_models.DeleteVscMountPointRequest,
    ) -> main_models.DeleteVscMountPointResponse:
        runtime = RuntimeOptions()
        return await self.delete_vsc_mount_point_with_options_async(request, runtime)

    def describe_mount_points_vsc_attach_info_with_options(
        self,
        tmp_req: main_models.DescribeMountPointsVscAttachInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMountPointsVscAttachInfoResponse:
        tmp_req.validate()
        request = main_models.DescribeMountPointsVscAttachInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query_infos):
            request.query_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_infos, 'QueryInfos', 'json')
        query = {}
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.query_infos_shrink):
            query['QueryInfos'] = request.query_infos_shrink
        if not DaraCore.is_null(request.use_assume_role_chk_server_perm):
            query['UseAssumeRoleChkServerPerm'] = request.use_assume_role_chk_server_perm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMountPointsVscAttachInfo',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMountPointsVscAttachInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mount_points_vsc_attach_info_with_options_async(
        self,
        tmp_req: main_models.DescribeMountPointsVscAttachInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMountPointsVscAttachInfoResponse:
        tmp_req.validate()
        request = main_models.DescribeMountPointsVscAttachInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query_infos):
            request.query_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_infos, 'QueryInfos', 'json')
        query = {}
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.query_infos_shrink):
            query['QueryInfos'] = request.query_infos_shrink
        if not DaraCore.is_null(request.use_assume_role_chk_server_perm):
            query['UseAssumeRoleChkServerPerm'] = request.use_assume_role_chk_server_perm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMountPointsVscAttachInfo',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMountPointsVscAttachInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mount_points_vsc_attach_info(
        self,
        request: main_models.DescribeMountPointsVscAttachInfoRequest,
    ) -> main_models.DescribeMountPointsVscAttachInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_mount_points_vsc_attach_info_with_options(request, runtime)

    async def describe_mount_points_vsc_attach_info_async(
        self,
        request: main_models.DescribeMountPointsVscAttachInfoRequest,
    ) -> main_models.DescribeMountPointsVscAttachInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_mount_points_vsc_attach_info_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2018-06-20',
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
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2018-06-20',
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

    def describe_vsc_mount_points_with_options(
        self,
        request: main_models.DescribeVscMountPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVscMountPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.vsc_id):
            query['VscId'] = request.vsc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVscMountPoints',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVscMountPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vsc_mount_points_with_options_async(
        self,
        request: main_models.DescribeVscMountPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVscMountPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.vsc_id):
            query['VscId'] = request.vsc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVscMountPoints',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVscMountPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vsc_mount_points(
        self,
        request: main_models.DescribeVscMountPointsRequest,
    ) -> main_models.DescribeVscMountPointsResponse:
        runtime = RuntimeOptions()
        return self.describe_vsc_mount_points_with_options(request, runtime)

    async def describe_vsc_mount_points_async(
        self,
        request: main_models.DescribeVscMountPointsRequest,
    ) -> main_models.DescribeVscMountPointsResponse:
        runtime = RuntimeOptions()
        return await self.describe_vsc_mount_points_with_options_async(request, runtime)

    def detach_vsc_from_mount_points_with_options(
        self,
        tmp_req: main_models.DetachVscFromMountPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachVscFromMountPointsResponse:
        tmp_req.validate()
        request = main_models.DetachVscFromMountPointsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detach_infos):
            request.detach_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.detach_infos, 'DetachInfos', 'json')
        query = {}
        if not DaraCore.is_null(request.detach_infos_shrink):
            query['DetachInfos'] = request.detach_infos_shrink
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.use_assume_role_chk_server_perm):
            query['UseAssumeRoleChkServerPerm'] = request.use_assume_role_chk_server_perm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachVscFromMountPoints',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachVscFromMountPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_vsc_from_mount_points_with_options_async(
        self,
        tmp_req: main_models.DetachVscFromMountPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachVscFromMountPointsResponse:
        tmp_req.validate()
        request = main_models.DetachVscFromMountPointsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detach_infos):
            request.detach_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.detach_infos, 'DetachInfos', 'json')
        query = {}
        if not DaraCore.is_null(request.detach_infos_shrink):
            query['DetachInfos'] = request.detach_infos_shrink
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.use_assume_role_chk_server_perm):
            query['UseAssumeRoleChkServerPerm'] = request.use_assume_role_chk_server_perm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachVscFromMountPoints',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachVscFromMountPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_vsc_from_mount_points(
        self,
        request: main_models.DetachVscFromMountPointsRequest,
    ) -> main_models.DetachVscFromMountPointsResponse:
        runtime = RuntimeOptions()
        return self.detach_vsc_from_mount_points_with_options(request, runtime)

    async def detach_vsc_from_mount_points_async(
        self,
        request: main_models.DetachVscFromMountPointsRequest,
    ) -> main_models.DetachVscFromMountPointsResponse:
        runtime = RuntimeOptions()
        return await self.detach_vsc_from_mount_points_with_options_async(request, runtime)

    def detach_vsc_mount_point_with_options(
        self,
        tmp_req: main_models.DetachVscMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachVscMountPointResponse:
        tmp_req.validate()
        request = main_models.DetachVscMountPointShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not DaraCore.is_null(tmp_req.vsc_ids):
            request.vsc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.vsc_ids, 'VscIds', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not DaraCore.is_null(request.use_assume_role_chk_server_perm):
            query['UseAssumeRoleChkServerPerm'] = request.use_assume_role_chk_server_perm
        if not DaraCore.is_null(request.vsc_ids_shrink):
            query['VscIds'] = request.vsc_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachVscMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachVscMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_vsc_mount_point_with_options_async(
        self,
        tmp_req: main_models.DetachVscMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachVscMountPointResponse:
        tmp_req.validate()
        request = main_models.DetachVscMountPointShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not DaraCore.is_null(tmp_req.vsc_ids):
            request.vsc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.vsc_ids, 'VscIds', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not DaraCore.is_null(request.use_assume_role_chk_server_perm):
            query['UseAssumeRoleChkServerPerm'] = request.use_assume_role_chk_server_perm
        if not DaraCore.is_null(request.vsc_ids_shrink):
            query['VscIds'] = request.vsc_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachVscMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachVscMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_vsc_mount_point(
        self,
        request: main_models.DetachVscMountPointRequest,
    ) -> main_models.DetachVscMountPointResponse:
        runtime = RuntimeOptions()
        return self.detach_vsc_mount_point_with_options(request, runtime)

    async def detach_vsc_mount_point_async(
        self,
        request: main_models.DetachVscMountPointRequest,
    ) -> main_models.DetachVscMountPointResponse:
        runtime = RuntimeOptions()
        return await self.detach_vsc_mount_point_with_options_async(request, runtime)

    def get_access_group_with_options(
        self,
        request: main_models.GetAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessGroup',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_group_with_options_async(
        self,
        request: main_models.GetAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessGroup',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_group(
        self,
        request: main_models.GetAccessGroupRequest,
    ) -> main_models.GetAccessGroupResponse:
        runtime = RuntimeOptions()
        return self.get_access_group_with_options(request, runtime)

    async def get_access_group_async(
        self,
        request: main_models.GetAccessGroupRequest,
    ) -> main_models.GetAccessGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_access_group_with_options_async(request, runtime)

    def get_access_rule_with_options(
        self,
        request: main_models.GetAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessRule',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_rule_with_options_async(
        self,
        request: main_models.GetAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessRule',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_rule(
        self,
        request: main_models.GetAccessRuleRequest,
    ) -> main_models.GetAccessRuleResponse:
        runtime = RuntimeOptions()
        return self.get_access_rule_with_options(request, runtime)

    async def get_access_rule_async(
        self,
        request: main_models.GetAccessRuleRequest,
    ) -> main_models.GetAccessRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_access_rule_with_options_async(request, runtime)

    def get_file_system_with_options(
        self,
        request: main_models.GetFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFileSystem',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_system_with_options_async(
        self,
        request: main_models.GetFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFileSystem',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_system(
        self,
        request: main_models.GetFileSystemRequest,
    ) -> main_models.GetFileSystemResponse:
        runtime = RuntimeOptions()
        return self.get_file_system_with_options(request, runtime)

    async def get_file_system_async(
        self,
        request: main_models.GetFileSystemRequest,
    ) -> main_models.GetFileSystemResponse:
        runtime = RuntimeOptions()
        return await self.get_file_system_with_options_async(request, runtime)

    def get_mount_point_with_options(
        self,
        request: main_models.GetMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMountPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mount_point_with_options_async(
        self,
        request: main_models.GetMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMountPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mount_point(
        self,
        request: main_models.GetMountPointRequest,
    ) -> main_models.GetMountPointResponse:
        runtime = RuntimeOptions()
        return self.get_mount_point_with_options(request, runtime)

    async def get_mount_point_async(
        self,
        request: main_models.GetMountPointRequest,
    ) -> main_models.GetMountPointResponse:
        runtime = RuntimeOptions()
        return await self.get_mount_point_with_options_async(request, runtime)

    def get_region_with_options(
        self,
        request: main_models.GetRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRegion',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_region_with_options_async(
        self,
        request: main_models.GetRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRegion',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_region(
        self,
        request: main_models.GetRegionRequest,
    ) -> main_models.GetRegionResponse:
        runtime = RuntimeOptions()
        return self.get_region_with_options(request, runtime)

    async def get_region_async(
        self,
        request: main_models.GetRegionRequest,
    ) -> main_models.GetRegionResponse:
        runtime = RuntimeOptions()
        return await self.get_region_with_options_async(request, runtime)

    def list_access_groups_with_options(
        self,
        request: main_models.ListAccessGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessGroups',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_groups_with_options_async(
        self,
        request: main_models.ListAccessGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessGroups',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_groups(
        self,
        request: main_models.ListAccessGroupsRequest,
    ) -> main_models.ListAccessGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_access_groups_with_options(request, runtime)

    async def list_access_groups_async(
        self,
        request: main_models.ListAccessGroupsRequest,
    ) -> main_models.ListAccessGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_access_groups_with_options_async(request, runtime)

    def list_access_rules_with_options(
        self,
        request: main_models.ListAccessRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessRules',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_rules_with_options_async(
        self,
        request: main_models.ListAccessRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessRules',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_rules(
        self,
        request: main_models.ListAccessRulesRequest,
    ) -> main_models.ListAccessRulesResponse:
        runtime = RuntimeOptions()
        return self.list_access_rules_with_options(request, runtime)

    async def list_access_rules_async(
        self,
        request: main_models.ListAccessRulesRequest,
    ) -> main_models.ListAccessRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_access_rules_with_options_async(request, runtime)

    def list_federations_with_options(
        self,
        request: main_models.ListFederationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFederationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federation_id):
            query['FederationId'] = request.federation_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFederations',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFederationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_federations_with_options_async(
        self,
        request: main_models.ListFederationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFederationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federation_id):
            query['FederationId'] = request.federation_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFederations',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFederationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_federations(
        self,
        request: main_models.ListFederationsRequest,
    ) -> main_models.ListFederationsResponse:
        runtime = RuntimeOptions()
        return self.list_federations_with_options(request, runtime)

    async def list_federations_async(
        self,
        request: main_models.ListFederationsRequest,
    ) -> main_models.ListFederationsResponse:
        runtime = RuntimeOptions()
        return await self.list_federations_with_options_async(request, runtime)

    def list_file_systems_with_options(
        self,
        request: main_models.ListFileSystemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFileSystemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFileSystems',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_file_systems_with_options_async(
        self,
        request: main_models.ListFileSystemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFileSystemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFileSystems',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_file_systems(
        self,
        request: main_models.ListFileSystemsRequest,
    ) -> main_models.ListFileSystemsResponse:
        runtime = RuntimeOptions()
        return self.list_file_systems_with_options(request, runtime)

    async def list_file_systems_async(
        self,
        request: main_models.ListFileSystemsRequest,
    ) -> main_models.ListFileSystemsResponse:
        runtime = RuntimeOptions()
        return await self.list_file_systems_with_options_async(request, runtime)

    def list_mount_points_with_options(
        self,
        request: main_models.ListMountPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMountPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMountPoints',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMountPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mount_points_with_options_async(
        self,
        request: main_models.ListMountPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMountPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMountPoints',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMountPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mount_points(
        self,
        request: main_models.ListMountPointsRequest,
    ) -> main_models.ListMountPointsResponse:
        runtime = RuntimeOptions()
        return self.list_mount_points_with_options(request, runtime)

    async def list_mount_points_async(
        self,
        request: main_models.ListMountPointsRequest,
    ) -> main_models.ListMountPointsResponse:
        runtime = RuntimeOptions()
        return await self.list_mount_points_with_options_async(request, runtime)

    def list_qos_policies_with_options(
        self,
        request: main_models.ListQosPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQosPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federation_id):
            query['FederationId'] = request.federation_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQosPolicies',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQosPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_qos_policies_with_options_async(
        self,
        request: main_models.ListQosPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQosPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federation_id):
            query['FederationId'] = request.federation_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQosPolicies',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQosPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_qos_policies(
        self,
        request: main_models.ListQosPoliciesRequest,
    ) -> main_models.ListQosPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_qos_policies_with_options(request, runtime)

    async def list_qos_policies_async(
        self,
        request: main_models.ListQosPoliciesRequest,
    ) -> main_models.ListQosPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_qos_policies_with_options_async(request, runtime)

    def list_user_groups_mappings_with_options(
        self,
        request: main_models.ListUserGroupsMappingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsMappingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filesystem_id):
            query['FilesystemId'] = request.filesystem_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroupsMappings',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsMappingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_mappings_with_options_async(
        self,
        request: main_models.ListUserGroupsMappingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsMappingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filesystem_id):
            query['FilesystemId'] = request.filesystem_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroupsMappings',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsMappingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups_mappings(
        self,
        request: main_models.ListUserGroupsMappingsRequest,
    ) -> main_models.ListUserGroupsMappingsResponse:
        runtime = RuntimeOptions()
        return self.list_user_groups_mappings_with_options(request, runtime)

    async def list_user_groups_mappings_async(
        self,
        request: main_models.ListUserGroupsMappingsRequest,
    ) -> main_models.ListUserGroupsMappingsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_groups_mappings_with_options_async(request, runtime)

    def modify_access_group_with_options(
        self,
        request: main_models.ModifyAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccessGroup',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_group_with_options_async(
        self,
        request: main_models.ModifyAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccessGroup',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_group(
        self,
        request: main_models.ModifyAccessGroupRequest,
    ) -> main_models.ModifyAccessGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_access_group_with_options(request, runtime)

    async def modify_access_group_async(
        self,
        request: main_models.ModifyAccessGroupRequest,
    ) -> main_models.ModifyAccessGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_access_group_with_options_async(request, runtime)

    def modify_access_rule_with_options(
        self,
        request: main_models.ModifyAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccessRule',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_rule_with_options_async(
        self,
        request: main_models.ModifyAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccessRule',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_rule(
        self,
        request: main_models.ModifyAccessRuleRequest,
    ) -> main_models.ModifyAccessRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_access_rule_with_options(request, runtime)

    async def modify_access_rule_async(
        self,
        request: main_models.ModifyAccessRuleRequest,
    ) -> main_models.ModifyAccessRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_access_rule_with_options_async(request, runtime)

    def modify_file_system_with_options(
        self,
        request: main_models.ModifyFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_name):
            query['FileSystemName'] = request.file_system_name
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.provisioned_throughput_in_mi_bps):
            query['ProvisionedThroughputInMiBps'] = request.provisioned_throughput_in_mi_bps
        if not DaraCore.is_null(request.space_capacity):
            query['SpaceCapacity'] = request.space_capacity
        if not DaraCore.is_null(request.throughput_mode):
            query['ThroughputMode'] = request.throughput_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFileSystem',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_file_system_with_options_async(
        self,
        request: main_models.ModifyFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_name):
            query['FileSystemName'] = request.file_system_name
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.provisioned_throughput_in_mi_bps):
            query['ProvisionedThroughputInMiBps'] = request.provisioned_throughput_in_mi_bps
        if not DaraCore.is_null(request.space_capacity):
            query['SpaceCapacity'] = request.space_capacity
        if not DaraCore.is_null(request.throughput_mode):
            query['ThroughputMode'] = request.throughput_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFileSystem',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_file_system(
        self,
        request: main_models.ModifyFileSystemRequest,
    ) -> main_models.ModifyFileSystemResponse:
        runtime = RuntimeOptions()
        return self.modify_file_system_with_options(request, runtime)

    async def modify_file_system_async(
        self,
        request: main_models.ModifyFileSystemRequest,
    ) -> main_models.ModifyFileSystemResponse:
        runtime = RuntimeOptions()
        return await self.modify_file_system_with_options_async(request, runtime)

    def modify_mount_point_with_options(
        self,
        request: main_models.ModifyMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMountPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mount_point_with_options_async(
        self,
        request: main_models.ModifyMountPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMountPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMountPoint',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_mount_point(
        self,
        request: main_models.ModifyMountPointRequest,
    ) -> main_models.ModifyMountPointResponse:
        runtime = RuntimeOptions()
        return self.modify_mount_point_with_options(request, runtime)

    async def modify_mount_point_async(
        self,
        request: main_models.ModifyMountPointRequest,
    ) -> main_models.ModifyMountPointResponse:
        runtime = RuntimeOptions()
        return await self.modify_mount_point_with_options_async(request, runtime)

    def modify_qos_policy_with_options(
        self,
        request: main_models.ModifyQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.federation_id):
            query['FederationId'] = request.federation_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.max_ioband_width):
            query['MaxIOBandWidth'] = request.max_ioband_width
        if not DaraCore.is_null(request.max_iops):
            query['MaxIOps'] = request.max_iops
        if not DaraCore.is_null(request.max_meta_qps):
            query['MaxMetaQps'] = request.max_meta_qps
        if not DaraCore.is_null(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQosPolicy',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_qos_policy_with_options_async(
        self,
        request: main_models.ModifyQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.federation_id):
            query['FederationId'] = request.federation_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not DaraCore.is_null(request.max_ioband_width):
            query['MaxIOBandWidth'] = request.max_ioband_width
        if not DaraCore.is_null(request.max_iops):
            query['MaxIOps'] = request.max_iops
        if not DaraCore.is_null(request.max_meta_qps):
            query['MaxMetaQps'] = request.max_meta_qps
        if not DaraCore.is_null(request.qos_policy_id):
            query['QosPolicyId'] = request.qos_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyQosPolicy',
            version = '2018-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_qos_policy(
        self,
        request: main_models.ModifyQosPolicyRequest,
    ) -> main_models.ModifyQosPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_qos_policy_with_options(request, runtime)

    async def modify_qos_policy_async(
        self,
        request: main_models.ModifyQosPolicyRequest,
    ) -> main_models.ModifyQosPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_qos_policy_with_options_async(request, runtime)
