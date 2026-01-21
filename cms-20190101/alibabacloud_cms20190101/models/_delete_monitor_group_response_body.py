# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DeleteMonitorGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        group: main_models.DeleteMonitorGroupResponseBodyGroup = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the call was successful.
        self.code = code
        # The deleted application group.
        self.group = group
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. The value true indicates a success. The value false indicates a failure.
        self.success = success

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.group is not None:
            result['Group'] = self.group.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Group') is not None:
            temp_model = main_models.DeleteMonitorGroupResponseBodyGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DeleteMonitorGroupResponseBodyGroup(DaraModel):
    def __init__(
        self,
        contact_groups: main_models.DeleteMonitorGroupResponseBodyGroupContactGroups = None,
        group_name: str = None,
    ):
        # The alert groups that receive alert notifications for the application group.
        self.contact_groups = contact_groups
        # The name of the application group.
        self.group_name = group_name

    def validate(self):
        if self.contact_groups:
            self.contact_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups.to_map()

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            temp_model = main_models.DeleteMonitorGroupResponseBodyGroupContactGroups()
            self.contact_groups = temp_model.from_map(m.get('ContactGroups'))

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

class DeleteMonitorGroupResponseBodyGroupContactGroups(DaraModel):
    def __init__(
        self,
        contact_group: List[main_models.DeleteMonitorGroupResponseBodyGroupContactGroupsContactGroup] = None,
    ):
        self.contact_group = contact_group

    def validate(self):
        if self.contact_group:
            for v1 in self.contact_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContactGroup'] = []
        if self.contact_group is not None:
            for k1 in self.contact_group:
                result['ContactGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_group = []
        if m.get('ContactGroup') is not None:
            for k1 in m.get('ContactGroup'):
                temp_model = main_models.DeleteMonitorGroupResponseBodyGroupContactGroupsContactGroup()
                self.contact_group.append(temp_model.from_map(k1))

        return self

class DeleteMonitorGroupResponseBodyGroupContactGroupsContactGroup(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the alert group.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

