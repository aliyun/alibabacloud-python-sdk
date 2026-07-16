# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeStageModelsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stage_model_info_list: List[main_models.DescribeStageModelsResponseBodyStageModelInfoList] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.stage_model_info_list = stage_model_info_list
        self.total_count = total_count

    def validate(self):
        if self.stage_model_info_list:
            for v1 in self.stage_model_info_list:
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StageModelInfoList'] = []
        if self.stage_model_info_list is not None:
            for k1 in self.stage_model_info_list:
                result['StageModelInfoList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stage_model_info_list = []
        if m.get('StageModelInfoList') is not None:
            for k1 in m.get('StageModelInfoList'):
                temp_model = main_models.DescribeStageModelsResponseBodyStageModelInfoList()
                self.stage_model_info_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeStageModelsResponseBodyStageModelInfoList(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        modified_time: str = None,
        stage_alias: str = None,
        stage_model_id: str = None,
        stage_name: str = None,
        type: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.modified_time = modified_time
        self.stage_alias = stage_alias
        self.stage_model_id = stage_model_id
        self.stage_name = stage_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.stage_alias is not None:
            result['StageAlias'] = self.stage_alias

        if self.stage_model_id is not None:
            result['StageModelId'] = self.stage_model_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('StageAlias') is not None:
            self.stage_alias = m.get('StageAlias')

        if m.get('StageModelId') is not None:
            self.stage_model_id = m.get('StageModelId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

