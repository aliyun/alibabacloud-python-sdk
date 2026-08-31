# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeCpfsAccessPointsResponseBody(DaraModel):
    def __init__(
        self,
        access_points: List[main_models.DescribeCpfsAccessPointsResponseBodyAccessPoints] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The access point information.
        self.access_points = access_points
        # The page number of the list.
        self.page_number = page_number
        # The number of results per page.
        # Valid values: 1 to 100.                              
        # Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of access points.
        self.total_count = total_count

    def validate(self):
        if self.access_points:
            for v1 in self.access_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessPoints'] = []
        if self.access_points is not None:
            for k1 in self.access_points:
                result['AccessPoints'].append(k1.to_map() if k1 else None)

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
        self.access_points = []
        if m.get('AccessPoints') is not None:
            for k1 in m.get('AccessPoints'):
                temp_model = main_models.DescribeCpfsAccessPointsResponseBodyAccessPoints()
                self.access_points.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCpfsAccessPointsResponseBodyAccessPoints(DaraModel):
    def __init__(
        self,
        arn: str = None,
        access_point_id: str = None,
        create_time: str = None,
        description: str = None,
        file_system_id: str = None,
        modify_time: str = None,
        region_id: str = None,
        root_directory: main_models.DescribeCpfsAccessPointsResponseBodyAccessPointsRootDirectory = None,
        status: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the access point.
        self.arn = arn
        # The access point ID.
        self.access_point_id = access_point_id
        # The time when the access point was created. The time follows the ISO 8601 standard in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # The description of the access point.
        self.description = description
        # The file system ID.
        self.file_system_id = file_system_id
        # The time when the access point was last modified. The time follows the ISO 8601 standard in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.modify_time = modify_time
        # The region ID.
        self.region_id = region_id
        # The root directory information.
        self.root_directory = root_directory
        # The current status of the access point.
        # 
        # Valid values:
        # 
        # - Active: available
        # - Inactive: unavailable
        # - Pending: being created
        # - Deleting: being deleted
        # 
        # > The file system can be mounted only when the status is Active.
        self.status = status

    def validate(self):
        if self.root_directory:
            self.root_directory.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['ARN'] = self.arn

        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.root_directory is not None:
            result['RootDirectory'] = self.root_directory.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ARN') is not None:
            self.arn = m.get('ARN')

        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RootDirectory') is not None:
            temp_model = main_models.DescribeCpfsAccessPointsResponseBodyAccessPointsRootDirectory()
            self.root_directory = temp_model.from_map(m.get('RootDirectory'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeCpfsAccessPointsResponseBodyAccessPointsRootDirectory(DaraModel):
    def __init__(
        self,
        root_path: str = None,
        root_path_status: str = None,
    ):
        # The root directory.
        self.root_path = root_path
        # The current status of the root directory.
        # 
        # Valid values:
        # 
        # - Unknown: The root path status is unknown.
        # - NotExist: The root path does not exist. It may have been deleted by the user.
        # - Ready: The root path status is normal.
        self.root_path_status = root_path_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.root_path is not None:
            result['RootPath'] = self.root_path

        if self.root_path_status is not None:
            result['RootPathStatus'] = self.root_path_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RootPath') is not None:
            self.root_path = m.get('RootPath')

        if m.get('RootPathStatus') is not None:
            self.root_path_status = m.get('RootPathStatus')

        return self

