# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class EscalationRule(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        escalations: List[main_models.EscalationRuleEscalations] = None,
        name: str = None,
        update_time: str = None,
        user_id: str = None,
        uuid: str = None,
    ):
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.escalations = escalations
        # This parameter is required.
        self.name = name
        self.update_time = update_time
        self.user_id = user_id
        self.uuid = uuid

    def validate(self):
        if self.escalations:
            for v1 in self.escalations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        result['Escalations'] = []
        if self.escalations is not None:
            for k1 in self.escalations:
                result['Escalations'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.escalations = []
        if m.get('Escalations') is not None:
            for k1 in m.get('Escalations'):
                temp_model = main_models.EscalationRuleEscalations()
                self.escalations.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class EscalationRuleEscalations(DaraModel):
    def __init__(
        self,
        backup_contact_groups: List[str] = None,
        contact_groups: List[str] = None,
        contact_groups_by_level: main_models.EscalationRuleEscalationsContactGroupsByLevel = None,
        escalate_min: int = None,
    ):
        self.backup_contact_groups = backup_contact_groups
        self.contact_groups = contact_groups
        self.contact_groups_by_level = contact_groups_by_level
        self.escalate_min = escalate_min

    def validate(self):
        if self.contact_groups_by_level:
            self.contact_groups_by_level.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_contact_groups is not None:
            result['BackupContactGroups'] = self.backup_contact_groups

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.contact_groups_by_level is not None:
            result['ContactGroupsByLevel'] = self.contact_groups_by_level.to_map()

        if self.escalate_min is not None:
            result['EscalateMin'] = self.escalate_min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupContactGroups') is not None:
            self.backup_contact_groups = m.get('BackupContactGroups')

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('ContactGroupsByLevel') is not None:
            temp_model = main_models.EscalationRuleEscalationsContactGroupsByLevel()
            self.contact_groups_by_level = temp_model.from_map(m.get('ContactGroupsByLevel'))

        if m.get('EscalateMin') is not None:
            self.escalate_min = m.get('EscalateMin')

        return self

class EscalationRuleEscalationsContactGroupsByLevel(DaraModel):
    def __init__(
        self,
        critical: List[str] = None,
        error: List[str] = None,
        info: List[str] = None,
        resolve: List[str] = None,
        warning: List[str] = None,
    ):
        self.critical = critical
        self.error = error
        self.info = info
        self.resolve = resolve
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical

        if self.error is not None:
            result['Error'] = self.error

        if self.info is not None:
            result['Info'] = self.info

        if self.resolve is not None:
            result['Resolve'] = self.resolve

        if self.warning is not None:
            result['Warning'] = self.warning

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            self.critical = m.get('Critical')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Resolve') is not None:
            self.resolve = m.get('Resolve')

        if m.get('Warning') is not None:
            self.warning = m.get('Warning')

        return self

