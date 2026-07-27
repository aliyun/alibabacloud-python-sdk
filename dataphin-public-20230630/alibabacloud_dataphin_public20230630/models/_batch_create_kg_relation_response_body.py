# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class BatchCreateKgRelationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_result: main_models.BatchCreateKgRelationResponseBodyCreateResult = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The result of batch relationship record creation.
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
            temp_model = main_models.BatchCreateKgRelationResponseBodyCreateResult()
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

class BatchCreateKgRelationResponseBodyCreateResult(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        success_count: int = None,
        success_relation_list: List[main_models.BatchCreateKgRelationResponseBodyCreateResultSuccessRelationList] = None,
    ):
        # The number of failed records.
        self.fail_count = fail_count
        # The number of successfully created records.
        self.success_count = success_count
        # The list of successfully created entity records.
        self.success_relation_list = success_relation_list

    def validate(self):
        if self.success_relation_list:
            for v1 in self.success_relation_list:
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

        result['SuccessRelationList'] = []
        if self.success_relation_list is not None:
            for k1 in self.success_relation_list:
                result['SuccessRelationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        self.success_relation_list = []
        if m.get('SuccessRelationList') is not None:
            for k1 in m.get('SuccessRelationList'):
                temp_model = main_models.BatchCreateKgRelationResponseBodyCreateResultSuccessRelationList()
                self.success_relation_list.append(temp_model.from_map(k1))

        return self

class BatchCreateKgRelationResponseBodyCreateResultSuccessRelationList(DaraModel):
    def __init__(
        self,
        relation_id: str = None,
        relation_type: str = None,
    ):
        # The relationship record ID.
        self.relation_id = relation_id
        # The relationship type code.
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        return self

