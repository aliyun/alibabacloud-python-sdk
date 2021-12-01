# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateDiskReplicaPairRequest(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        charge_type: str = None,
        client_token: str = None,
        description: str = None,
        destination_disk_id: str = None,
        destination_region_id: str = None,
        destination_zone_id: str = None,
        disk_id: str = None,
        pair_name: str = None,
        period: int = None,
        period_unit: str = None,
        source_region_id: str = None,
        source_zone_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.charge_type = charge_type
        self.client_token = client_token
        self.description = description
        self.destination_disk_id = destination_disk_id
        self.destination_region_id = destination_region_id
        self.destination_zone_id = destination_zone_id
        self.disk_id = disk_id
        self.pair_name = pair_name
        self.period = period
        self.period_unit = period_unit
        self.source_region_id = source_region_id
        self.source_zone_id = source_zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_disk_id is not None:
            result['DestinationDiskId'] = self.destination_disk_id
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.pair_name is not None:
            result['PairName'] = self.pair_name
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationDiskId') is not None:
            self.destination_disk_id = m.get('DestinationDiskId')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('PairName') is not None:
            self.pair_name = m.get('PairName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')
        return self


class CreateDiskReplicaPairResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        replica_pair_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.replica_pair_id = replica_pair_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDiskReplicaPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDiskReplicaPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDiskReplicaPairRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        replica_pair_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.replica_pair_id = replica_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class DeleteDiskReplicaPairResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDiskReplicaPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDiskReplicaPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiskReplicaPairsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        pair_ids: str = None,
        region_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.pair_ids = pair_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.pair_ids is not None:
            result['PairIds'] = self.pair_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PairIds') is not None:
            self.pair_ids = m.get('PairIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDiskReplicaPairsResponseBodyReplicaPairs(TeaModel):
    def __init__(
        self,
        async_cycle: int = None,
        bandwidth: int = None,
        description: str = None,
        destination_disk_id: str = None,
        destination_region: str = None,
        last_rpo: int = None,
        pair_name: str = None,
        replica_pair_id: str = None,
        source_disk_id: str = None,
        source_region: str = None,
        status: str = None,
        status_message: str = None,
    ):
        self.async_cycle = async_cycle
        self.bandwidth = bandwidth
        self.description = description
        self.destination_disk_id = destination_disk_id
        self.destination_region = destination_region
        self.last_rpo = last_rpo
        self.pair_name = pair_name
        self.replica_pair_id = replica_pair_id
        self.source_disk_id = source_disk_id
        self.source_region = source_region
        self.status = status
        self.status_message = status_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_cycle is not None:
            result['AsyncCycle'] = self.async_cycle
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_disk_id is not None:
            result['DestinationDiskId'] = self.destination_disk_id
        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region
        if self.last_rpo is not None:
            result['LastRPO'] = self.last_rpo
        if self.pair_name is not None:
            result['PairName'] = self.pair_name
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id
        if self.source_region is not None:
            result['SourceRegion'] = self.source_region
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncCycle') is not None:
            self.async_cycle = m.get('AsyncCycle')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationDiskId') is not None:
            self.destination_disk_id = m.get('DestinationDiskId')
        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')
        if m.get('LastRPO') is not None:
            self.last_rpo = m.get('LastRPO')
        if m.get('PairName') is not None:
            self.pair_name = m.get('PairName')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')
        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class DescribeDiskReplicaPairsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        replica_pairs: List[DescribeDiskReplicaPairsResponseBodyReplicaPairs] = None,
        request_id: str = None,
    ):
        self.next_token = next_token
        self.replica_pairs = replica_pairs
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.replica_pairs:
            for k in self.replica_pairs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ReplicaPairs'] = []
        if self.replica_pairs is not None:
            for k in self.replica_pairs:
                result['ReplicaPairs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.replica_pairs = []
        if m.get('ReplicaPairs') is not None:
            for k in m.get('ReplicaPairs'):
                temp_model = DescribeDiskReplicaPairsResponseBodyReplicaPairs()
                self.replica_pairs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDiskReplicaPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDiskReplicaPairsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDiskReplicaPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        resource_type: str = None,
    ):
        self.accept_language = accept_language
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeRegionsResponseBodyRegionsZones(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        self.local_name = local_name
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        zones: List[DescribeRegionsResponseBodyRegionsZones] = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeRegionsResponseBodyRegionsZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FailoverDiskReplicaPairRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        replica_pair_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.replica_pair_id = replica_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class FailoverDiskReplicaPairResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FailoverDiskReplicaPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FailoverDiskReplicaPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FailoverDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskReplicaPairRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        pair_name: str = None,
        region_id: str = None,
        replica_pair_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.pair_name = pair_name
        self.region_id = region_id
        self.replica_pair_id = replica_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.pair_name is not None:
            result['PairName'] = self.pair_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PairName') is not None:
            self.pair_name = m.get('PairName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class ModifyDiskReplicaPairResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDiskReplicaPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDiskReplicaPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReprotectDiskReplicaPairRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        replica_pair_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.replica_pair_id = replica_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class ReprotectDiskReplicaPairResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReprotectDiskReplicaPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReprotectDiskReplicaPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReprotectDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDiskReplicaPairRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        replica_pair_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.replica_pair_id = replica_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class StartDiskReplicaPairResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartDiskReplicaPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDiskReplicaPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDiskReplicaPairRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        replica_pair_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.replica_pair_id = replica_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class StopDiskReplicaPairResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopDiskReplicaPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDiskReplicaPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


