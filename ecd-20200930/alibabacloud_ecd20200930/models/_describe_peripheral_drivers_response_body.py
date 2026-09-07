# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribePeripheralDriversResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        driver_infos: List[main_models.DescribePeripheralDriversResponseBodyDriverInfos] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The total number of matching drivers, not the length of the current page list. This value may be 0 when the current page contains no data.
        self.count = count
        # The list of driver information on the current page. An empty list is returned when no data is available.
        self.driver_infos = driver_infos
        # Reserved field. This field does not provide a valid return value and may not be returned. This operation uses PageSize and PageNumber for pagination. Do not rely on this field. The example value 20 is provided only to illustrate the integer type and does not represent the actual return value, default value, or page size of this operation.
        self.max_results = max_results
        # Reserved field. Token-based pagination is not supported and this field may not be returned. Do not rely on this field for continued queries. The example value token-for-format-only is provided only to illustrate the string type and is not an actual return value or a usable pagination token.
        self.next_token = next_token
        # The request ID. Provide this value when troubleshooting issues.
        self.request_id = request_id

    def validate(self):
        if self.driver_infos:
            for v1 in self.driver_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['DriverInfos'] = []
        if self.driver_infos is not None:
            for k1 in self.driver_infos:
                result['DriverInfos'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.driver_infos = []
        if m.get('DriverInfos') is not None:
            for k1 in m.get('DriverInfos'):
                temp_model = main_models.DescribePeripheralDriversResponseBodyDriverInfos()
                self.driver_infos.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePeripheralDriversResponseBodyDriverInfos(DaraModel):
    def __init__(
        self,
        brand: str = None,
        create_time: str = None,
        device_type: str = None,
        icon: str = None,
        id: str = None,
        name: str = None,
        os_type: str = None,
        owner_type: str = None,
        source: str = None,
    ):
        # The brand to which the driver belongs.
        self.brand = brand
        # The time when the driver record was created, in ISO 8601 (RFC 3339) format with a time zone offset. The time zone offset is based on the returned value. This field may be empty or not returned if the time information does not exist.
        self.create_time = create_time
        # The device type to which the driver applies.
        self.device_type = device_type
        # The brand icon URL. This field may be empty or not returned if no icon is configured. The example value is for illustration purposes only.
        self.icon = icon
        # The driver ID, which can be used for subsequent queries.
        self.id = id
        # The driver name.
        self.name = name
        # The operating system to which the driver applies, such as Windows. The actual returned value prevails.
        self.os_type = os_type
        # The driver ownership. Valid values:
        # - WUYING: Wuying official driver.
        # - CUSTOMER: Custom driver of the current account.
        self.owner_type = owner_type
        # The driver source. Valid values:
        # - OpsApp: Uploaded from the management console.
        # - WuyingHelper: Uploaded from Wuying Helper.
        # - Wuying: Wuying source.
        # 
        # Unrecognized sources may also be classified as Wuying. To distinguish between official and custom drivers, use OwnerType.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand is not None:
            result['Brand'] = self.brand

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

