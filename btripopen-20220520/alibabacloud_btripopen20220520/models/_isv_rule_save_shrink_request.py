# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IsvRuleSaveShrinkRequest(DaraModel):
    def __init__(
        self,
        apply_need: bool = None,
        book_type: str = None,
        bookuser_list_shrink: str = None,
        rule_need: bool = None,
        status: int = None,
        user_id: str = None,
    ):
        self.apply_need = apply_need
        # This parameter is required.
        self.book_type = book_type
        self.bookuser_list_shrink = bookuser_list_shrink
        self.rule_need = rule_need
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_need is not None:
            result['apply_need'] = self.apply_need

        if self.book_type is not None:
            result['book_type'] = self.book_type

        if self.bookuser_list_shrink is not None:
            result['bookuser_list'] = self.bookuser_list_shrink

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

        if m.get('bookuser_list') is not None:
            self.bookuser_list_shrink = m.get('bookuser_list')

        if m.get('rule_need') is not None:
            self.rule_need = m.get('rule_need')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

