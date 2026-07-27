# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ImportKgSchemaResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        import_result: main_models.ImportKgSchemaResponseBodyImportResult = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.import_result = import_result
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.import_result:
            self.import_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.import_result is not None:
            result['ImportResult'] = self.import_result.to_map()

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('ImportResult') is not None:
            temp_model = main_models.ImportKgSchemaResponseBodyImportResult()
            self.import_result = temp_model.from_map(m.get('ImportResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ImportKgSchemaResponseBodyImportResult(DaraModel):
    def __init__(
        self,
        entity_type_count: int = None,
        relation_type_count: int = None,
    ):
        self.entity_type_count = entity_type_count
        self.relation_type_count = relation_type_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_type_count is not None:
            result['EntityTypeCount'] = self.entity_type_count

        if self.relation_type_count is not None:
            result['RelationTypeCount'] = self.relation_type_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityTypeCount') is not None:
            self.entity_type_count = m.get('EntityTypeCount')

        if m.get('RelationTypeCount') is not None:
            self.relation_type_count = m.get('RelationTypeCount')

        return self

