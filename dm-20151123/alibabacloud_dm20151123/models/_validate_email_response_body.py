# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateEmailResponseBody(DaraModel):
    def __init__(
        self,
        domain_part: str = None,
        is_free_mail: bool = None,
        local_part: str = None,
        provider: str = None,
        request_id: str = None,
        status: str = None,
        sub_status: str = None,
    ):
        # The domain part of the email address parsed from the syntax check. The domain part is converted to lowercase.
        self.domain_part = domain_part
        # Indicates whether the address is from a free email service.
        self.is_free_mail = is_free_mail
        # The local part of the email address parsed from the syntax check. The local part is converted to lowercase and the content after the plus sign (+) is removed.
        self.local_part = local_part
        # The email service provider of the address.
        self.provider = provider
        # The request ID.
        self.request_id = request_id
        # The validation status of the email address.
        # 
        # This parameter is required.
        self.status = status
        # The detailed validation status of the email address. This provides more information about the Status.
        # 
        # This parameter is required.
        self.sub_status = sub_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_part is not None:
            result['DomainPart'] = self.domain_part

        if self.is_free_mail is not None:
            result['IsFreeMail'] = self.is_free_mail

        if self.local_part is not None:
            result['LocalPart'] = self.local_part

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainPart') is not None:
            self.domain_part = m.get('DomainPart')

        if m.get('IsFreeMail') is not None:
            self.is_free_mail = m.get('IsFreeMail')

        if m.get('LocalPart') is not None:
            self.local_part = m.get('LocalPart')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        return self

