# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeBucketsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeBucketsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeBucketsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeBucketsResponseBodyData(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        extranet_endpoint: str = None,
        gmt_created: str = None,
        intranet_endpoint: str = None,
        location: str = None,
        oss_object_list: List[main_models.DescribeBucketsResponseBodyDataOssObjectList] = None,
        region_id: str = None,
    ):
        self.bucket_name = bucket_name
        self.extranet_endpoint = extranet_endpoint
        self.gmt_created = gmt_created
        self.intranet_endpoint = intranet_endpoint
        self.location = location
        self.oss_object_list = oss_object_list
        self.region_id = region_id

    def validate(self):
        if self.oss_object_list:
            for v1 in self.oss_object_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.extranet_endpoint is not None:
            result['ExtranetEndpoint'] = self.extranet_endpoint

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint

        if self.location is not None:
            result['Location'] = self.location

        result['OssObjectList'] = []
        if self.oss_object_list is not None:
            for k1 in self.oss_object_list:
                result['OssObjectList'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('ExtranetEndpoint') is not None:
            self.extranet_endpoint = m.get('ExtranetEndpoint')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        self.oss_object_list = []
        if m.get('OssObjectList') is not None:
            for k1 in m.get('OssObjectList'):
                temp_model = main_models.DescribeBucketsResponseBodyDataOssObjectList()
                self.oss_object_list.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeBucketsResponseBodyDataOssObjectList(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        etag: str = None,
        key: str = None,
        last_modified: str = None,
        owner: main_models.DescribeBucketsResponseBodyDataOssObjectListOwner = None,
        restore_info: str = None,
        size: int = None,
        storage_class: str = None,
        type: str = None,
    ):
        self.bucket_name = bucket_name
        self.etag = etag
        self.key = key
        self.last_modified = last_modified
        self.owner = owner
        self.restore_info = restore_info
        self.size = size
        self.storage_class = storage_class
        self.type = type

    def validate(self):
        if self.owner:
            self.owner.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.etag is not None:
            result['ETag'] = self.etag

        if self.key is not None:
            result['Key'] = self.key

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.owner is not None:
            result['Owner'] = self.owner.to_map()

        if self.restore_info is not None:
            result['RestoreInfo'] = self.restore_info

        if self.size is not None:
            result['Size'] = self.size

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('ETag') is not None:
            self.etag = m.get('ETag')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('Owner') is not None:
            temp_model = main_models.DescribeBucketsResponseBodyDataOssObjectListOwner()
            self.owner = temp_model.from_map(m.get('Owner'))

        if m.get('RestoreInfo') is not None:
            self.restore_info = m.get('RestoreInfo')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeBucketsResponseBodyDataOssObjectListOwner(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
    ):
        self.display_name = display_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

