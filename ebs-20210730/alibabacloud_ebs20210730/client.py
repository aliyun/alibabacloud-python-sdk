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

    def create_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.CreateDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bandwidth'] = request.bandwidth
        query['ChargeType'] = request.charge_type
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['DestinationDiskId'] = request.destination_disk_id
        query['DestinationRegionId'] = request.destination_region_id
        query['DestinationZoneId'] = request.destination_zone_id
        query['DiskId'] = request.disk_id
        query['PairName'] = request.pair_name
        query['Period'] = request.period
        query['PeriodUnit'] = request.period_unit
        query['SourceRegionId'] = request.source_region_id
        query['SourceZoneId'] = request.source_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Bandwidth'] = request.bandwidth
        query['ChargeType'] = request.charge_type
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['DestinationDiskId'] = request.destination_disk_id
        query['DestinationRegionId'] = request.destination_region_id
        query['DestinationZoneId'] = request.destination_zone_id
        query['DiskId'] = request.disk_id
        query['PairName'] = request.pair_name
        query['Period'] = request.period
        query['PeriodUnit'] = request.period_unit
        query['SourceRegionId'] = request.source_region_id
        query['SourceZoneId'] = request.source_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def delete_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def describe_disk_replica_pairs_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['PairIds'] = request.pair_ids
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairs',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['PairIds'] = request.pair_ids
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairs',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def describe_regions_with_options(
        self,
        request: ebs_20210730_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AcceptLanguage'] = request.accept_language
        query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AcceptLanguage'] = request.accept_language
        query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def failover_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.FailoverDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def modify_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['PairName'] = request.pair_name
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['PairName'] = request.pair_name
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def reprotect_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ReprotectDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def start_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.StartDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def stop_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.StopDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskReplicaPairResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
