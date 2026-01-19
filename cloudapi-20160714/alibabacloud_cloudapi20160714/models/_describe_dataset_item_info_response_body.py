# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeDatasetItemInfoResponseBody(DaraModel):
    def __init__(
        self,
        dataset_item_info: main_models.DescribeDatasetItemInfoResponseBodyDatasetItemInfo = None,
        request_id: str = None,
    ):
        # The Dataset information.
        self.dataset_item_info = dataset_item_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dataset_item_info:
            self.dataset_item_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_item_info is not None:
            result['DatasetItemInfo'] = self.dataset_item_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetItemInfo') is not None:
            temp_model = main_models.DescribeDatasetItemInfoResponseBodyDatasetItemInfo()
            self.dataset_item_info = temp_model.from_map(m.get('DatasetItemInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDatasetItemInfoResponseBodyDatasetItemInfo(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        dataset_id: str = None,
        dataset_item_id: str = None,
        description: str = None,
        expired_time: str = None,
        modified_time: str = None,
        value: str = None,
    ):
        # The creation time (UTC) of the data entry.
        self.created_time = created_time
        # The ID of the dataset.
        self.dataset_id = dataset_id
        # The ID of the data entry.
        self.dataset_item_id = dataset_item_id
        # The description of the data entry.
        self.description = description
        # The time in UTC when the data entry expires. The time is in the **yyyy-MM-ddTHH:mm:ssZ** format. If this parameter is empty, the data entry does not expire.
        self.expired_time = expired_time
        # The last modification time (UTC) of the data entry.
        self.modified_time = modified_time
        # The value of the data entry.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_item_id is not None:
            result['DatasetItemId'] = self.dataset_item_id

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetItemId') is not None:
            self.dataset_item_id = m.get('DatasetItemId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

