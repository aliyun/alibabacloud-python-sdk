# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class BatchRevokeSeatsRequest(DaraModel):
    def __init__(
        self,
        items: List[main_models.BatchRevokeSeatsRequestItems] = None,
        locale: str = None,
    ):
        # The list of revocation items. This parameter is required.
        self.items = items
        # The language. Valid values: zh-CN and en-US.
        self.locale = locale

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.locale is not None:
            result['Locale'] = self.locale

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.BatchRevokeSeatsRequestItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        return self

class BatchRevokeSeatsRequestItems(DaraModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The ID of the currently associated member.
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        return self

