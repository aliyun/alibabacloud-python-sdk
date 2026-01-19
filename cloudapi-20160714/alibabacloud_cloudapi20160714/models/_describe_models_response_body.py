# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeModelsResponseBody(DaraModel):
    def __init__(
        self,
        model_details: main_models.DescribeModelsResponseBodyModelDetails = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned information about models. It is an array consisting of ModelDetail data.
        self.model_details = model_details
        # The page number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.model_details:
            self.model_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_details is not None:
            result['ModelDetails'] = self.model_details.to_map()

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
        if m.get('ModelDetails') is not None:
            temp_model = main_models.DescribeModelsResponseBodyModelDetails()
            self.model_details = temp_model.from_map(m.get('ModelDetails'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeModelsResponseBodyModelDetails(DaraModel):
    def __init__(
        self,
        model_detail: List[main_models.DescribeModelsResponseBodyModelDetailsModelDetail] = None,
    ):
        self.model_detail = model_detail

    def validate(self):
        if self.model_detail:
            for v1 in self.model_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModelDetail'] = []
        if self.model_detail is not None:
            for k1 in self.model_detail:
                result['ModelDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_detail = []
        if m.get('ModelDetail') is not None:
            for k1 in m.get('ModelDetail'):
                temp_model = main_models.DescribeModelsResponseBodyModelDetailsModelDetail()
                self.model_detail.append(temp_model.from_map(k1))

        return self

class DescribeModelsResponseBodyModelDetailsModelDetail(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        model_id: str = None,
        model_name: str = None,
        model_ref: str = None,
        modified_time: str = None,
        schema: str = None,
        tags: main_models.DescribeModelsResponseBodyModelDetailsModelDetailTags = None,
    ):
        # The time when the model was created.
        self.created_time = created_time
        # The description of the model definition.
        self.description = description
        # The ID of the API group to which the model belongs.
        self.group_id = group_id
        # The ID of the model.
        self.model_id = model_id
        # The name of the model.
        self.model_name = model_name
        # The URI of the model.
        self.model_ref = model_ref
        # The time when the model was last modified.
        self.modified_time = modified_time
        # The definition of the model.
        self.schema = schema
        # The tags of the model.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_ref is not None:
            result['ModelRef'] = self.model_ref

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelRef') is not None:
            self.model_ref = m.get('ModelRef')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeModelsResponseBodyModelDetailsModelDetailTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeModelsResponseBodyModelDetailsModelDetailTags(DaraModel):
    def __init__(
        self,
        tag_info: List[main_models.DescribeModelsResponseBodyModelDetailsModelDetailTagsTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for v1 in self.tag_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k1 in self.tag_info:
                result['TagInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k1 in m.get('TagInfo'):
                temp_model = main_models.DescribeModelsResponseBodyModelDetailsModelDetailTagsTagInfo()
                self.tag_info.append(temp_model.from_map(k1))

        return self

class DescribeModelsResponseBodyModelDetailsModelDetailTagsTagInfo(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

