# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class DriveLogDetail(DaraModel):
    def __init__(
        self,
        force_delete: bool = None,
        handover_owner_name: str = None,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        owner_type: str = None,
        total_size: int = None,
        update_to: main_models.DriveLogDetailUpdateTo = None,
    ):
        self.force_delete = force_delete
        self.handover_owner_name = handover_owner_name
        self.name = name
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.total_size = total_size
        self.update_to = update_to

    def validate(self):
        if self.update_to:
            self.update_to.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_delete is not None:
            result['force_delete'] = self.force_delete

        if self.handover_owner_name is not None:
            result['handover_owner_name'] = self.handover_owner_name

        if self.name is not None:
            result['name'] = self.name

        if self.owner_id is not None:
            result['owner_id'] = self.owner_id

        if self.owner_name is not None:
            result['owner_name'] = self.owner_name

        if self.owner_type is not None:
            result['owner_type'] = self.owner_type

        if self.total_size is not None:
            result['total_size'] = self.total_size

        if self.update_to is not None:
            result['update_to'] = self.update_to.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('force_delete') is not None:
            self.force_delete = m.get('force_delete')

        if m.get('handover_owner_name') is not None:
            self.handover_owner_name = m.get('handover_owner_name')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner_id') is not None:
            self.owner_id = m.get('owner_id')

        if m.get('owner_name') is not None:
            self.owner_name = m.get('owner_name')

        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')

        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        if m.get('update_to') is not None:
            temp_model = main_models.DriveLogDetailUpdateTo()
            self.update_to = temp_model.from_map(m.get('update_to'))

        return self



class DriveLogDetailUpdateTo(DaraModel):
    def __init__(
        self,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        owner_type: str = None,
        total_size: int = None,
    ):
        self.name = name
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.owner_id is not None:
            result['owner_id'] = self.owner_id

        if self.owner_name is not None:
            result['owner_name'] = self.owner_name

        if self.owner_type is not None:
            result['owner_type'] = self.owner_type

        if self.total_size is not None:
            result['total_size'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner_id') is not None:
            self.owner_id = m.get('owner_id')

        if m.get('owner_name') is not None:
            self.owner_name = m.get('owner_name')

        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')

        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        return self

