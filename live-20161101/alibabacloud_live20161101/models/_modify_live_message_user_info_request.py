# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLiveMessageUserInfoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data_center: str = None,
        user_id: str = None,
        user_meta_info: str = None,
    ):
        # The ID of the interactive messaging application whose user information you want to modify.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The data center. It must be the same as the data center that was specified when you called the [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2593195.html) operation to create the interactive messaging application. Valid values: cn-shanghai and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The ID of the user whose information you want to modify.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The additional information about the user after the modification. The value can be up to 512 bytes in length.
        self.user_meta_info = user_meta_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_meta_info is not None:
            result['UserMetaInfo'] = self.user_meta_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserMetaInfo') is not None:
            self.user_meta_info = m.get('UserMetaInfo')

        return self

