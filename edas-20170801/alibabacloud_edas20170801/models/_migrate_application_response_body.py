# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class MigrateApplicationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: main_models.MigrateApplicationResponseBodyData = None,
    ):
        # The status code.
        self.code = code
        # The additional information.
        self.message = message
        # The API information.
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('data') is not None:
            temp_model = main_models.MigrateApplicationResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class MigrateApplicationResponseBodyData(DaraModel):
    def __init__(
        self,
        migration_id: str = None,
    ):
        # The migration ID.
        self.migration_id = migration_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.migration_id is not None:
            result['migrationId'] = self.migration_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('migrationId') is not None:
            self.migration_id = m.get('migrationId')

        return self

