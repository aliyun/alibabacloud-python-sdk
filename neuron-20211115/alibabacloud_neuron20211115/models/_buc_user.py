# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BucUser(DaraModel):
    def __init__(
        self,
        account: str = None,
        emp_id: str = None,
        emp_type: str = None,
        enterprise_id: int = None,
        name: str = None,
        nick_name: str = None,
        personal_photo_url: str = None,
        request_id: str = None,
    ):
        self.account = account
        self.emp_id = emp_id
        self.emp_type = emp_type
        self.enterprise_id = enterprise_id
        self.name = name
        self.nick_name = nick_name
        self.personal_photo_url = personal_photo_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['account'] = self.account

        if self.emp_id is not None:
            result['empId'] = self.emp_id

        if self.emp_type is not None:
            result['empType'] = self.emp_type

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.name is not None:
            result['name'] = self.name

        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        if self.personal_photo_url is not None:
            result['personalPhotoUrl'] = self.personal_photo_url

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account') is not None:
            self.account = m.get('account')

        if m.get('empId') is not None:
            self.emp_id = m.get('empId')

        if m.get('empType') is not None:
            self.emp_type = m.get('empType')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('personalPhotoUrl') is not None:
            self.personal_photo_url = m.get('personalPhotoUrl')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

