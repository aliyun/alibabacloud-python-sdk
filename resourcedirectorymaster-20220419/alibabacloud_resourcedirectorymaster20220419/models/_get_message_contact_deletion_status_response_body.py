# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class GetMessageContactDeletionStatusResponseBody(DaraModel):
    def __init__(
        self,
        contact_deletion_status: main_models.GetMessageContactDeletionStatusResponseBodyContactDeletionStatus = None,
        request_id: str = None,
    ):
        # The deletion information of the contact.
        self.contact_deletion_status = contact_deletion_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.contact_deletion_status:
            self.contact_deletion_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_deletion_status is not None:
            result['ContactDeletionStatus'] = self.contact_deletion_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactDeletionStatus') is not None:
            temp_model = main_models.GetMessageContactDeletionStatusResponseBodyContactDeletionStatus()
            self.contact_deletion_status = temp_model.from_map(m.get('ContactDeletionStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMessageContactDeletionStatusResponseBodyContactDeletionStatus(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        fail_reason_list: List[main_models.GetMessageContactDeletionStatusResponseBodyContactDeletionStatusFailReasonList] = None,
        status: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The types of messages received by the contact.
        self.fail_reason_list = fail_reason_list
        # The deletion status of the contact. Valid values:
        # 
        # *   Deleting
        # *   Failed
        self.status = status

    def validate(self):
        if self.fail_reason_list:
            for v1 in self.fail_reason_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        result['FailReasonList'] = []
        if self.fail_reason_list is not None:
            for k1 in self.fail_reason_list:
                result['FailReasonList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        self.fail_reason_list = []
        if m.get('FailReasonList') is not None:
            for k1 in m.get('FailReasonList'):
                temp_model = main_models.GetMessageContactDeletionStatusResponseBodyContactDeletionStatusFailReasonList()
                self.fail_reason_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetMessageContactDeletionStatusResponseBodyContactDeletionStatusFailReasonList(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        message_types: List[str] = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The types of messages received by the contact.
        self.message_types = message_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.message_types is not None:
            result['MessageTypes'] = self.message_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('MessageTypes') is not None:
            self.message_types = m.get('MessageTypes')

        return self

