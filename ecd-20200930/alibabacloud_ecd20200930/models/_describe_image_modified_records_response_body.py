# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeImageModifiedRecordsResponseBody(DaraModel):
    def __init__(
        self,
        image_modified_records: List[main_models.DescribeImageModifiedRecordsResponseBodyImageModifiedRecords] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The image change records.
        self.image_modified_records = image_modified_records
        # The pagination token for the next query. If NextToken is empty, no more results exist.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of image change records.
        self.total_count = total_count

    def validate(self):
        if self.image_modified_records:
            for v1 in self.image_modified_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageModifiedRecords'] = []
        if self.image_modified_records is not None:
            for k1 in self.image_modified_records:
                result['ImageModifiedRecords'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_modified_records = []
        if m.get('ImageModifiedRecords') is not None:
            for k1 in m.get('ImageModifiedRecords'):
                temp_model = main_models.DescribeImageModifiedRecordsResponseBodyImageModifiedRecords()
                self.image_modified_records.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImageModifiedRecordsResponseBodyImageModifiedRecords(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        new_image_id: str = None,
        new_image_name: str = None,
        reason: str = None,
        status: int = None,
        update_time: str = None,
    ):
        # The image ID before the change.
        self.image_id = image_id
        # The image name before the change.
        self.image_name = image_name
        # The ID of the new image after the change.
        self.new_image_id = new_image_id
        # The name of the new image after the change.
        self.new_image_name = new_image_name
        # The reason for ignoring the vulnerability. This parameter is required only when you perform the ignore vulnerability operation, that is, when `OperateType` is set to `vul_ignore`.
        self.reason = reason
        # The status of the image change.
        self.status = status
        # The time when the image was last changed. The time is in the ISO 8601 standard in UTC: yyyy-MM-ddTHH:mm:ss.SSSZ.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.new_image_id is not None:
            result['NewImageId'] = self.new_image_id

        if self.new_image_name is not None:
            result['NewImageName'] = self.new_image_name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('NewImageId') is not None:
            self.new_image_id = m.get('NewImageId')

        if m.get('NewImageName') is not None:
            self.new_image_name = m.get('NewImageName')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

