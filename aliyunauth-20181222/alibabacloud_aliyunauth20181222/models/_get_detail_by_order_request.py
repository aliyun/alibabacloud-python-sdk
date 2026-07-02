# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDetailByOrderRequest(DaraModel):
    def __init__(
        self,
        acceptor: str = None,
        biz_no: str = None,
        channel: str = None,
        check_auth_items: str = None,
        emp_id: str = None,
        language: str = None,
        opt_source: str = None,
    ):
        # This parameter is required.
        self.acceptor = acceptor
        # This parameter is required.
        self.biz_no = biz_no
        # This parameter is required.
        self.channel = channel
        self.check_auth_items = check_auth_items
        # This parameter is required.
        self.emp_id = emp_id
        self.language = language
        # This parameter is required.
        self.opt_source = opt_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceptor is not None:
            result['Acceptor'] = self.acceptor

        if self.biz_no is not None:
            result['BizNo'] = self.biz_no

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.check_auth_items is not None:
            result['CheckAuthItems'] = self.check_auth_items

        if self.emp_id is not None:
            result['EmpId'] = self.emp_id

        if self.language is not None:
            result['Language'] = self.language

        if self.opt_source is not None:
            result['OptSource'] = self.opt_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acceptor') is not None:
            self.acceptor = m.get('Acceptor')

        if m.get('BizNo') is not None:
            self.biz_no = m.get('BizNo')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('CheckAuthItems') is not None:
            self.check_auth_items = m.get('CheckAuthItems')

        if m.get('EmpId') is not None:
            self.emp_id = m.get('EmpId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OptSource') is not None:
            self.opt_source = m.get('OptSource')

        return self

