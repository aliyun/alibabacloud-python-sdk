# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class RegisterLineageRelationResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        lineage_relation: main_models.RegisterLineageRelationResponseBodyLineageRelation = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The lineage.
        self.lineage_relation = lineage_relation
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.lineage_relation:
            self.lineage_relation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.lineage_relation is not None:
            result['LineageRelation'] = self.lineage_relation.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('LineageRelation') is not None:
            temp_model = main_models.RegisterLineageRelationResponseBodyLineageRelation()
            self.lineage_relation = temp_model.from_map(m.get('LineageRelation'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RegisterLineageRelationResponseBodyLineageRelation(DaraModel):
    def __init__(
        self,
        dest_entity_qualified_name: str = None,
        relationship_guid: str = None,
        src_entity_qualified_name: str = None,
    ):
        # The unique identifier of the destination entity.
        self.dest_entity_qualified_name = dest_entity_qualified_name
        # The ID of the lineage between entities.
        self.relationship_guid = relationship_guid
        # The unique identifier of the source entity.
        self.src_entity_qualified_name = src_entity_qualified_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_entity_qualified_name is not None:
            result['DestEntityQualifiedName'] = self.dest_entity_qualified_name

        if self.relationship_guid is not None:
            result['RelationshipGuid'] = self.relationship_guid

        if self.src_entity_qualified_name is not None:
            result['SrcEntityQualifiedName'] = self.src_entity_qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestEntityQualifiedName') is not None:
            self.dest_entity_qualified_name = m.get('DestEntityQualifiedName')

        if m.get('RelationshipGuid') is not None:
            self.relationship_guid = m.get('RelationshipGuid')

        if m.get('SrcEntityQualifiedName') is not None:
            self.src_entity_qualified_name = m.get('SrcEntityQualifiedName')

        return self

