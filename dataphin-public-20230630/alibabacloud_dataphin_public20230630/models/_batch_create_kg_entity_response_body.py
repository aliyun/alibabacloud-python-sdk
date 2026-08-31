# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class BatchCreateKgEntityResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_result: main_models.BatchCreateKgEntityResponseBodyCreateResult = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The result of creating entity records in batches.
        self.create_result = create_result
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.create_result:
            self.create_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_result is not None:
            result['CreateResult'] = self.create_result.to_map()

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

        if m.get('CreateResult') is not None:
            temp_model = main_models.BatchCreateKgEntityResponseBodyCreateResult()
            self.create_result = temp_model.from_map(m.get('CreateResult'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class BatchCreateKgEntityResponseBodyCreateResult(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        success_count: int = None,
        success_entity_list: List[main_models.BatchCreateKgEntityResponseBodyCreateResultSuccessEntityList] = None,
    ):
        # The number of entity records that failed to be created.
        self.fail_count = fail_count
        # The number of successfully created entity records.
        self.success_count = success_count
        # The list of IDs of successfully created entity records.
        self.success_entity_list = success_entity_list

    def validate(self):
        if self.success_entity_list:
            for v1 in self.success_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        result['SuccessEntityList'] = []
        if self.success_entity_list is not None:
            for k1 in self.success_entity_list:
                result['SuccessEntityList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        self.success_entity_list = []
        if m.get('SuccessEntityList') is not None:
            for k1 in m.get('SuccessEntityList'):
                temp_model = main_models.BatchCreateKgEntityResponseBodyCreateResultSuccessEntityList()
                self.success_entity_list.append(temp_model.from_map(k1))

        return self

class BatchCreateKgEntityResponseBodyCreateResultSuccessEntityList(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        # The entity record ID.
        self.entity_id = entity_id
        # The entity type code.
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        return self

