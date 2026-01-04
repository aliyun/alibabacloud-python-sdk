# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeEipSegmentResponseBody(DaraModel):
    def __init__(
        self,
        eip_segments: main_models.DescribeEipSegmentResponseBodyEipSegments = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the contiguous EIP group.
        self.eip_segments = eip_segments
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.eip_segments:
            self.eip_segments.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_segments is not None:
            result['EipSegments'] = self.eip_segments.to_map()

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
        if m.get('EipSegments') is not None:
            temp_model = main_models.DescribeEipSegmentResponseBodyEipSegments()
            self.eip_segments = temp_model.from_map(m.get('EipSegments'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEipSegmentResponseBodyEipSegments(DaraModel):
    def __init__(
        self,
        eip_segment: List[main_models.DescribeEipSegmentResponseBodyEipSegmentsEipSegment] = None,
    ):
        self.eip_segment = eip_segment

    def validate(self):
        if self.eip_segment:
            for v1 in self.eip_segment:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EipSegment'] = []
        if self.eip_segment is not None:
            for k1 in self.eip_segment:
                result['EipSegment'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_segment = []
        if m.get('EipSegment') is not None:
            for k1 in m.get('EipSegment'):
                temp_model = main_models.DescribeEipSegmentResponseBodyEipSegmentsEipSegment()
                self.eip_segment.append(temp_model.from_map(k1))

        return self

class DescribeEipSegmentResponseBodyEipSegmentsEipSegment(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        descritpion: str = None,
        instance_id: str = None,
        ip_count: str = None,
        name: str = None,
        region_id: str = None,
        segment: str = None,
        status: str = None,
        zone: str = None,
    ):
        # The time when the contiguous EIP group was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the contiguous EIP group.
        self.descritpion = descritpion
        # The ID of the contiguous EIP group.
        self.instance_id = instance_id
        # The number of EIPs in the contiguous EIP group.
        self.ip_count = ip_count
        # The name of the contiguous EIP group.
        self.name = name
        # The ID of the region to which the contiguous EIP group belongs.
        self.region_id = region_id
        # The CIDR block and mask of the contiguous EIP group.
        self.segment = segment
        # The status of the contiguous EIP group. Valid values:
        # 
        # *   **Allocating**
        # *   **Allocated**
        # *   **Releasing**
        self.status = status
        # The zone of the contiguous EIP group.
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.descritpion is not None:
            result['Descritpion'] = self.descritpion

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_count is not None:
            result['IpCount'] = self.ip_count

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.segment is not None:
            result['Segment'] = self.segment

        if self.status is not None:
            result['Status'] = self.status

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Descritpion') is not None:
            self.descritpion = m.get('Descritpion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Segment') is not None:
            self.segment = m.get('Segment')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

