# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeDatasetListResponseBody(DaraModel):
    def __init__(
        self,
        dataset_info_list: List[main_models.DescribeDatasetListResponseBodyDatasetInfoList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned dataset information. It is an array consisting of datasetinfo.
        self.dataset_info_list = dataset_info_list
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.dataset_info_list:
            for v1 in self.dataset_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatasetInfoList'] = []
        if self.dataset_info_list is not None:
            for k1 in self.dataset_info_list:
                result['DatasetInfoList'].append(k1.to_map() if k1 else None)

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
        self.dataset_info_list = []
        if m.get('DatasetInfoList') is not None:
            for k1 in m.get('DatasetInfoList'):
                temp_model = main_models.DescribeDatasetListResponseBodyDatasetInfoList()
                self.dataset_info_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDatasetListResponseBodyDatasetInfoList(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        dataset_id: str = None,
        dataset_name: str = None,
        dataset_type: str = None,
        description: str = None,
        modified_time: str = None,
        tags: List[main_models.DescribeDatasetListResponseBodyDatasetInfoListTags] = None,
    ):
        # The time when the dataset was created. The time is displayed in UTC.
        self.created_time = created_time
        # The dataset ID.
        self.dataset_id = dataset_id
        # The dataset name.
        self.dataset_name = dataset_name
        # The dataset type. Valid values:
        # 
        # *   JWT_BLOCKING : a JSON Web Token (JWT) blacklist
        # *   IP_WHITELIST_CIDR : an IP address whitelist
        # *   PARAMETER_ACCESS: a list of parameters for parameter-based access control
        self.dataset_type = dataset_type
        self.description = description
        # The time when the dataset was last modified. The time is displayed in UTC.
        self.modified_time = modified_time
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.description is not None:
            result['Description'] = self.description

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDatasetListResponseBodyDatasetInfoListTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeDatasetListResponseBodyDatasetInfoListTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
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

