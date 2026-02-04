# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCensResponseBody(DaraModel):
    def __init__(
        self,
        cens: main_models.DescribeCensResponseBodyCens = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the CEN instance.
        self.cens = cens
        # The number of the page returned.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cens:
            self.cens.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cens is not None:
            result['Cens'] = self.cens.to_map()

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
        if m.get('Cens') is not None:
            temp_model = main_models.DescribeCensResponseBodyCens()
            self.cens = temp_model.from_map(m.get('Cens'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCensResponseBodyCens(DaraModel):
    def __init__(
        self,
        cen: List[main_models.DescribeCensResponseBodyCensCen] = None,
    ):
        self.cen = cen

    def validate(self):
        if self.cen:
            for v1 in self.cen:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cen'] = []
        if self.cen is not None:
            for k1 in self.cen:
                result['Cen'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen = []
        if m.get('Cen') is not None:
            for k1 in m.get('Cen'):
                temp_model = main_models.DescribeCensResponseBodyCensCen()
                self.cen.append(temp_model.from_map(k1))

        return self

class DescribeCensResponseBodyCensCen(DaraModel):
    def __init__(
        self,
        cen_bandwidth_package_ids: main_models.DescribeCensResponseBodyCensCenCenBandwidthPackageIds = None,
        cen_id: str = None,
        creation_time: str = None,
        description: str = None,
        ipv_6level: str = None,
        name: str = None,
        protection_level: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: main_models.DescribeCensResponseBodyCensCenTags = None,
    ):
        # The IDs of the bandwidth plans that are associated with the CEN instance.
        self.cen_bandwidth_package_ids = cen_bandwidth_package_ids
        # The CEN instance ID.
        self.cen_id = cen_id
        # The time when the CEN instance was created.
        # 
        # The time follows the ISO8601 standard in the `YYYY-MM-DDThh:mmZ` format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the CEN instance.
        self.description = description
        # Indicates whether IPv6 is enabled for the CEN instance.
        # 
        # *   **ENABLE**
        # *   **DISABLED**
        self.ipv_6level = ipv_6level
        # The CEN instance name.
        self.name = name
        # The level of CIDR block overlapping.
        # 
        # **REDUCED**: Overlapped CIDR blocks are allowed. This value specifies that CIDR blocks can overlap but CIDR blocks cannot be duplicates.
        self.protection_level = protection_level
        # The ID of the resource group to which the CEN instance belongs.
        self.resource_group_id = resource_group_id
        # The status of the CEN instance.
        # 
        # *   **Creating**
        # *   **Active**
        # *   **Deleting**
        self.status = status
        # The IDs of the tags that are added to the CEN instance.
        self.tags = tags

    def validate(self):
        if self.cen_bandwidth_package_ids:
            self.cen_bandwidth_package_ids.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_bandwidth_package_ids is not None:
            result['CenBandwidthPackageIds'] = self.cen_bandwidth_package_ids.to_map()

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ipv_6level is not None:
            result['Ipv6Level'] = self.ipv_6level

        if self.name is not None:
            result['Name'] = self.name

        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenBandwidthPackageIds') is not None:
            temp_model = main_models.DescribeCensResponseBodyCensCenCenBandwidthPackageIds()
            self.cen_bandwidth_package_ids = temp_model.from_map(m.get('CenBandwidthPackageIds'))

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Ipv6Level') is not None:
            self.ipv_6level = m.get('Ipv6Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeCensResponseBodyCensCenTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeCensResponseBodyCensCenTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeCensResponseBodyCensCenTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeCensResponseBodyCensCenTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCensResponseBodyCensCenTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeCensResponseBodyCensCenCenBandwidthPackageIds(DaraModel):
    def __init__(
        self,
        cen_bandwidth_package_id: List[str] = None,
    ):
        self.cen_bandwidth_package_id = cen_bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')

        return self

