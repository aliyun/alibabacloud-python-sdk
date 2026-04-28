# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class AuditLog(DaraModel):
    def __init__(
        self,
        acted_at: str = None,
        action_category: str = None,
        action_type: str = None,
        actor_id: str = None,
        actor_name: str = None,
        actor_type: str = None,
        client_device: str = None,
        client_ip: str = None,
        client_type: str = None,
        client_version: str = None,
        detail: main_models.AuditLogDetail = None,
        file_path_type: str = None,
        log_id: str = None,
        object_id: str = None,
        object_name: str = None,
    ):
        self.acted_at = acted_at
        self.action_category = action_category
        self.action_type = action_type
        self.actor_id = actor_id
        self.actor_name = actor_name
        self.actor_type = actor_type
        self.client_device = client_device
        self.client_ip = client_ip
        self.client_type = client_type
        self.client_version = client_version
        self.detail = detail
        self.file_path_type = file_path_type
        self.log_id = log_id
        self.object_id = object_id
        self.object_name = object_name

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acted_at is not None:
            result['acted_at'] = self.acted_at

        if self.action_category is not None:
            result['action_category'] = self.action_category

        if self.action_type is not None:
            result['action_type'] = self.action_type

        if self.actor_id is not None:
            result['actor_id'] = self.actor_id

        if self.actor_name is not None:
            result['actor_name'] = self.actor_name

        if self.actor_type is not None:
            result['actor_type'] = self.actor_type

        if self.client_device is not None:
            result['client_device'] = self.client_device

        if self.client_ip is not None:
            result['client_ip'] = self.client_ip

        if self.client_type is not None:
            result['client_type'] = self.client_type

        if self.client_version is not None:
            result['client_version'] = self.client_version

        if self.detail is not None:
            result['detail'] = self.detail.to_map()

        if self.file_path_type is not None:
            result['file_path_type'] = self.file_path_type

        if self.log_id is not None:
            result['log_id'] = self.log_id

        if self.object_id is not None:
            result['object_id'] = self.object_id

        if self.object_name is not None:
            result['object_name'] = self.object_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acted_at') is not None:
            self.acted_at = m.get('acted_at')

        if m.get('action_category') is not None:
            self.action_category = m.get('action_category')

        if m.get('action_type') is not None:
            self.action_type = m.get('action_type')

        if m.get('actor_id') is not None:
            self.actor_id = m.get('actor_id')

        if m.get('actor_name') is not None:
            self.actor_name = m.get('actor_name')

        if m.get('actor_type') is not None:
            self.actor_type = m.get('actor_type')

        if m.get('client_device') is not None:
            self.client_device = m.get('client_device')

        if m.get('client_ip') is not None:
            self.client_ip = m.get('client_ip')

        if m.get('client_type') is not None:
            self.client_type = m.get('client_type')

        if m.get('client_version') is not None:
            self.client_version = m.get('client_version')

        if m.get('detail') is not None:
            temp_model = main_models.AuditLogDetail()
            self.detail = temp_model.from_map(m.get('detail'))

        if m.get('file_path_type') is not None:
            self.file_path_type = m.get('file_path_type')

        if m.get('log_id') is not None:
            self.log_id = m.get('log_id')

        if m.get('object_id') is not None:
            self.object_id = m.get('object_id')

        if m.get('object_name') is not None:
            self.object_name = m.get('object_name')

        return self

