# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListCrossProjectPipelineRunItemsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListCrossProjectPipelineRunItemsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business response.
        self.data = data
        # The request ID, which is used to locate and troubleshoot this API call.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListCrossProjectPipelineRunItemsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCrossProjectPipelineRunItemsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pipeline_run_items: List[main_models.ListCrossProjectPipelineRunItemsResponseBodyDataPipelineRunItems] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of publish items for the root objects and their child objects that are included in the cross-workspace publish pipeline.
        self.pipeline_run_items = pipeline_run_items
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.pipeline_run_items:
            for v1 in self.pipeline_run_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PipelineRunItems'] = []
        if self.pipeline_run_items is not None:
            for k1 in self.pipeline_run_items:
                result['PipelineRunItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.pipeline_run_items = []
        if m.get('PipelineRunItems') is not None:
            for k1 in m.get('PipelineRunItems'):
                temp_model = main_models.ListCrossProjectPipelineRunItemsResponseBodyDataPipelineRunItems()
                self.pipeline_run_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCrossProjectPipelineRunItemsResponseBodyDataPipelineRunItems(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        error_code: str = None,
        error_message: str = None,
        is_root: bool = None,
        object_id: str = None,
        object_name: str = None,
        object_type: str = None,
        object_version: str = None,
        parent_object_id: str = None,
        status: str = None,
    ):
        # The change type.
        self.change_type = change_type
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # Indicates whether the object is a root object.
        self.is_root = is_root
        # The ID of the publish object.
        self.object_id = object_id
        # The name of the publish object.
        self.object_name = object_name
        # The object type of the publish object.
        self.object_type = object_type
        # The version of the publish object.
        self.object_version = object_version
        # The ID of the parent object.
        self.parent_object_id = parent_object_id
        # The status of the publish item.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.is_root is not None:
            result['IsRoot'] = self.is_root

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.object_version is not None:
            result['ObjectVersion'] = self.object_version

        if self.parent_object_id is not None:
            result['ParentObjectId'] = self.parent_object_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('IsRoot') is not None:
            self.is_root = m.get('IsRoot')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('ObjectVersion') is not None:
            self.object_version = m.get('ObjectVersion')

        if m.get('ParentObjectId') is not None:
            self.parent_object_id = m.get('ParentObjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

