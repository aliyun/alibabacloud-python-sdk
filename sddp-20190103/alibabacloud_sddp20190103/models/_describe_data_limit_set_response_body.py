# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeDataLimitSetResponseBody(DaraModel):
    def __init__(
        self,
        data_limit_set: main_models.DescribeDataLimitSetResponseBodyDataLimitSet = None,
        request_id: str = None,
    ):
        # The information about the data asset.
        self.data_limit_set = data_limit_set
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data_limit_set:
            self.data_limit_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_limit_set is not None:
            result['DataLimitSet'] = self.data_limit_set.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLimitSet') is not None:
            temp_model = main_models.DescribeDataLimitSetResponseBodyDataLimitSet()
            self.data_limit_set = temp_model.from_map(m.get('DataLimitSet'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDataLimitSetResponseBodyDataLimitSet(DaraModel):
    def __init__(
        self,
        data_limit_list: List[main_models.DescribeDataLimitSetResponseBodyDataLimitSetDataLimitList] = None,
        oss_bucket_list: List[main_models.DescribeDataLimitSetResponseBodyDataLimitSetOssBucketList] = None,
        region_list: List[main_models.DescribeDataLimitSetResponseBodyDataLimitSetRegionList] = None,
        resource_type: int = None,
        resource_type_code: str = None,
        total_count: int = None,
    ):
        # An array that consists of data assets that DSC is authorized to scan.
        self.data_limit_list = data_limit_list
        # An array consisting of the OSS objects that DSC is authorized to scan.
        self.oss_bucket_list = oss_bucket_list
        # An array consisting of the regions in which the data assets can be scanned.
        self.region_list = region_list
        # The type of service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        self.resource_type = resource_type
        # The service to which the data asset belongs. Valid values:
        # 
        # *   **ODPS**
        # *   **OSS**
        # *   **ADS**
        # *   **OTS**
        # *   **RDS**
        self.resource_type_code = resource_type_code
        # The total number of data objects in the data assets.
        self.total_count = total_count

    def validate(self):
        if self.data_limit_list:
            for v1 in self.data_limit_list:
                 if v1:
                    v1.validate()
        if self.oss_bucket_list:
            for v1 in self.oss_bucket_list:
                 if v1:
                    v1.validate()
        if self.region_list:
            for v1 in self.region_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataLimitList'] = []
        if self.data_limit_list is not None:
            for k1 in self.data_limit_list:
                result['DataLimitList'].append(k1.to_map() if k1 else None)

        result['OssBucketList'] = []
        if self.oss_bucket_list is not None:
            for k1 in self.oss_bucket_list:
                result['OssBucketList'].append(k1.to_map() if k1 else None)

        result['RegionList'] = []
        if self.region_list is not None:
            for k1 in self.region_list:
                result['RegionList'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_limit_list = []
        if m.get('DataLimitList') is not None:
            for k1 in m.get('DataLimitList'):
                temp_model = main_models.DescribeDataLimitSetResponseBodyDataLimitSetDataLimitList()
                self.data_limit_list.append(temp_model.from_map(k1))

        self.oss_bucket_list = []
        if m.get('OssBucketList') is not None:
            for k1 in m.get('OssBucketList'):
                temp_model = main_models.DescribeDataLimitSetResponseBodyDataLimitSetOssBucketList()
                self.oss_bucket_list.append(temp_model.from_map(k1))

        self.region_list = []
        if m.get('RegionList') is not None:
            for k1 in m.get('RegionList'):
                temp_model = main_models.DescribeDataLimitSetResponseBodyDataLimitSetRegionList()
                self.region_list.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataLimitSetResponseBodyDataLimitSetRegionList(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        # The name of the region.
        self.local_name = local_name
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeDataLimitSetResponseBodyDataLimitSetOssBucketList(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        region_id: str = None,
    ):
        # The name of the OSS bucket to which the OSS object belongs.
        self.bucket_name = bucket_name
        # The region ID of the OSS object.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeDataLimitSetResponseBodyDataLimitSetDataLimitList(DaraModel):
    def __init__(
        self,
        check_status: int = None,
        check_status_name: str = None,
        connector: str = None,
        gmt_create: int = None,
        id: int = None,
        local_name: str = None,
        parent_id: str = None,
        region_id: str = None,
        resource_type: int = None,
        resource_type_code: str = None,
        user_name: str = None,
    ):
        # Indicates whether the test of connectivity between DSC and the data asset is passed.
        # 
        # *   **2**: The connectivity test is in progress.
        # *   **3**: The connectivity test is passed.
        # *   **4**: The connectivity test failed.
        self.check_status = check_status
        # The name of the data detection status.
        self.check_status_name = check_status_name
        # The connection string that is used to access the data asset.
        self.connector = connector
        # The time when the data asset was created. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The ID of the data asset.
        self.id = id
        # The region in which the data asset resides.
        self.local_name = local_name
        # The parent asset ID of the data asset.
        self.parent_id = parent_id
        # The region in which the data asset resides.
        self.region_id = region_id
        # The type of service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        self.resource_type = resource_type
        # The code of the service to which the data asset belongs. Valid values:
        # 
        # *   **ODPS**
        # *   **OSS**
        # *   **ADS**
        # *   **OTS**
        # *   **RDS**
        self.resource_type_code = resource_type_code
        # The username that is used to access the data asset.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.check_status_name is not None:
            result['CheckStatusName'] = self.check_status_name

        if self.connector is not None:
            result['Connector'] = self.connector

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('CheckStatusName') is not None:
            self.check_status_name = m.get('CheckStatusName')

        if m.get('Connector') is not None:
            self.connector = m.get('Connector')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

