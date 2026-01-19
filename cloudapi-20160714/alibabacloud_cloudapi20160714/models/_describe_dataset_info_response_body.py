# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeDatasetInfoResponseBody(DaraModel):
    def __init__(
        self,
        dataset_info: main_models.DescribeDatasetInfoResponseBodyDatasetInfo = None,
        request_id: str = None,
    ):
        # The dataset info.
        self.dataset_info = dataset_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dataset_info:
            self.dataset_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_info is not None:
            result['DatasetInfo'] = self.dataset_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetInfo') is not None:
            temp_model = main_models.DescribeDatasetInfoResponseBodyDatasetInfo()
            self.dataset_info = temp_model.from_map(m.get('DatasetInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDatasetInfoResponseBodyDatasetInfo(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        dataset_id: str = None,
        dataset_name: str = None,
        dataset_type: str = None,
        description: str = None,
        modified_time: str = None,
    ):
        # The creation time (UTC) of the dataset.
        self.created_time = created_time
        # The ID of the dataset.
        self.dataset_id = dataset_id
        # The name of the dataset.
        self.dataset_name = dataset_name
        # The type of the dataset. Valid values:
        # 
        # *   JWT_BLOCKING: a JSON Web Token (JWT) blacklist
        # *   IP_WHITELIST_CIDR : an IP address whitelist
        # *   PARAMETER_ACCESS : parameter-based access control
        self.dataset_type = dataset_type
        self.description = description
        # The last modification time (UTC) of the dataset.
        self.modified_time = modified_time

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

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.description is not None:
            result['Description'] = self.description

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

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

        return self

