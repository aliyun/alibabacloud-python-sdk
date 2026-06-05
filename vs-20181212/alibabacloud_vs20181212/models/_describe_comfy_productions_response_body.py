# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeComfyProductionsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        productions: List[main_models.DescribeComfyProductionsResponseBodyProductions] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.productions = productions
        # Id of the request
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.productions:
            for v1 in self.productions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Productions'] = []
        if self.productions is not None:
            for k1 in self.productions:
                result['Productions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.productions = []
        if m.get('Productions') is not None:
            for k1 in m.get('Productions'):
                temp_model = main_models.DescribeComfyProductionsResponseBodyProductions()
                self.productions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeComfyProductionsResponseBodyProductions(DaraModel):
    def __init__(
        self,
        comfy_task_id: str = None,
        creation_time: str = None,
        file_name: str = None,
        production_id: str = None,
        state: str = None,
        updated_time: str = None,
    ):
        self.comfy_task_id = comfy_task_id
        self.creation_time = creation_time
        self.file_name = file_name
        self.production_id = production_id
        self.state = state
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comfy_task_id is not None:
            result['ComfyTaskId'] = self.comfy_task_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        if self.state is not None:
            result['State'] = self.state

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComfyTaskId') is not None:
            self.comfy_task_id = m.get('ComfyTaskId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

