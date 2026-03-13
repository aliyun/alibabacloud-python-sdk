# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IsvRuleSaveRequest(DaraModel):
    def __init__(
        self,
        apply_need: bool = None,
        book_type: str = None,
        bookuser_list: List[main_models.IsvRuleSaveRequestBookuserList] = None,
        rule_need: bool = None,
        status: int = None,
        user_id: str = None,
    ):
        self.apply_need = apply_need
        # This parameter is required.
        self.book_type = book_type
        self.bookuser_list = bookuser_list
        self.rule_need = rule_need
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.bookuser_list:
            for v1 in self.bookuser_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_need is not None:
            result['apply_need'] = self.apply_need

        if self.book_type is not None:
            result['book_type'] = self.book_type

        result['bookuser_list'] = []
        if self.bookuser_list is not None:
            for k1 in self.bookuser_list:
                result['bookuser_list'].append(k1.to_map() if k1 else None)

        if self.rule_need is not None:
            result['rule_need'] = self.rule_need

        if self.status is not None:
            result['status'] = self.status

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_need') is not None:
            self.apply_need = m.get('apply_need')

        if m.get('book_type') is not None:
            self.book_type = m.get('book_type')

        self.bookuser_list = []
        if m.get('bookuser_list') is not None:
            for k1 in m.get('bookuser_list'):
                temp_model = main_models.IsvRuleSaveRequestBookuserList()
                self.bookuser_list.append(temp_model.from_map(k1))

        if m.get('rule_need') is not None:
            self.rule_need = m.get('rule_need')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class IsvRuleSaveRequestBookuserList(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: int = None,
    ):
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['entity_id'] = self.entity_id

        if self.entity_type is not None:
            result['entity_type'] = self.entity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity_id') is not None:
            self.entity_id = m.get('entity_id')

        if m.get('entity_type') is not None:
            self.entity_type = m.get('entity_type')

        return self

