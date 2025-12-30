# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class DeleteUsersRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        user: List[main_models.DeleteUsersRequestUser] = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The users that you want to delete.
        # 
        # This parameter is required.
        self.user = user

    def validate(self):
        if self.user:
            for v1 in self.user:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        result['User'] = []
        if self.user is not None:
            for k1 in self.user:
                result['User'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        self.user = []
        if m.get('User') is not None:
            for k1 in m.get('User'):
                temp_model = main_models.DeleteUsersRequestUser()
                self.user.append(temp_model.from_map(k1))

        return self

class DeleteUsersRequestUser(DaraModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        # The name of user N that you want to delete.
        # 
        # Valid values of N: 1 to 100.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

