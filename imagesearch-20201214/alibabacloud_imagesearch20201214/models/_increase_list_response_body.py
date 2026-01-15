# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imagesearch20201214 import models as main_models
from darabonba.model import DaraModel

class IncreaseListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.IncreaseListResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the batch task.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.IncreaseListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class IncreaseListResponseBodyData(DaraModel):
    def __init__(
        self,
        increments: main_models.IncreaseListResponseBodyDataIncrements = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # A list of batch tasks.
        self.increments = increments
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The total number of tasks.
        self.total_count = total_count

    def validate(self):
        if self.increments:
            self.increments.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.increments is not None:
            result['Increments'] = self.increments.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Increments') is not None:
            temp_model = main_models.IncreaseListResponseBodyDataIncrements()
            self.increments = temp_model.from_map(m.get('Increments'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class IncreaseListResponseBodyDataIncrements(DaraModel):
    def __init__(
        self,
        instance: List[main_models.IncreaseListResponseBodyDataIncrementsInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.IncreaseListResponseBodyDataIncrementsInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class IncreaseListResponseBodyDataIncrementsInstance(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        callback_address: str = None,
        code: str = None,
        error_url: str = None,
        id: int = None,
        msg: str = None,
        path: str = None,
        status: str = None,
        utc_create: str = None,
        utc_modified: int = None,
    ):
        # The name of the Object Storage Service (OSS) bucket.
        self.bucket_name = bucket_name
        # The callback address.
        self.callback_address = callback_address
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code
        # The address where you can download the result. The address is valid for 2 hours.
        self.error_url = error_url
        # The ID of the task.
        self.id = id
        # The error message returned.
        self.msg = msg
        # The absolute path to the increment.meta file in the bucket. The path must start with a forward slash (/) and cannot end with a forward slash (/).
        self.path = path
        # The status of the batch task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.status = status
        # The time when the task was created. Unit: milliseconds.
        self.utc_create = utc_create
        # The time when the task was updated. Unit: milliseconds.
        self.utc_modified = utc_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address

        if self.code is not None:
            result['Code'] = self.code

        if self.error_url is not None:
            result['ErrorUrl'] = self.error_url

        if self.id is not None:
            result['Id'] = self.id

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.path is not None:
            result['Path'] = self.path

        if self.status is not None:
            result['Status'] = self.status

        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create

        if self.utc_modified is not None:
            result['UtcModified'] = self.utc_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorUrl') is not None:
            self.error_url = m.get('ErrorUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')

        if m.get('UtcModified') is not None:
            self.utc_modified = m.get('UtcModified')

        return self

