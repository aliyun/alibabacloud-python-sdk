# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListAuthorityResponseBody(DaraModel):
    def __init__(
        self,
        authority_list: main_models.ListAuthorityResponseBodyAuthorityList = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.authority_list = authority_list
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.authority_list:
            self.authority_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authority_list is not None:
            result['AuthorityList'] = self.authority_list.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorityList') is not None:
            temp_model = main_models.ListAuthorityResponseBodyAuthorityList()
            self.authority_list = temp_model.from_map(m.get('AuthorityList'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAuthorityResponseBodyAuthorityList(DaraModel):
    def __init__(
        self,
        authority: List[main_models.ListAuthorityResponseBodyAuthorityListAuthority] = None,
    ):
        self.authority = authority

    def validate(self):
        if self.authority:
            for v1 in self.authority:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Authority'] = []
        if self.authority is not None:
            for k1 in self.authority:
                result['Authority'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authority = []
        if m.get('Authority') is not None:
            for k1 in m.get('Authority'):
                temp_model = main_models.ListAuthorityResponseBodyAuthorityListAuthority()
                self.authority.append(temp_model.from_map(k1))

        return self

class ListAuthorityResponseBodyAuthorityListAuthority(DaraModel):
    def __init__(
        self,
        action_list: main_models.ListAuthorityResponseBodyAuthorityListAuthorityActionList = None,
        description: str = None,
        group_id: str = None,
        name: str = None,
    ):
        self.action_list = action_list
        self.description = description
        self.group_id = group_id
        self.name = name

    def validate(self):
        if self.action_list:
            self.action_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_list is not None:
            result['ActionList'] = self.action_list.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionList') is not None:
            temp_model = main_models.ListAuthorityResponseBodyAuthorityListAuthorityActionList()
            self.action_list = temp_model.from_map(m.get('ActionList'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListAuthorityResponseBodyAuthorityListAuthorityActionList(DaraModel):
    def __init__(
        self,
        action: List[main_models.ListAuthorityResponseBodyAuthorityListAuthorityActionListAction] = None,
    ):
        self.action = action

    def validate(self):
        if self.action:
            for v1 in self.action:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Action'] = []
        if self.action is not None:
            for k1 in self.action:
                result['Action'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action = []
        if m.get('Action') is not None:
            for k1 in m.get('Action'):
                temp_model = main_models.ListAuthorityResponseBodyAuthorityListAuthorityActionListAction()
                self.action.append(temp_model.from_map(k1))

        return self

class ListAuthorityResponseBodyAuthorityListAuthorityActionListAction(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        group_id: str = None,
        name: str = None,
    ):
        self.code = code
        self.description = description
        self.group_id = group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

