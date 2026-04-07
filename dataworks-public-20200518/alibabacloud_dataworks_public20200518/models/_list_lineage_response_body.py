# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListLineageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListLineageResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The structure returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListLineageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListLineageResponseBodyData(DaraModel):
    def __init__(
        self,
        data_entity_list: List[main_models.ListLineageResponseBodyDataDataEntityList] = None,
        next_token: str = None,
    ):
        # The array of the entity structure.
        self.data_entity_list = data_entity_list
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token

    def validate(self):
        if self.data_entity_list:
            for v1 in self.data_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k1 in self.data_entity_list:
                result['DataEntityList'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_entity_list = []
        if m.get('DataEntityList') is not None:
            for k1 in m.get('DataEntityList'):
                temp_model = main_models.ListLineageResponseBodyDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListLineageResponseBodyDataDataEntityList(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        entity: main_models.Entity = None,
        relation_list: List[main_models.ListLineageResponseBodyDataDataEntityListRelationList] = None,
    ):
        # The time when the lineage was generated.
        self.create_timestamp = create_timestamp
        # The information about the entity.
        self.entity = entity
        # The array of the relationship structure.
        self.relation_list = relation_list

    def validate(self):
        if self.entity:
            self.entity.validate()
        if self.relation_list:
            for v1 in self.relation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.entity is not None:
            result['Entity'] = self.entity.to_map()

        result['RelationList'] = []
        if self.relation_list is not None:
            for k1 in self.relation_list:
                result['RelationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Entity') is not None:
            temp_model = main_models.Entity()
            self.entity = temp_model.from_map(m.get('Entity'))

        self.relation_list = []
        if m.get('RelationList') is not None:
            for k1 in m.get('RelationList'):
                temp_model = main_models.ListLineageResponseBodyDataDataEntityListRelationList()
                self.relation_list.append(temp_model.from_map(k1))

        return self

class ListLineageResponseBodyDataDataEntityListRelationList(DaraModel):
    def __init__(
        self,
        channel: str = None,
        datasource: str = None,
        guid: str = None,
        type: str = None,
    ):
        # The data channel. Valid values:
        # 
        # *   **FIRST_PARTY: DataWorks platform**
        # *   **THIRD_PARTY: user registration**
        self.channel = channel
        # The data source.
        self.datasource = datasource
        # The unique relationship ID.
        self.guid = guid
        # The task type, which is used to describe the relationship between entities, such as SQL-based calculation, mapping based on report fields, or API operation definition.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.datasource is not None:
            result['Datasource'] = self.datasource

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Datasource') is not None:
            self.datasource = m.get('Datasource')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

