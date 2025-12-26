# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListBindInfoRequest(DaraModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        app_instance_group_id_list: List[str] = None,
        app_instance_id_list: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        user_id_list: List[str] = None,
        wy_id_list: List[str] = None,
    ):
        # The app IDs. You can specify 1 to 100 IDs.
        # 
        # >  If you specify this parameter, only the bindings of the specified apps are returned.
        self.app_id_list = app_id_list
        # The IDs of the delivery groups. You can specify 1 to 100 IDs.
        # 
        # >  If you specify this parameter, only the bindings of the specified delivery groups are returned.
        self.app_instance_group_id_list = app_instance_group_id_list
        # The IDs of app instances. You can specify 1 to 100 IDs.
        # 
        # >  If you specify this parameter, only the bindings of the specified app instances are returned.
        self.app_instance_id_list = app_instance_id_list
        # The page number. Default value: `1`. We recommend that you specify this parameter.
        self.page_number = page_number
        # The number of entries per page. The value cannot be greater than `100`. Default value: `20`. We recommend that you specify this parameter.
        self.page_size = page_size
        # The user IDs. You can specify 1 to 100 IDs.
        # 
        # >  If you specify this parameter, only the bindings of the specified users are returned.
        self.user_id_list = user_id_list
        # The IDs of the Alibaba Cloud Workspace users. You can specify 1 to 100 IDs.
        # 
        # >  If you specify this parameter, only the bindings of the specified Alibaba Cloud Workspace users are returned.
        self.wy_id_list = wy_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list

        if self.app_instance_group_id_list is not None:
            result['AppInstanceGroupIdList'] = self.app_instance_group_id_list

        if self.app_instance_id_list is not None:
            result['AppInstanceIdList'] = self.app_instance_id_list

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list

        if self.wy_id_list is not None:
            result['WyIdList'] = self.wy_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')

        if m.get('AppInstanceGroupIdList') is not None:
            self.app_instance_group_id_list = m.get('AppInstanceGroupIdList')

        if m.get('AppInstanceIdList') is not None:
            self.app_instance_id_list = m.get('AppInstanceIdList')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')

        if m.get('WyIdList') is not None:
            self.wy_id_list = m.get('WyIdList')

        return self

