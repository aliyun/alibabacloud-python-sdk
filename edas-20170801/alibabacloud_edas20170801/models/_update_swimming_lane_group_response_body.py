# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class UpdateSwimmingLaneGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.UpdateSwimmingLaneGroupResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data that is returned.
        self.data = data
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateSwimmingLaneGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateSwimmingLaneGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        application_list: List[main_models.UpdateSwimmingLaneGroupResponseBodyDataApplicationList] = None,
        entry_application: main_models.UpdateSwimmingLaneGroupResponseBodyDataEntryApplication = None,
        id: int = None,
        name: str = None,
        namespace_id: str = None,
    ):
        # The list of applications related to the lane group.
        self.application_list = application_list
        # The EDAS ingress gateway information.
        self.entry_application = entry_application
        # The ID of the lane group.
        self.id = id
        # The name of the lane group.
        self.name = name
        # The ID of the namespace.
        self.namespace_id = namespace_id

    def validate(self):
        if self.application_list:
            for v1 in self.application_list:
                 if v1:
                    v1.validate()
        if self.entry_application:
            self.entry_application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationList'] = []
        if self.application_list is not None:
            for k1 in self.application_list:
                result['ApplicationList'].append(k1.to_map() if k1 else None)

        if self.entry_application is not None:
            result['EntryApplication'] = self.entry_application.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_list = []
        if m.get('ApplicationList') is not None:
            for k1 in m.get('ApplicationList'):
                temp_model = main_models.UpdateSwimmingLaneGroupResponseBodyDataApplicationList()
                self.application_list.append(temp_model.from_map(k1))

        if m.get('EntryApplication') is not None:
            temp_model = main_models.UpdateSwimmingLaneGroupResponseBodyDataEntryApplication()
            self.entry_application = temp_model.from_map(m.get('EntryApplication'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

class UpdateSwimmingLaneGroupResponseBodyDataEntryApplication(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

class UpdateSwimmingLaneGroupResponseBodyDataApplicationList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

