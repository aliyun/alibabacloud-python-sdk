# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dfs20180620 import models as dfs20180620_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_vsc_mount_point_with_options(
        self,
        tmp_req: dfs20180620_models.AttachVscMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.AttachVscMountPointResponse:
        """
        ***\
        
        @param tmp_req: AttachVscMountPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachVscMountPointResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dfs20180620_models.AttachVscMountPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not UtilClient.is_unset(tmp_req.vsc_ids):
            request.vsc_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vsc_ids, 'VscIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not UtilClient.is_unset(request.vsc_ids_shrink):
            query['VscIds'] = request.vsc_ids_shrink
        if not UtilClient.is_unset(request.vsc_type):
            query['VscType'] = request.vsc_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachVscMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.AttachVscMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_vsc_mount_point_with_options_async(
        self,
        tmp_req: dfs20180620_models.AttachVscMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.AttachVscMountPointResponse:
        """
        ***\
        
        @param tmp_req: AttachVscMountPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachVscMountPointResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dfs20180620_models.AttachVscMountPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not UtilClient.is_unset(tmp_req.vsc_ids):
            request.vsc_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vsc_ids, 'VscIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not UtilClient.is_unset(request.vsc_ids_shrink):
            query['VscIds'] = request.vsc_ids_shrink
        if not UtilClient.is_unset(request.vsc_type):
            query['VscType'] = request.vsc_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachVscMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.AttachVscMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_vsc_mount_point(
        self,
        request: dfs20180620_models.AttachVscMountPointRequest,
    ) -> dfs20180620_models.AttachVscMountPointResponse:
        """
        ***\
        
        @param request: AttachVscMountPointRequest
        @return: AttachVscMountPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_vsc_mount_point_with_options(request, runtime)

    async def attach_vsc_mount_point_async(
        self,
        request: dfs20180620_models.AttachVscMountPointRequest,
    ) -> dfs20180620_models.AttachVscMountPointResponse:
        """
        ***\
        
        @param request: AttachVscMountPointRequest
        @return: AttachVscMountPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_vsc_mount_point_with_options_async(request, runtime)

    def bind_vsc_mount_point_alias_with_options(
        self,
        request: dfs20180620_models.BindVscMountPointAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.BindVscMountPointAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_prefix):
            query['AliasPrefix'] = request.alias_prefix
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindVscMountPointAlias',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.BindVscMountPointAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_vsc_mount_point_alias_with_options_async(
        self,
        request: dfs20180620_models.BindVscMountPointAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.BindVscMountPointAliasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_prefix):
            query['AliasPrefix'] = request.alias_prefix
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindVscMountPointAlias',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.BindVscMountPointAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_vsc_mount_point_alias(
        self,
        request: dfs20180620_models.BindVscMountPointAliasRequest,
    ) -> dfs20180620_models.BindVscMountPointAliasResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_vsc_mount_point_alias_with_options(request, runtime)

    async def bind_vsc_mount_point_alias_async(
        self,
        request: dfs20180620_models.BindVscMountPointAliasRequest,
    ) -> dfs20180620_models.BindVscMountPointAliasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_vsc_mount_point_alias_with_options_async(request, runtime)

    def create_access_group_with_options(
        self,
        request: dfs20180620_models.CreateAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessGroup',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_group_with_options_async(
        self,
        request: dfs20180620_models.CreateAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessGroup',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_group(
        self,
        request: dfs20180620_models.CreateAccessGroupRequest,
    ) -> dfs20180620_models.CreateAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_group_with_options(request, runtime)

    async def create_access_group_async(
        self,
        request: dfs20180620_models.CreateAccessGroupRequest,
    ) -> dfs20180620_models.CreateAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_group_with_options_async(request, runtime)

    def create_access_rule_with_options(
        self,
        request: dfs20180620_models.CreateAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.network_segment):
            query['NetworkSegment'] = request.network_segment
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessRule',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_rule_with_options_async(
        self,
        request: dfs20180620_models.CreateAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.network_segment):
            query['NetworkSegment'] = request.network_segment
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessRule',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_rule(
        self,
        request: dfs20180620_models.CreateAccessRuleRequest,
    ) -> dfs20180620_models.CreateAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_rule_with_options(request, runtime)

    async def create_access_rule_async(
        self,
        request: dfs20180620_models.CreateAccessRuleRequest,
    ) -> dfs20180620_models.CreateAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_rule_with_options_async(request, runtime)

    def create_file_system_with_options(
        self,
        request: dfs20180620_models.CreateFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_redundancy_type):
            query['DataRedundancyType'] = request.data_redundancy_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_name):
            query['FileSystemName'] = request.file_system_name
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.partition_number):
            query['PartitionNumber'] = request.partition_number
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.provisioned_throughput_in_mi_bps):
            query['ProvisionedThroughputInMiBps'] = request.provisioned_throughput_in_mi_bps
        if not UtilClient.is_unset(request.space_capacity):
            query['SpaceCapacity'] = request.space_capacity
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.throughput_mode):
            query['ThroughputMode'] = request.throughput_mode
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileSystem',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_system_with_options_async(
        self,
        request: dfs20180620_models.CreateFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_redundancy_type):
            query['DataRedundancyType'] = request.data_redundancy_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_name):
            query['FileSystemName'] = request.file_system_name
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.partition_number):
            query['PartitionNumber'] = request.partition_number
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.provisioned_throughput_in_mi_bps):
            query['ProvisionedThroughputInMiBps'] = request.provisioned_throughput_in_mi_bps
        if not UtilClient.is_unset(request.space_capacity):
            query['SpaceCapacity'] = request.space_capacity
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.throughput_mode):
            query['ThroughputMode'] = request.throughput_mode
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileSystem',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_system(
        self,
        request: dfs20180620_models.CreateFileSystemRequest,
    ) -> dfs20180620_models.CreateFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_file_system_with_options(request, runtime)

    async def create_file_system_async(
        self,
        request: dfs20180620_models.CreateFileSystemRequest,
    ) -> dfs20180620_models.CreateFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_file_system_with_options_async(request, runtime)

    def create_mount_point_with_options(
        self,
        request: dfs20180620_models.CreateMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateMountPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mount_point_with_options_async(
        self,
        request: dfs20180620_models.CreateMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateMountPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mount_point(
        self,
        request: dfs20180620_models.CreateMountPointRequest,
    ) -> dfs20180620_models.CreateMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mount_point_with_options(request, runtime)

    async def create_mount_point_async(
        self,
        request: dfs20180620_models.CreateMountPointRequest,
    ) -> dfs20180620_models.CreateMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mount_point_with_options_async(request, runtime)

    def create_user_groups_mapping_with_options(
        self,
        tmp_req: dfs20180620_models.CreateUserGroupsMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateUserGroupsMappingResponse:
        UtilClient.validate_model(tmp_req)
        request = dfs20180620_models.CreateUserGroupsMappingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.group_names):
            request.group_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_names, 'GroupNames', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserGroupsMapping',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateUserGroupsMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_groups_mapping_with_options_async(
        self,
        tmp_req: dfs20180620_models.CreateUserGroupsMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateUserGroupsMappingResponse:
        UtilClient.validate_model(tmp_req)
        request = dfs20180620_models.CreateUserGroupsMappingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.group_names):
            request.group_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_names, 'GroupNames', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserGroupsMapping',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateUserGroupsMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_groups_mapping(
        self,
        request: dfs20180620_models.CreateUserGroupsMappingRequest,
    ) -> dfs20180620_models.CreateUserGroupsMappingResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_groups_mapping_with_options(request, runtime)

    async def create_user_groups_mapping_async(
        self,
        request: dfs20180620_models.CreateUserGroupsMappingRequest,
    ) -> dfs20180620_models.CreateUserGroupsMappingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_groups_mapping_with_options_async(request, runtime)

    def create_vsc_mount_point_with_options(
        self,
        tmp_req: dfs20180620_models.CreateVscMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateVscMountPointResponse:
        UtilClient.validate_model(tmp_req)
        request = dfs20180620_models.CreateVscMountPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVscMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateVscMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vsc_mount_point_with_options_async(
        self,
        tmp_req: dfs20180620_models.CreateVscMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.CreateVscMountPointResponse:
        UtilClient.validate_model(tmp_req)
        request = dfs20180620_models.CreateVscMountPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVscMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.CreateVscMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vsc_mount_point(
        self,
        request: dfs20180620_models.CreateVscMountPointRequest,
    ) -> dfs20180620_models.CreateVscMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vsc_mount_point_with_options(request, runtime)

    async def create_vsc_mount_point_async(
        self,
        request: dfs20180620_models.CreateVscMountPointRequest,
    ) -> dfs20180620_models.CreateVscMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vsc_mount_point_with_options_async(request, runtime)

    def delete_access_group_with_options(
        self,
        request: dfs20180620_models.DeleteAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessGroup',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_group_with_options_async(
        self,
        request: dfs20180620_models.DeleteAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessGroup',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_group(
        self,
        request: dfs20180620_models.DeleteAccessGroupRequest,
    ) -> dfs20180620_models.DeleteAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_group_with_options(request, runtime)

    async def delete_access_group_async(
        self,
        request: dfs20180620_models.DeleteAccessGroupRequest,
    ) -> dfs20180620_models.DeleteAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_group_with_options_async(request, runtime)

    def delete_access_rule_with_options(
        self,
        request: dfs20180620_models.DeleteAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessRule',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_rule_with_options_async(
        self,
        request: dfs20180620_models.DeleteAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessRule',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_rule(
        self,
        request: dfs20180620_models.DeleteAccessRuleRequest,
    ) -> dfs20180620_models.DeleteAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_rule_with_options(request, runtime)

    async def delete_access_rule_async(
        self,
        request: dfs20180620_models.DeleteAccessRuleRequest,
    ) -> dfs20180620_models.DeleteAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_rule_with_options_async(request, runtime)

    def delete_file_system_with_options(
        self,
        request: dfs20180620_models.DeleteFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileSystem',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_system_with_options_async(
        self,
        request: dfs20180620_models.DeleteFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileSystem',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file_system(
        self,
        request: dfs20180620_models.DeleteFileSystemRequest,
    ) -> dfs20180620_models.DeleteFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_file_system_with_options(request, runtime)

    async def delete_file_system_async(
        self,
        request: dfs20180620_models.DeleteFileSystemRequest,
    ) -> dfs20180620_models.DeleteFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_system_with_options_async(request, runtime)

    def delete_mount_point_with_options(
        self,
        request: dfs20180620_models.DeleteMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteMountPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mount_point_with_options_async(
        self,
        request: dfs20180620_models.DeleteMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteMountPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mount_point(
        self,
        request: dfs20180620_models.DeleteMountPointRequest,
    ) -> dfs20180620_models.DeleteMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mount_point_with_options(request, runtime)

    async def delete_mount_point_async(
        self,
        request: dfs20180620_models.DeleteMountPointRequest,
    ) -> dfs20180620_models.DeleteMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mount_point_with_options_async(request, runtime)

    def delete_user_groups_mapping_with_options(
        self,
        tmp_req: dfs20180620_models.DeleteUserGroupsMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteUserGroupsMappingResponse:
        UtilClient.validate_model(tmp_req)
        request = dfs20180620_models.DeleteUserGroupsMappingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.group_names):
            request.group_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_names, 'GroupNames', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroupsMapping',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteUserGroupsMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_groups_mapping_with_options_async(
        self,
        tmp_req: dfs20180620_models.DeleteUserGroupsMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteUserGroupsMappingResponse:
        UtilClient.validate_model(tmp_req)
        request = dfs20180620_models.DeleteUserGroupsMappingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.group_names):
            request.group_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_names, 'GroupNames', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroupsMapping',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteUserGroupsMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_groups_mapping(
        self,
        request: dfs20180620_models.DeleteUserGroupsMappingRequest,
    ) -> dfs20180620_models.DeleteUserGroupsMappingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_groups_mapping_with_options(request, runtime)

    async def delete_user_groups_mapping_async(
        self,
        request: dfs20180620_models.DeleteUserGroupsMappingRequest,
    ) -> dfs20180620_models.DeleteUserGroupsMappingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_groups_mapping_with_options_async(request, runtime)

    def delete_vsc_mount_point_with_options(
        self,
        request: dfs20180620_models.DeleteVscMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteVscMountPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVscMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteVscMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vsc_mount_point_with_options_async(
        self,
        request: dfs20180620_models.DeleteVscMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DeleteVscMountPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVscMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DeleteVscMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vsc_mount_point(
        self,
        request: dfs20180620_models.DeleteVscMountPointRequest,
    ) -> dfs20180620_models.DeleteVscMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vsc_mount_point_with_options(request, runtime)

    async def delete_vsc_mount_point_async(
        self,
        request: dfs20180620_models.DeleteVscMountPointRequest,
    ) -> dfs20180620_models.DeleteVscMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vsc_mount_point_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: dfs20180620_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: dfs20180620_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: dfs20180620_models.DescribeRegionsRequest,
    ) -> dfs20180620_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: dfs20180620_models.DescribeRegionsRequest,
    ) -> dfs20180620_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_vsc_mount_points_with_options(
        self,
        request: dfs20180620_models.DescribeVscMountPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DescribeVscMountPointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.vsc_id):
            query['VscId'] = request.vsc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVscMountPoints',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DescribeVscMountPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vsc_mount_points_with_options_async(
        self,
        request: dfs20180620_models.DescribeVscMountPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DescribeVscMountPointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.vsc_id):
            query['VscId'] = request.vsc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVscMountPoints',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DescribeVscMountPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vsc_mount_points(
        self,
        request: dfs20180620_models.DescribeVscMountPointsRequest,
    ) -> dfs20180620_models.DescribeVscMountPointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vsc_mount_points_with_options(request, runtime)

    async def describe_vsc_mount_points_async(
        self,
        request: dfs20180620_models.DescribeVscMountPointsRequest,
    ) -> dfs20180620_models.DescribeVscMountPointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vsc_mount_points_with_options_async(request, runtime)

    def detach_vsc_mount_point_with_options(
        self,
        tmp_req: dfs20180620_models.DetachVscMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DetachVscMountPointResponse:
        UtilClient.validate_model(tmp_req)
        request = dfs20180620_models.DetachVscMountPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not UtilClient.is_unset(tmp_req.vsc_ids):
            request.vsc_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vsc_ids, 'VscIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not UtilClient.is_unset(request.vsc_ids_shrink):
            query['VscIds'] = request.vsc_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachVscMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DetachVscMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_vsc_mount_point_with_options_async(
        self,
        tmp_req: dfs20180620_models.DetachVscMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.DetachVscMountPointResponse:
        UtilClient.validate_model(tmp_req)
        request = dfs20180620_models.DetachVscMountPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not UtilClient.is_unset(tmp_req.vsc_ids):
            request.vsc_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vsc_ids, 'VscIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not UtilClient.is_unset(request.vsc_ids_shrink):
            query['VscIds'] = request.vsc_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachVscMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.DetachVscMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_vsc_mount_point(
        self,
        request: dfs20180620_models.DetachVscMountPointRequest,
    ) -> dfs20180620_models.DetachVscMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_vsc_mount_point_with_options(request, runtime)

    async def detach_vsc_mount_point_async(
        self,
        request: dfs20180620_models.DetachVscMountPointRequest,
    ) -> dfs20180620_models.DetachVscMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_vsc_mount_point_with_options_async(request, runtime)

    def get_access_group_with_options(
        self,
        request: dfs20180620_models.GetAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.GetAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessGroup',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.GetAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_group_with_options_async(
        self,
        request: dfs20180620_models.GetAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.GetAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessGroup',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.GetAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_group(
        self,
        request: dfs20180620_models.GetAccessGroupRequest,
    ) -> dfs20180620_models.GetAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_group_with_options(request, runtime)

    async def get_access_group_async(
        self,
        request: dfs20180620_models.GetAccessGroupRequest,
    ) -> dfs20180620_models.GetAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_group_with_options_async(request, runtime)

    def get_access_rule_with_options(
        self,
        request: dfs20180620_models.GetAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.GetAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessRule',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.GetAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_rule_with_options_async(
        self,
        request: dfs20180620_models.GetAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.GetAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessRule',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.GetAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_rule(
        self,
        request: dfs20180620_models.GetAccessRuleRequest,
    ) -> dfs20180620_models.GetAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_rule_with_options(request, runtime)

    async def get_access_rule_async(
        self,
        request: dfs20180620_models.GetAccessRuleRequest,
    ) -> dfs20180620_models.GetAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_rule_with_options_async(request, runtime)

    def get_file_system_with_options(
        self,
        request: dfs20180620_models.GetFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.GetFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileSystem',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.GetFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_system_with_options_async(
        self,
        request: dfs20180620_models.GetFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.GetFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileSystem',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.GetFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_system(
        self,
        request: dfs20180620_models.GetFileSystemRequest,
    ) -> dfs20180620_models.GetFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_file_system_with_options(request, runtime)

    async def get_file_system_async(
        self,
        request: dfs20180620_models.GetFileSystemRequest,
    ) -> dfs20180620_models.GetFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_file_system_with_options_async(request, runtime)

    def get_mount_point_with_options(
        self,
        request: dfs20180620_models.GetMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.GetMountPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.GetMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mount_point_with_options_async(
        self,
        request: dfs20180620_models.GetMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.GetMountPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.GetMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mount_point(
        self,
        request: dfs20180620_models.GetMountPointRequest,
    ) -> dfs20180620_models.GetMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mount_point_with_options(request, runtime)

    async def get_mount_point_async(
        self,
        request: dfs20180620_models.GetMountPointRequest,
    ) -> dfs20180620_models.GetMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mount_point_with_options_async(request, runtime)

    def get_region_with_options(
        self,
        request: dfs20180620_models.GetRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.GetRegionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegion',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.GetRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_region_with_options_async(
        self,
        request: dfs20180620_models.GetRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.GetRegionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegion',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.GetRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_region(
        self,
        request: dfs20180620_models.GetRegionRequest,
    ) -> dfs20180620_models.GetRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_region_with_options(request, runtime)

    async def get_region_async(
        self,
        request: dfs20180620_models.GetRegionRequest,
    ) -> dfs20180620_models.GetRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_region_with_options_async(request, runtime)

    def list_access_groups_with_options(
        self,
        request: dfs20180620_models.ListAccessGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ListAccessGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessGroups',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ListAccessGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_groups_with_options_async(
        self,
        request: dfs20180620_models.ListAccessGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ListAccessGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessGroups',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ListAccessGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_groups(
        self,
        request: dfs20180620_models.ListAccessGroupsRequest,
    ) -> dfs20180620_models.ListAccessGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_groups_with_options(request, runtime)

    async def list_access_groups_async(
        self,
        request: dfs20180620_models.ListAccessGroupsRequest,
    ) -> dfs20180620_models.ListAccessGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_groups_with_options_async(request, runtime)

    def list_access_rules_with_options(
        self,
        request: dfs20180620_models.ListAccessRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ListAccessRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessRules',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ListAccessRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_rules_with_options_async(
        self,
        request: dfs20180620_models.ListAccessRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ListAccessRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessRules',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ListAccessRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_rules(
        self,
        request: dfs20180620_models.ListAccessRulesRequest,
    ) -> dfs20180620_models.ListAccessRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_rules_with_options(request, runtime)

    async def list_access_rules_async(
        self,
        request: dfs20180620_models.ListAccessRulesRequest,
    ) -> dfs20180620_models.ListAccessRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_rules_with_options_async(request, runtime)

    def list_file_systems_with_options(
        self,
        request: dfs20180620_models.ListFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ListFileSystemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFileSystems',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ListFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_file_systems_with_options_async(
        self,
        request: dfs20180620_models.ListFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ListFileSystemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFileSystems',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ListFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_file_systems(
        self,
        request: dfs20180620_models.ListFileSystemsRequest,
    ) -> dfs20180620_models.ListFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_file_systems_with_options(request, runtime)

    async def list_file_systems_async(
        self,
        request: dfs20180620_models.ListFileSystemsRequest,
    ) -> dfs20180620_models.ListFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_file_systems_with_options_async(request, runtime)

    def list_mount_points_with_options(
        self,
        request: dfs20180620_models.ListMountPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ListMountPointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMountPoints',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ListMountPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mount_points_with_options_async(
        self,
        request: dfs20180620_models.ListMountPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ListMountPointsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.start_offset):
            query['StartOffset'] = request.start_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMountPoints',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ListMountPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mount_points(
        self,
        request: dfs20180620_models.ListMountPointsRequest,
    ) -> dfs20180620_models.ListMountPointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_mount_points_with_options(request, runtime)

    async def list_mount_points_async(
        self,
        request: dfs20180620_models.ListMountPointsRequest,
    ) -> dfs20180620_models.ListMountPointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_mount_points_with_options_async(request, runtime)

    def list_user_groups_mappings_with_options(
        self,
        request: dfs20180620_models.ListUserGroupsMappingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ListUserGroupsMappingsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filesystem_id):
            query['FilesystemId'] = request.filesystem_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsMappings',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ListUserGroupsMappingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_mappings_with_options_async(
        self,
        request: dfs20180620_models.ListUserGroupsMappingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ListUserGroupsMappingsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filesystem_id):
            query['FilesystemId'] = request.filesystem_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsMappings',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ListUserGroupsMappingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups_mappings(
        self,
        request: dfs20180620_models.ListUserGroupsMappingsRequest,
    ) -> dfs20180620_models.ListUserGroupsMappingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_mappings_with_options(request, runtime)

    async def list_user_groups_mappings_async(
        self,
        request: dfs20180620_models.ListUserGroupsMappingsRequest,
    ) -> dfs20180620_models.ListUserGroupsMappingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_mappings_with_options_async(request, runtime)

    def modify_access_group_with_options(
        self,
        request: dfs20180620_models.ModifyAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ModifyAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessGroup',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ModifyAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_group_with_options_async(
        self,
        request: dfs20180620_models.ModifyAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ModifyAccessGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessGroup',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ModifyAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_group(
        self,
        request: dfs20180620_models.ModifyAccessGroupRequest,
    ) -> dfs20180620_models.ModifyAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_access_group_with_options(request, runtime)

    async def modify_access_group_async(
        self,
        request: dfs20180620_models.ModifyAccessGroupRequest,
    ) -> dfs20180620_models.ModifyAccessGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_access_group_with_options_async(request, runtime)

    def modify_access_rule_with_options(
        self,
        request: dfs20180620_models.ModifyAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ModifyAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessRule',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ModifyAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_rule_with_options_async(
        self,
        request: dfs20180620_models.ModifyAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ModifyAccessRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessRule',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ModifyAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_rule(
        self,
        request: dfs20180620_models.ModifyAccessRuleRequest,
    ) -> dfs20180620_models.ModifyAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_access_rule_with_options(request, runtime)

    async def modify_access_rule_async(
        self,
        request: dfs20180620_models.ModifyAccessRuleRequest,
    ) -> dfs20180620_models.ModifyAccessRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_access_rule_with_options_async(request, runtime)

    def modify_file_system_with_options(
        self,
        request: dfs20180620_models.ModifyFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ModifyFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_name):
            query['FileSystemName'] = request.file_system_name
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.provisioned_throughput_in_mi_bps):
            query['ProvisionedThroughputInMiBps'] = request.provisioned_throughput_in_mi_bps
        if not UtilClient.is_unset(request.space_capacity):
            query['SpaceCapacity'] = request.space_capacity
        if not UtilClient.is_unset(request.throughput_mode):
            query['ThroughputMode'] = request.throughput_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFileSystem',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ModifyFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_file_system_with_options_async(
        self,
        request: dfs20180620_models.ModifyFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ModifyFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_name):
            query['FileSystemName'] = request.file_system_name
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.provisioned_throughput_in_mi_bps):
            query['ProvisionedThroughputInMiBps'] = request.provisioned_throughput_in_mi_bps
        if not UtilClient.is_unset(request.space_capacity):
            query['SpaceCapacity'] = request.space_capacity
        if not UtilClient.is_unset(request.throughput_mode):
            query['ThroughputMode'] = request.throughput_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFileSystem',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ModifyFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_file_system(
        self,
        request: dfs20180620_models.ModifyFileSystemRequest,
    ) -> dfs20180620_models.ModifyFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_file_system_with_options(request, runtime)

    async def modify_file_system_async(
        self,
        request: dfs20180620_models.ModifyFileSystemRequest,
    ) -> dfs20180620_models.ModifyFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_file_system_with_options_async(request, runtime)

    def modify_mount_point_with_options(
        self,
        request: dfs20180620_models.ModifyMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ModifyMountPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ModifyMountPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mount_point_with_options_async(
        self,
        request: dfs20180620_models.ModifyMountPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dfs20180620_models.ModifyMountPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_id):
            query['AccessGroupId'] = request.access_group_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.input_region_id):
            query['InputRegionId'] = request.input_region_id
        if not UtilClient.is_unset(request.mount_point_id):
            query['MountPointId'] = request.mount_point_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMountPoint',
            version='2018-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dfs20180620_models.ModifyMountPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_mount_point(
        self,
        request: dfs20180620_models.ModifyMountPointRequest,
    ) -> dfs20180620_models.ModifyMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_mount_point_with_options(request, runtime)

    async def modify_mount_point_async(
        self,
        request: dfs20180620_models.ModifyMountPointRequest,
    ) -> dfs20180620_models.ModifyMountPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_mount_point_with_options_async(request, runtime)
