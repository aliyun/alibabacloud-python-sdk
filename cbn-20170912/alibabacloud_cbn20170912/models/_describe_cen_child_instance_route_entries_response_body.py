# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenChildInstanceRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        cen_route_entries: main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cen_route_entries = cen_route_entries
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cen_route_entries:
            self.cen_route_entries.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_route_entries is not None:
            result['CenRouteEntries'] = self.cen_route_entries.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenRouteEntries') is not None:
            temp_model = main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries()
            self.cen_route_entries = temp_model.from_map(m.get('CenRouteEntries'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries(DaraModel):
    def __init__(
        self,
        cen_route_entry: List[main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry] = None,
    ):
        self.cen_route_entry = cen_route_entry

    def validate(self):
        if self.cen_route_entry:
            for v1 in self.cen_route_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CenRouteEntry'] = []
        if self.cen_route_entry is not None:
            for k1 in self.cen_route_entry:
                result['CenRouteEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_route_entry = []
        if m.get('CenRouteEntry') is not None:
            for k1 in m.get('CenRouteEntry'):
                temp_model = main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry()
                self.cen_route_entry.append(temp_model.from_map(k1))

        return self

class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry(DaraModel):
    def __init__(
        self,
        as_paths: main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths = None,
        cen_route_map_records: main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords = None,
        communities: main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities = None,
        conflicts: main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflicts = None,
        destination_cidr_block: str = None,
        next_hop_instance_id: str = None,
        next_hop_region_id: str = None,
        next_hop_type: str = None,
        operational_mode: bool = None,
        publish_status: str = None,
        route_table_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.as_paths = as_paths
        self.cen_route_map_records = cen_route_map_records
        self.communities = communities
        self.conflicts = conflicts
        self.destination_cidr_block = destination_cidr_block
        self.next_hop_instance_id = next_hop_instance_id
        self.next_hop_region_id = next_hop_region_id
        self.next_hop_type = next_hop_type
        self.operational_mode = operational_mode
        self.publish_status = publish_status
        self.route_table_id = route_table_id
        self.status = status
        self.type = type

    def validate(self):
        if self.as_paths:
            self.as_paths.validate()
        if self.cen_route_map_records:
            self.cen_route_map_records.validate()
        if self.communities:
            self.communities.validate()
        if self.conflicts:
            self.conflicts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.as_paths is not None:
            result['AsPaths'] = self.as_paths.to_map()

        if self.cen_route_map_records is not None:
            result['CenRouteMapRecords'] = self.cen_route_map_records.to_map()

        if self.communities is not None:
            result['Communities'] = self.communities.to_map()

        if self.conflicts is not None:
            result['Conflicts'] = self.conflicts.to_map()

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id

        if self.next_hop_region_id is not None:
            result['NextHopRegionId'] = self.next_hop_region_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.operational_mode is not None:
            result['OperationalMode'] = self.operational_mode

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPaths') is not None:
            temp_model = main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths()
            self.as_paths = temp_model.from_map(m.get('AsPaths'))

        if m.get('CenRouteMapRecords') is not None:
            temp_model = main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords()
            self.cen_route_map_records = temp_model.from_map(m.get('CenRouteMapRecords'))

        if m.get('Communities') is not None:
            temp_model = main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities()
            self.communities = temp_model.from_map(m.get('Communities'))

        if m.get('Conflicts') is not None:
            temp_model = main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflicts()
            self.conflicts = temp_model.from_map(m.get('Conflicts'))

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')

        if m.get('NextHopRegionId') is not None:
            self.next_hop_region_id = m.get('NextHopRegionId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('OperationalMode') is not None:
            self.operational_mode = m.get('OperationalMode')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflicts(DaraModel):
    def __init__(
        self,
        conflict: List[main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflictsConflict] = None,
    ):
        self.conflict = conflict

    def validate(self):
        if self.conflict:
            for v1 in self.conflict:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conflict'] = []
        if self.conflict is not None:
            for k1 in self.conflict:
                result['Conflict'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conflict = []
        if m.get('Conflict') is not None:
            for k1 in m.get('Conflict'):
                temp_model = main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflictsConflict()
                self.conflict.append(temp_model.from_map(k1))

        return self

class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflictsConflict(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.destination_cidr_block = destination_cidr_block
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities(DaraModel):
    def __init__(
        self,
        community: List[str] = None,
    ):
        self.community = community

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.community is not None:
            result['Community'] = self.community

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Community') is not None:
            self.community = m.get('Community')

        return self

class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords(DaraModel):
    def __init__(
        self,
        cen_route_map_record: List[main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord] = None,
    ):
        self.cen_route_map_record = cen_route_map_record

    def validate(self):
        if self.cen_route_map_record:
            for v1 in self.cen_route_map_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CenRouteMapRecord'] = []
        if self.cen_route_map_record is not None:
            for k1 in self.cen_route_map_record:
                result['CenRouteMapRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_route_map_record = []
        if m.get('CenRouteMapRecord') is not None:
            for k1 in m.get('CenRouteMapRecord'):
                temp_model = main_models.DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord()
                self.cen_route_map_record.append(temp_model.from_map(k1))

        return self

class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        route_map_id: str = None,
    ):
        self.region_id = region_id
        self.route_map_id = route_map_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        return self

class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths(DaraModel):
    def __init__(
        self,
        as_path: List[str] = None,
    ):
        self.as_path = as_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.as_path is not None:
            result['AsPath'] = self.as_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')

        return self

