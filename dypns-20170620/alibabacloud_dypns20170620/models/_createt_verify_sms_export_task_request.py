# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatetVerifySmsExportTaskRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_name: str = None,
        send_status: int = None,
        sign_name: str = None,
        start_date: str = None,
        task_name: str = None,
        template_code: str = None,
    ):
        self.end_date = end_date
        self.owner_id = owner_id
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_name = scheme_name
        self.send_status = send_status
        self.sign_name = sign_name
        self.start_date = start_date
        self.task_name = task_name
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name

        if self.send_status is not None:
            result['SendStatus'] = self.send_status

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')

        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

