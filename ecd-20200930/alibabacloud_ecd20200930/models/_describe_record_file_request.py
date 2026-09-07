# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecordFileRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        end_time: str = None,
        end_user_id: str = None,
        file_name: str = None,
        order_by: str = None,
        order_sort: str = None,
        page_number: int = None,
        page_size: int = None,
        record_type: str = None,
        region_id: str = None,
        resource_type: str = None,
        start_time: str = None,
        status: int = None,
    ):
        # The Cloud Desktop ID.
        self.desktop_id = desktop_id
        # The end time of the query. Format: yyyyMMddHHmmss.
        self.end_time = end_time
        # The ID of the end user.
        self.end_user_id = end_user_id
        # The name of the recording file.
        self.file_name = file_name
        # The field used for sorting. If this parameter is not specified, the results are sorted by recording start time in descending order. Valid values:
        # 
        # - startTime: recording start time.
        self.order_by = order_by
        # The sort order. Valid values:
        # 
        # - asc: ascending order.
        # - desc: descending order.
        self.order_sort = order_sort
        # The page number.
        self.page_number = page_number
        # The maximum number of rows per page in a paging query.
        self.page_size = page_size
        # The type of the screen recording file. Valid values:
        # 
        # - alltime: full-time recording.
        # - period: interval recording.
        # - event: event-based recording.
        # - session: session recording.
        self.record_type = record_type
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource type.
        self.resource_type = resource_type
        # The start time of the query. Format: yyyyMMddHHmmss.
        self.start_time = start_time
        # The status of the screen recording file. Valid values:
        # 
        # - 0: uploaded.
        # - 1: uploading.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_sort is not None:
            result['OrderSort'] = self.order_sort

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderSort') is not None:
            self.order_sort = m.get('OrderSort')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

