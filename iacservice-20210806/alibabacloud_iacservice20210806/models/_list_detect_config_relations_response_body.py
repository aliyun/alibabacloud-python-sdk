# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListDetectConfigRelationsResponseBody(DaraModel):
    def __init__(
        self,
        detect_config_relations: List[main_models.ListDetectConfigRelationsResponseBodyDetectConfigRelations] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.detect_config_relations = detect_config_relations
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.detect_config_relations:
            for v1 in self.detect_config_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['detectConfigRelations'] = []
        if self.detect_config_relations is not None:
            for k1 in self.detect_config_relations:
                result['detectConfigRelations'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detect_config_relations = []
        if m.get('detectConfigRelations') is not None:
            for k1 in m.get('detectConfigRelations'):
                temp_model = main_models.ListDetectConfigRelationsResponseBodyDetectConfigRelations()
                self.detect_config_relations.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListDetectConfigRelationsResponseBodyDetectConfigRelations(DaraModel):
    def __init__(
        self,
        attach_date: str = None,
        detect_config_id: str = None,
        enabled: str = None,
        target_id: str = None,
        target_name: str = None,
        target_type: str = None,
    ):
        self.attach_date = attach_date
        self.detect_config_id = detect_config_id
        self.enabled = enabled
        self.target_id = target_id
        self.target_name = target_name
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_date is not None:
            result['attachDate'] = self.attach_date

        if self.detect_config_id is not None:
            result['detectConfigId'] = self.detect_config_id

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.target_id is not None:
            result['targetId'] = self.target_id

        if self.target_name is not None:
            result['targetName'] = self.target_name

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachDate') is not None:
            self.attach_date = m.get('attachDate')

        if m.get('detectConfigId') is not None:
            self.detect_config_id = m.get('detectConfigId')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')

        if m.get('targetName') is not None:
            self.target_name = m.get('targetName')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

