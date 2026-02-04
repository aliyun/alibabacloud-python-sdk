# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeKvUsageDataRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        end_time: str = None,
        field: str = None,
        namespace_id: str = None,
        response_type: str = None,
        split_by: str = None,
        start_time: str = None,
    ):
        # The request method. If the parameter is empty, data about all methods is returned. Valid values:
        # 
        # *   **get**
        # *   **put**
        # *   **list**
        # *   **delete**
        self.access_type = access_type
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The type of the request data. Set the value to **acc**.
        # 
        # This parameter is required.
        self.field = field
        # The namespace ID. If the parameter is empty, data about all namespaces is returned.
        # 
        # You can specify a maximum number of 30 namespace IDs and separate them with commas (,).
        self.namespace_id = namespace_id
        # The type of the response data. Valid values:
        # 
        # *   **detail**: detailed data
        # *   **total**: summary data
        # 
        # Default value: **detail**.
        self.response_type = response_type
        # The key that is used to group data. Valid values: **type** and **namespace**.
        # 
        # *   **type**: Data is grouped by time. The data in the last 5 minutes is returned.
        # *   **namespace**: Data is grouped by namespace and is not padded with zeros.
        # *   Default value: **type**.
        # 
        # If **ResponseType** is set to **total**, data to return is not grouped by **namespace** but by **type**.
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # The minimum data granularity is 1 hour. If you do not specify this parameter, the data in the last seven days is returned.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.field is not None:
            result['Field'] = self.field

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.response_type is not None:
            result['ResponseType'] = self.response_type

        if self.split_by is not None:
            result['SplitBy'] = self.split_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('ResponseType') is not None:
            self.response_type = m.get('ResponseType')

        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

