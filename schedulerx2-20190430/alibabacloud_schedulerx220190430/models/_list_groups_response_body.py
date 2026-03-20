# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class ListGroupsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListGroupsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The applications.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.ListGroupsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        app_groups: List[main_models.ListGroupsResponseBodyDataAppGroups] = None,
    ):
        # The applications and their details.
        self.app_groups = app_groups

    def validate(self):
        if self.app_groups:
            for v1 in self.app_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppGroups'] = []
        if self.app_groups is not None:
            for k1 in self.app_groups:
                result['AppGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_groups = []
        if m.get('AppGroups') is not None:
            for k1 in m.get('AppGroups'):
                temp_model = main_models.ListGroupsResponseBodyDataAppGroups()
                self.app_groups.append(temp_model.from_map(k1))

        return self

class ListGroupsResponseBodyDataAppGroups(DaraModel):
    def __init__(
        self,
        app_group_id: int = None,
        app_key: str = None,
        app_name: str = None,
        app_version: int = None,
        description: str = None,
        enable_log: bool = None,
        group_id: str = None,
        namespace: str = None,
    ):
        # The application group ID.
        self.app_group_id = app_group_id
        # The AppKey for the application.
        self.app_key = app_key
        # The name of the application.
        self.app_name = app_name
        # The application version. 1: Basic version, 2: Professional version.
        self.app_version = app_version
        # The description of the application.
        self.description = description
        self.enable_log = enable_log
        # The application ID.
        self.group_id = group_id
        # The ID of the namespace.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

