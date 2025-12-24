# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeCensResponseBody(DaraModel):
    def __init__(
        self,
        cens: List[main_models.DescribeCensResponseBodyCens] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the CEN instances.
        self.cens = cens
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of CEN instances returned.
        self.total_count = total_count

    def validate(self):
        if self.cens:
            for v1 in self.cens:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cens'] = []
        if self.cens is not None:
            for k1 in self.cens:
                result['Cens'].append(k1.to_map() if k1 else None)

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
        self.cens = []
        if m.get('Cens') is not None:
            for k1 in m.get('Cens'):
                temp_model = main_models.DescribeCensResponseBodyCens()
                self.cens.append(temp_model.from_map(k1))

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
        cen_id: str = None,
        creation_time: str = None,
        description: str = None,
        ipv_6level: str = None,
        name: str = None,
        package_ids: List[main_models.DescribeCensResponseBodyCensPackageIds] = None,
        protection_level: str = None,
        status: str = None,
        tags: List[main_models.DescribeCensResponseBodyCensTags] = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The time when the CEN instance was created.
        self.creation_time = creation_time
        # The description of the CEN instance.
        self.description = description
        # The IPv6 level.
        # 
        # >  IPv6 is not supported.
        # 
        # Valid value:
        # 
        # *   DISABLED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.ipv_6level = ipv_6level
        # The name of the CEN instance.
        self.name = name
        # The bandwidth plans that are bound to the CEN instance.
        self.package_ids = package_ids
        # The tolerated level of CIDR block conflict.
        # 
        # Valid value:
        # 
        # *   REDUCED: CIDR block conflicts are allowed, but the conflicting CIDR blocks cannot be identical.
        self.protection_level = protection_level
        # The status of the CEN instance.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Active
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The tags of the CEN instance.
        self.tags = tags

    def validate(self):
        if self.package_ids:
            for v1 in self.package_ids:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        result['PackageIds'] = []
        if self.package_ids is not None:
            for k1 in self.package_ids:
                result['PackageIds'].append(k1.to_map() if k1 else None)

        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        self.package_ids = []
        if m.get('PackageIds') is not None:
            for k1 in m.get('PackageIds'):
                temp_model = main_models.DescribeCensResponseBodyCensPackageIds()
                self.package_ids.append(temp_model.from_map(k1))

        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeCensResponseBodyCensTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeCensResponseBodyCensTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

class DescribeCensResponseBodyCensPackageIds(DaraModel):
    def __init__(
        self,
        package_id: str = None,
    ):
        # The ID of the bandwidth plan that is bound to the CEN instance.
        self.package_id = package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.package_id is not None:
            result['PackageId'] = self.package_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        return self

