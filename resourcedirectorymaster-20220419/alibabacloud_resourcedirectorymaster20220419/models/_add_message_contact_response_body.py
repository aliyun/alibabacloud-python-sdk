# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class AddMessageContactResponseBody(DaraModel):
    def __init__(
        self,
        contact: main_models.AddMessageContactResponseBodyContact = None,
        request_id: str = None,
    ):
        # The information about the contact.
        self.contact = contact
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.contact:
            self.contact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact is not None:
            result['Contact'] = self.contact.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contact') is not None:
            temp_model = main_models.AddMessageContactResponseBodyContact()
            self.contact = temp_model.from_map(m.get('Contact'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddMessageContactResponseBodyContact(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        create_date: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The time when the contact was created.
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        return self

