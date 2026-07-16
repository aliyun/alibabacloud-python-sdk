# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListPortalMenuAuthorizationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListPortalMenuAuthorizationResponseBodyResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # A list of authorization details for the BI portal menus.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # - true: The request was successful.
        # 
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListPortalMenuAuthorizationResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListPortalMenuAuthorizationResponseBodyResult(DaraModel):
    def __init__(
        self,
        menu_id: str = None,
        receivers: List[main_models.ListPortalMenuAuthorizationResponseBodyResultReceivers] = None,
        show_only_with_access: bool = None,
    ):
        # The ID of the leaf-node menu in the BI portal.
        self.menu_id = menu_id
        # The details of the authorization objects for the menu.
        self.receivers = receivers
        # Indicates whether the menu is visible only to authorized users. Valid values:
        # 
        # - true: The menu is visible only to authorized users.
        # 
        # - false: The menu is visible to all users.
        self.show_only_with_access = show_only_with_access

    def validate(self):
        if self.receivers:
            for v1 in self.receivers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.menu_id is not None:
            result['MenuId'] = self.menu_id

        result['Receivers'] = []
        if self.receivers is not None:
            for k1 in self.receivers:
                result['Receivers'].append(k1.to_map() if k1 else None)

        if self.show_only_with_access is not None:
            result['ShowOnlyWithAccess'] = self.show_only_with_access

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MenuId') is not None:
            self.menu_id = m.get('MenuId')

        self.receivers = []
        if m.get('Receivers') is not None:
            for k1 in m.get('Receivers'):
                temp_model = main_models.ListPortalMenuAuthorizationResponseBodyResultReceivers()
                self.receivers.append(temp_model.from_map(k1))

        if m.get('ShowOnlyWithAccess') is not None:
            self.show_only_with_access = m.get('ShowOnlyWithAccess')

        return self

class ListPortalMenuAuthorizationResponseBodyResultReceivers(DaraModel):
    def __init__(
        self,
        auth_points_value: int = None,
        receiver_id: str = None,
        receiver_type: int = None,
    ):
        # The authorization type for the menu. Valid values:
        # 
        # - 1: View
        # 
        # - 11: Edit
        # 
        # - 3: Export and view
        # 
        # - 10: Manage data entry
        self.auth_points_value = auth_points_value
        # The ID of the authorization object.
        # 
        # > - If the authorization object is an organization, this ID is the organization ID.
        # >
        # > - If the authorization object is a workspace, this ID is the workspace ID.
        self.receiver_id = receiver_id
        # The type of the authorization object. Valid values:
        # 
        # - 0: User
        # 
        # - 1: User group
        # 
        # - 2: Organization
        # 
        # - 3: Workspace
        self.receiver_type = receiver_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_points_value is not None:
            result['AuthPointsValue'] = self.auth_points_value

        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id

        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPointsValue') is not None:
            self.auth_points_value = m.get('AuthPointsValue')

        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')

        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')

        return self

