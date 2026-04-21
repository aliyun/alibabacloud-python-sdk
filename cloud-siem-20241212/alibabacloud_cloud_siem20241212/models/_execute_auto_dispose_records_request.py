# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ExecuteAutoDisposeRecordsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        selected_entity_list: List[main_models.ExecuteAutoDisposeRecordsRequestSelectedEntityList] = None,
        un_selected_entity_list: List[main_models.ExecuteAutoDisposeRecordsRequestUnSelectedEntityList] = None,
    ):
        # This parameter is required.
        self.lang = lang
        self.selected_entity_list = selected_entity_list
        self.un_selected_entity_list = un_selected_entity_list

    def validate(self):
        if self.selected_entity_list:
            for v1 in self.selected_entity_list:
                 if v1:
                    v1.validate()
        if self.un_selected_entity_list:
            for v1 in self.un_selected_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        result['SelectedEntityList'] = []
        if self.selected_entity_list is not None:
            for k1 in self.selected_entity_list:
                result['SelectedEntityList'].append(k1.to_map() if k1 else None)

        result['UnSelectedEntityList'] = []
        if self.un_selected_entity_list is not None:
            for k1 in self.un_selected_entity_list:
                result['UnSelectedEntityList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        self.selected_entity_list = []
        if m.get('SelectedEntityList') is not None:
            for k1 in m.get('SelectedEntityList'):
                temp_model = main_models.ExecuteAutoDisposeRecordsRequestSelectedEntityList()
                self.selected_entity_list.append(temp_model.from_map(k1))

        self.un_selected_entity_list = []
        if m.get('UnSelectedEntityList') is not None:
            for k1 in m.get('UnSelectedEntityList'):
                temp_model = main_models.ExecuteAutoDisposeRecordsRequestUnSelectedEntityList()
                self.un_selected_entity_list.append(temp_model.from_map(k1))

        return self

class ExecuteAutoDisposeRecordsRequestUnSelectedEntityList(DaraModel):
    def __init__(
        self,
        auto_dispose_record_id: str = None,
        entity_uuid: str = None,
    ):
        self.auto_dispose_record_id = auto_dispose_record_id
        self.entity_uuid = entity_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_dispose_record_id is not None:
            result['AutoDisposeRecordId'] = self.auto_dispose_record_id

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDisposeRecordId') is not None:
            self.auto_dispose_record_id = m.get('AutoDisposeRecordId')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        return self

class ExecuteAutoDisposeRecordsRequestSelectedEntityList(DaraModel):
    def __init__(
        self,
        auto_dispose_record_id: str = None,
        entity_uuid: str = None,
    ):
        self.auto_dispose_record_id = auto_dispose_record_id
        self.entity_uuid = entity_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_dispose_record_id is not None:
            result['AutoDisposeRecordId'] = self.auto_dispose_record_id

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDisposeRecordId') is not None:
            self.auto_dispose_record_id = m.get('AutoDisposeRecordId')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        return self

