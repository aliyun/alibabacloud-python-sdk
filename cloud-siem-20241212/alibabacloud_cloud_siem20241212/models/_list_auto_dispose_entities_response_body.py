# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListAutoDisposeEntitiesResponseBody(DaraModel):
    def __init__(
        self,
        auto_decision_entities: List[main_models.ListAutoDisposeEntitiesResponseBodyAutoDecisionEntities] = None,
        current_page: int = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.auto_decision_entities = auto_decision_entities
        self.current_page = current_page
        self.max_results = max_results
        self.next_token = next_token
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.auto_decision_entities:
            for v1 in self.auto_decision_entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoDecisionEntities'] = []
        if self.auto_decision_entities is not None:
            for k1 in self.auto_decision_entities:
                result['AutoDecisionEntities'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_decision_entities = []
        if m.get('AutoDecisionEntities') is not None:
            for k1 in m.get('AutoDecisionEntities'):
                temp_model = main_models.ListAutoDisposeEntitiesResponseBodyAutoDecisionEntities()
                self.auto_decision_entities.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAutoDisposeEntitiesResponseBodyAutoDecisionEntities(DaraModel):
    def __init__(
        self,
        alert_id: str = None,
        disposal_method: str = None,
        dispose_record_id: str = None,
        entity_name: str = None,
        entity_type: str = None,
        entity_uuid: str = None,
        playbook_uuid: str = None,
        uuid: str = None,
    ):
        self.alert_id = alert_id
        self.disposal_method = disposal_method
        self.dispose_record_id = dispose_record_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.entity_uuid = entity_uuid
        self.playbook_uuid = playbook_uuid
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.disposal_method is not None:
            result['DisposalMethod'] = self.disposal_method

        if self.dispose_record_id is not None:
            result['DisposeRecordId'] = self.dispose_record_id

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('DisposalMethod') is not None:
            self.disposal_method = m.get('DisposalMethod')

        if m.get('DisposeRecordId') is not None:
            self.dispose_record_id = m.get('DisposeRecordId')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

