# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMuteGroupUserRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        group_id: str = None,
        operator_user_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # The ID of the interactive messaging application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the messaging group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the user who performs the operation.
        self.operator_user_id = operator_user_id
        # The page number. Default value: 1. Valid values: 1 to 100000.
        # 
        # This parameter is required.
        self.page_num = page_num
        # The number of entries per page. Default value: 20. Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.operator_user_id is not None:
            result['OperatorUserId'] = self.operator_user_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('OperatorUserId') is not None:
            self.operator_user_id = m.get('OperatorUserId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

