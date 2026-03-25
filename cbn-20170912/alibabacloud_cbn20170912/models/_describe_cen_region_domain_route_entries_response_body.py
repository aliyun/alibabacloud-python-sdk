# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenRegionDomainRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        cen_route_entries: main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cen_route_entries = cen_route_entries
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
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
            temp_model = main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries()
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

class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries(DaraModel):
    def __init__(
        self,
        cen_route_entry: List[main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry] = None,
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
                temp_model = main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry()
                self.cen_route_entry.append(temp_model.from_map(k1))

        return self

class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry(DaraModel):
    def __init__(
        self,
        as_paths: main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths = None,
        cen_out_route_map_records: main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecords = None,
        cen_route_map_records: main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords = None,
        communities: main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities = None,
        destination_cidr_block: str = None,
        next_hop_instance_id: str = None,
        next_hop_region_id: str = None,
        next_hop_type: str = None,
        preference: int = None,
        status: str = None,
        to_other_region_status: str = None,
        type: str = None,
    ):
        self.as_paths = as_paths
        self.cen_out_route_map_records = cen_out_route_map_records
        self.cen_route_map_records = cen_route_map_records
        self.communities = communities
        self.destination_cidr_block = destination_cidr_block
        self.next_hop_instance_id = next_hop_instance_id
        self.next_hop_region_id = next_hop_region_id
        self.next_hop_type = next_hop_type
        self.preference = preference
        self.status = status
        self.to_other_region_status = to_other_region_status
        self.type = type

    def validate(self):
        if self.as_paths:
            self.as_paths.validate()
        if self.cen_out_route_map_records:
            self.cen_out_route_map_records.validate()
        if self.cen_route_map_records:
            self.cen_route_map_records.validate()
        if self.communities:
            self.communities.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.as_paths is not None:
            result['AsPaths'] = self.as_paths.to_map()

        if self.cen_out_route_map_records is not None:
            result['CenOutRouteMapRecords'] = self.cen_out_route_map_records.to_map()

        if self.cen_route_map_records is not None:
            result['CenRouteMapRecords'] = self.cen_route_map_records.to_map()

        if self.communities is not None:
            result['Communities'] = self.communities.to_map()

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id

        if self.next_hop_region_id is not None:
            result['NextHopRegionId'] = self.next_hop_region_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.preference is not None:
            result['Preference'] = self.preference

        if self.status is not None:
            result['Status'] = self.status

        if self.to_other_region_status is not None:
            result['ToOtherRegionStatus'] = self.to_other_region_status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPaths') is not None:
            temp_model = main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths()
            self.as_paths = temp_model.from_map(m.get('AsPaths'))

        if m.get('CenOutRouteMapRecords') is not None:
            temp_model = main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecords()
            self.cen_out_route_map_records = temp_model.from_map(m.get('CenOutRouteMapRecords'))

        if m.get('CenRouteMapRecords') is not None:
            temp_model = main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords()
            self.cen_route_map_records = temp_model.from_map(m.get('CenRouteMapRecords'))

        if m.get('Communities') is not None:
            temp_model = main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities()
            self.communities = temp_model.from_map(m.get('Communities'))

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')

        if m.get('NextHopRegionId') is not None:
            self.next_hop_region_id = m.get('NextHopRegionId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('Preference') is not None:
            self.preference = m.get('Preference')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ToOtherRegionStatus') is not None:
            self.to_other_region_status = m.get('ToOtherRegionStatus')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities(DaraModel):
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

class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords(DaraModel):
    def __init__(
        self,
        cen_route_map_record: List[main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord] = None,
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
                temp_model = main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord()
                self.cen_route_map_record.append(temp_model.from_map(k1))

        return self

class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord(DaraModel):
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

class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecords(DaraModel):
    def __init__(
        self,
        cen_out_route_map_record: List[main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecordsCenOutRouteMapRecord] = None,
    ):
        self.cen_out_route_map_record = cen_out_route_map_record

    def validate(self):
        if self.cen_out_route_map_record:
            for v1 in self.cen_out_route_map_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CenOutRouteMapRecord'] = []
        if self.cen_out_route_map_record is not None:
            for k1 in self.cen_out_route_map_record:
                result['CenOutRouteMapRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_out_route_map_record = []
        if m.get('CenOutRouteMapRecord') is not None:
            for k1 in m.get('CenOutRouteMapRecord'):
                temp_model = main_models.DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecordsCenOutRouteMapRecord()
                self.cen_out_route_map_record.append(temp_model.from_map(k1))

        return self

class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecordsCenOutRouteMapRecord(DaraModel):
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

class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths(DaraModel):
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

