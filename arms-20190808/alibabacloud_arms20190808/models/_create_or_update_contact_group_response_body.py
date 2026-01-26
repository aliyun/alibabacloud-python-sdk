# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateContactGroupResponseBody(DaraModel):
    def __init__(
        self,
        alert_contact_group: main_models.CreateOrUpdateContactGroupResponseBodyAlertContactGroup = None,
        request_id: str = None,
    ):
        # The information about the alert contact group.
        self.alert_contact_group = alert_contact_group
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.alert_contact_group:
            self.alert_contact_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_contact_group is not None:
            result['AlertContactGroup'] = self.alert_contact_group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertContactGroup') is not None:
            temp_model = main_models.CreateOrUpdateContactGroupResponseBodyAlertContactGroup()
            self.alert_contact_group = temp_model.from_map(m.get('AlertContactGroup'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateOrUpdateContactGroupResponseBodyAlertContactGroup(DaraModel):
    def __init__(
        self,
        contact_group_id: float = None,
        contact_group_name: str = None,
        contact_ids: str = None,
    ):
        # The ID of the alert contact group.
        self.contact_group_id = contact_group_id
        # The name of the alert contact group.
        self.contact_group_name = contact_group_name
        # The IDs of the contacts that are included in the alert contact group.
        self.contact_ids = contact_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id

        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')

        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')

        return self

