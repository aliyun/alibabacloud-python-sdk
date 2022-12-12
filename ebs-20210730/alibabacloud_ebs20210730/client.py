# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ebs20210730 import models as ebs_20210730_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.AddDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.AddDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.AddDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.AddDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.AddDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.AddDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_disk_replica_pair(
        self,
        request: ebs_20210730_models.AddDiskReplicaPairRequest,
    ) -> ebs_20210730_models.AddDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_disk_replica_pair_with_options(request, runtime)

    async def add_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.AddDiskReplicaPairRequest,
    ) -> ebs_20210730_models.AddDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_disk_replica_pair_with_options_async(request, runtime)

    def apply_lens_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ApplyLensServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ApplyLensService',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ApplyLensServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_lens_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ApplyLensServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ApplyLensService',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ApplyLensServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_lens_service(self) -> ebs_20210730_models.ApplyLensServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_lens_service_with_options(runtime)

    async def apply_lens_service_async(self) -> ebs_20210730_models.ApplyLensServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_lens_service_with_options_async(runtime)

    def cancel_lens_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CancelLensServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CancelLensService',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CancelLensServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_lens_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CancelLensServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CancelLensService',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CancelLensServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_lens_service(self) -> ebs_20210730_models.CancelLensServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_lens_service_with_options(runtime)

    async def cancel_lens_service_async(self) -> ebs_20210730_models.CancelLensServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_lens_service_with_options_async(runtime)

    def create_dedicated_block_storage_cluster_with_options(
        self,
        request: ebs_20210730_models.CreateDedicatedBlockStorageClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.azone):
            query['Azone'] = request.azone
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedBlockStorageCluster',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_block_storage_cluster_with_options_async(
        self,
        request: ebs_20210730_models.CreateDedicatedBlockStorageClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.azone):
            query['Azone'] = request.azone
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedBlockStorageCluster',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_block_storage_cluster(
        self,
        request: ebs_20210730_models.CreateDedicatedBlockStorageClusterRequest,
    ) -> ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_block_storage_cluster_with_options(request, runtime)

    async def create_dedicated_block_storage_cluster_async(
        self,
        request: ebs_20210730_models.CreateDedicatedBlockStorageClusterRequest,
    ) -> ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_block_storage_cluster_with_options_async(request, runtime)

    def create_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.CreateDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.CreateDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_disk_replica_group(
        self,
        request: ebs_20210730_models.CreateDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.CreateDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_disk_replica_group_with_options(request, runtime)

    async def create_disk_replica_group_async(
        self,
        request: ebs_20210730_models.CreateDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.CreateDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_disk_replica_group_with_options_async(request, runtime)

    def create_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.CreateDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_disk_id):
            query['DestinationDiskId'] = request.destination_disk_id
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.pair_name):
            query['PairName'] = request.pair_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.CreateDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_disk_id):
            query['DestinationDiskId'] = request.destination_disk_id
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.pair_name):
            query['PairName'] = request.pair_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_disk_replica_pair(
        self,
        request: ebs_20210730_models.CreateDiskReplicaPairRequest,
    ) -> ebs_20210730_models.CreateDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_disk_replica_pair_with_options(request, runtime)

    async def create_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.CreateDiskReplicaPairRequest,
    ) -> ebs_20210730_models.CreateDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_disk_replica_pair_with_options_async(request, runtime)

    def delete_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_disk_replica_group(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.DeleteDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_replica_group_with_options(request, runtime)

    async def delete_disk_replica_group_async(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.DeleteDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_disk_replica_group_with_options_async(request, runtime)

    def delete_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_disk_replica_pair(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaPairRequest,
    ) -> ebs_20210730_models.DeleteDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_replica_pair_with_options(request, runtime)

    async def delete_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaPairRequest,
    ) -> ebs_20210730_models.DeleteDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_disk_replica_pair_with_options_async(request, runtime)

    def describe_dedicated_block_storage_cluster_disks_with_options(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedBlockStorageClusterDisks',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_block_storage_cluster_disks_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedBlockStorageClusterDisks',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_block_storage_cluster_disks(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksRequest,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_block_storage_cluster_disks_with_options(request, runtime)

    async def describe_dedicated_block_storage_cluster_disks_async(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksRequest,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_block_storage_cluster_disks_with_options_async(request, runtime)

    def describe_dedicated_block_storage_clusters_with_options(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.azone_id):
            body['AzoneId'] = request.azone_id
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_block_storage_cluster_id):
            body['DedicatedBlockStorageClusterId'] = request.dedicated_block_storage_cluster_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedBlockStorageClusters',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_block_storage_clusters_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.azone_id):
            body['AzoneId'] = request.azone_id
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_block_storage_cluster_id):
            body['DedicatedBlockStorageClusterId'] = request.dedicated_block_storage_cluster_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedBlockStorageClusters',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_block_storage_clusters(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClustersRequest,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_block_storage_clusters_with_options(request, runtime)

    async def describe_dedicated_block_storage_clusters_async(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClustersRequest,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_block_storage_clusters_with_options_async(request, runtime)

    def describe_disk_events_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskEvents',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_events_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskEvents',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_events(
        self,
        request: ebs_20210730_models.DescribeDiskEventsRequest,
    ) -> ebs_20210730_models.DescribeDiskEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_events_with_options(request, runtime)

    async def describe_disk_events_async(
        self,
        request: ebs_20210730_models.DescribeDiskEventsRequest,
    ) -> ebs_20210730_models.DescribeDiskEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_events_with_options_async(request, runtime)

    def describe_disk_monitor_data_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskMonitorData',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_monitor_data_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskMonitorData',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_monitor_data(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataRequest,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_monitor_data_with_options(request, runtime)

    async def describe_disk_monitor_data_async(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataRequest,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_monitor_data_with_options_async(request, runtime)

    def describe_disk_monitor_data_list_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskMonitorDataList',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskMonitorDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_monitor_data_list_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskMonitorDataList',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskMonitorDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_monitor_data_list(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataListRequest,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_monitor_data_list_with_options(request, runtime)

    async def describe_disk_monitor_data_list_async(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataListRequest,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_monitor_data_list_with_options_async(request, runtime)

    def describe_disk_replica_groups_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.site):
            query['Site'] = request.site
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaGroups',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_replica_groups_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.site):
            query['Site'] = request.site
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaGroups',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_replica_groups(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaGroupsRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_replica_groups_with_options(request, runtime)

    async def describe_disk_replica_groups_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaGroupsRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_replica_groups_with_options_async(request, runtime)

    def describe_disk_replica_pair_progress_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairProgress',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaPairProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_replica_pair_progress_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairProgress',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaPairProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_replica_pair_progress(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairProgressRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_replica_pair_progress_with_options(request, runtime)

    async def describe_disk_replica_pair_progress_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairProgressRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_replica_pair_progress_with_options_async(request, runtime)

    def describe_disk_replica_pairs_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pair_ids):
            query['PairIds'] = request.pair_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.site):
            query['Site'] = request.site
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairs',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_replica_pairs_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pair_ids):
            query['PairIds'] = request.pair_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.site):
            query['Site'] = request.site
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairs',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_replica_pairs(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairsRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_replica_pairs_with_options(request, runtime)

    async def describe_disk_replica_pairs_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairsRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_replica_pairs_with_options_async(request, runtime)

    def describe_lens_service_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeLensServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeLensServiceStatus',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeLensServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lens_service_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeLensServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeLensServiceStatus',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeLensServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lens_service_status(self) -> ebs_20210730_models.DescribeLensServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lens_service_status_with_options(runtime)

    async def describe_lens_service_status_async(self) -> ebs_20210730_models.DescribeLensServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lens_service_status_with_options_async(runtime)

    def describe_regions_with_options(
        self,
        request: ebs_20210730_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ebs_20210730_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: ebs_20210730_models.DescribeRegionsRequest,
    ) -> ebs_20210730_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ebs_20210730_models.DescribeRegionsRequest,
    ) -> ebs_20210730_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def failover_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.FailoverDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.FailoverDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def failover_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.FailoverDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.FailoverDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def failover_disk_replica_group(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.FailoverDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.failover_disk_replica_group_with_options(request, runtime)

    async def failover_disk_replica_group_async(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.FailoverDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.failover_disk_replica_group_with_options_async(request, runtime)

    def failover_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.FailoverDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.FailoverDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def failover_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.FailoverDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.FailoverDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def failover_disk_replica_pair(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaPairRequest,
    ) -> ebs_20210730_models.FailoverDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.failover_disk_replica_pair_with_options(request, runtime)

    async def failover_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaPairRequest,
    ) -> ebs_20210730_models.FailoverDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.failover_disk_replica_pair_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ebs_20210730_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ebs_20210730_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ebs_20210730_models.ListTagResourcesRequest,
    ) -> ebs_20210730_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ebs_20210730_models.ListTagResourcesRequest,
    ) -> ebs_20210730_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_dedicated_block_storage_cluster_attribute_with_options(
        self,
        request: ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedBlockStorageClusterAttribute',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_block_storage_cluster_attribute_with_options_async(
        self,
        request: ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedBlockStorageClusterAttribute',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_block_storage_cluster_attribute(
        self,
        request: ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
    ) -> ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_block_storage_cluster_attribute_with_options(request, runtime)

    async def modify_dedicated_block_storage_cluster_attribute_async(
        self,
        request: ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
    ) -> ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_block_storage_cluster_attribute_with_options_async(request, runtime)

    def modify_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_replica_group(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.ModifyDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_replica_group_with_options(request, runtime)

    async def modify_disk_replica_group_async(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.ModifyDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_replica_group_with_options_async(request, runtime)

    def modify_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.pair_name):
            query['PairName'] = request.pair_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.pair_name):
            query['PairName'] = request.pair_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_replica_pair(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaPairRequest,
    ) -> ebs_20210730_models.ModifyDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_replica_pair_with_options(request, runtime)

    async def modify_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaPairRequest,
    ) -> ebs_20210730_models.ModifyDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_replica_pair_with_options_async(request, runtime)

    def remove_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.RemoveDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.RemoveDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.RemoveDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.RemoveDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.RemoveDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.RemoveDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_disk_replica_pair(
        self,
        request: ebs_20210730_models.RemoveDiskReplicaPairRequest,
    ) -> ebs_20210730_models.RemoveDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_disk_replica_pair_with_options(request, runtime)

    async def remove_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.RemoveDiskReplicaPairRequest,
    ) -> ebs_20210730_models.RemoveDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_disk_replica_pair_with_options_async(request, runtime)

    def reprotect_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ReprotectDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ReprotectDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def reprotect_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ReprotectDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ReprotectDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reprotect_disk_replica_group(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.ReprotectDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.reprotect_disk_replica_group_with_options(request, runtime)

    async def reprotect_disk_replica_group_async(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.ReprotectDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reprotect_disk_replica_group_with_options_async(request, runtime)

    def reprotect_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ReprotectDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ReprotectDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def reprotect_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ReprotectDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ReprotectDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reprotect_disk_replica_pair(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaPairRequest,
    ) -> ebs_20210730_models.ReprotectDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.reprotect_disk_replica_pair_with_options(request, runtime)

    async def reprotect_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaPairRequest,
    ) -> ebs_20210730_models.ReprotectDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reprotect_disk_replica_pair_with_options_async(request, runtime)

    def start_disk_monitor_with_options(
        self,
        tmp_req: ebs_20210730_models.StartDiskMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskMonitorResponse:
        UtilClient.validate_model(tmp_req)
        request = ebs_20210730_models.StartDiskMonitorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.disk_ids):
            request.disk_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.disk_ids, 'DiskIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.disk_ids_shrink):
            query['DiskIds'] = request.disk_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskMonitor',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_disk_monitor_with_options_async(
        self,
        tmp_req: ebs_20210730_models.StartDiskMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskMonitorResponse:
        UtilClient.validate_model(tmp_req)
        request = ebs_20210730_models.StartDiskMonitorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.disk_ids):
            request.disk_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.disk_ids, 'DiskIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.disk_ids_shrink):
            query['DiskIds'] = request.disk_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskMonitor',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_disk_monitor(
        self,
        request: ebs_20210730_models.StartDiskMonitorRequest,
    ) -> ebs_20210730_models.StartDiskMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_disk_monitor_with_options(request, runtime)

    async def start_disk_monitor_async(
        self,
        request: ebs_20210730_models.StartDiskMonitorRequest,
    ) -> ebs_20210730_models.StartDiskMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_disk_monitor_with_options_async(request, runtime)

    def start_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.StartDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.one_shot):
            query['OneShot'] = request.one_shot
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.StartDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.one_shot):
            query['OneShot'] = request.one_shot
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_disk_replica_group(
        self,
        request: ebs_20210730_models.StartDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.StartDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_disk_replica_group_with_options(request, runtime)

    async def start_disk_replica_group_async(
        self,
        request: ebs_20210730_models.StartDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.StartDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_disk_replica_group_with_options_async(request, runtime)

    def start_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.StartDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.one_shot):
            query['OneShot'] = request.one_shot
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.StartDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.one_shot):
            query['OneShot'] = request.one_shot
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_disk_replica_pair(
        self,
        request: ebs_20210730_models.StartDiskReplicaPairRequest,
    ) -> ebs_20210730_models.StartDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_disk_replica_pair_with_options(request, runtime)

    async def start_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.StartDiskReplicaPairRequest,
    ) -> ebs_20210730_models.StartDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_disk_replica_pair_with_options_async(request, runtime)

    def stop_disk_monitor_with_options(
        self,
        tmp_req: ebs_20210730_models.StopDiskMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskMonitorResponse:
        UtilClient.validate_model(tmp_req)
        request = ebs_20210730_models.StopDiskMonitorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.disk_ids):
            request.disk_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.disk_ids, 'DiskIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.disk_ids_shrink):
            query['DiskIds'] = request.disk_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskMonitor',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_disk_monitor_with_options_async(
        self,
        tmp_req: ebs_20210730_models.StopDiskMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskMonitorResponse:
        UtilClient.validate_model(tmp_req)
        request = ebs_20210730_models.StopDiskMonitorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.disk_ids):
            request.disk_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.disk_ids, 'DiskIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.disk_ids_shrink):
            query['DiskIds'] = request.disk_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskMonitor',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_disk_monitor(
        self,
        request: ebs_20210730_models.StopDiskMonitorRequest,
    ) -> ebs_20210730_models.StopDiskMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_disk_monitor_with_options(request, runtime)

    async def stop_disk_monitor_async(
        self,
        request: ebs_20210730_models.StopDiskMonitorRequest,
    ) -> ebs_20210730_models.StopDiskMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_disk_monitor_with_options_async(request, runtime)

    def stop_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.StopDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.StopDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskReplicaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_disk_replica_group(
        self,
        request: ebs_20210730_models.StopDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.StopDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_disk_replica_group_with_options(request, runtime)

    async def stop_disk_replica_group_async(
        self,
        request: ebs_20210730_models.StopDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.StopDiskReplicaGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_disk_replica_group_with_options_async(request, runtime)

    def stop_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.StopDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.StopDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_disk_replica_pair(
        self,
        request: ebs_20210730_models.StopDiskReplicaPairRequest,
    ) -> ebs_20210730_models.StopDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_disk_replica_pair_with_options(request, runtime)

    async def stop_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.StopDiskReplicaPairRequest,
    ) -> ebs_20210730_models.StopDiskReplicaPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_disk_replica_pair_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ebs_20210730_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ebs_20210730_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ebs_20210730_models.TagResourcesRequest,
    ) -> ebs_20210730_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ebs_20210730_models.TagResourcesRequest,
    ) -> ebs_20210730_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ebs_20210730_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ebs_20210730_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: ebs_20210730_models.UntagResourcesRequest,
    ) -> ebs_20210730_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ebs_20210730_models.UntagResourcesRequest,
    ) -> ebs_20210730_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
