# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListLiveMessageGroupsResponseBody(DaraModel):
    def __init__(
        self,
        group_list: List[main_models.ListLiveMessageGroupsResponseBodyGroupList] = None,
        hasmore: bool = None,
        nextpage_token: str = None,
        request_id: str = None,
    ):
        # Details about the groups.
        self.group_list = group_list
        # Indicates whether the current page is followed by another page.
        self.hasmore = hasmore
        # The starting page number for the next query. This parameter is returned only if the value of Hasmore is true.
        self.nextpage_token = nextpage_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.group_list:
            for v1 in self.group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GroupList'] = []
        if self.group_list is not None:
            for k1 in self.group_list:
                result['GroupList'].append(k1.to_map() if k1 else None)

        if self.hasmore is not None:
            result['Hasmore'] = self.hasmore

        if self.nextpage_token is not None:
            result['NextpageToken'] = self.nextpage_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_list = []
        if m.get('GroupList') is not None:
            for k1 in m.get('GroupList'):
                temp_model = main_models.ListLiveMessageGroupsResponseBodyGroupList()
                self.group_list.append(temp_model.from_map(k1))

        if m.get('Hasmore') is not None:
            self.hasmore = m.get('Hasmore')

        if m.get('NextpageToken') is not None:
            self.nextpage_token = m.get('NextpageToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLiveMessageGroupsResponseBodyGroupList(DaraModel):
    def __init__(
        self,
        admin_list: List[str] = None,
        createtime: int = None,
        creator_id: str = None,
        delete: bool = None,
        group_id: str = None,
        group_info: str = None,
        group_name: str = None,
    ):
        # The list of the IDs of the group administrators.
        self.admin_list = admin_list
        # The time when the group was created. The value is a UNIX timestamp. Unit: seconds.
        self.createtime = createtime
        # The ID of the group creator.
        self.creator_id = creator_id
        # Indicates whether the group is deleted.
        self.delete = delete
        # The ID of the group.
        self.group_id = group_id
        # The additional information about the group.
        self.group_info = group_info
        # The name of the group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_list is not None:
            result['AdminList'] = self.admin_list

        if self.createtime is not None:
            result['Createtime'] = self.createtime

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.delete is not None:
            result['Delete'] = self.delete

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_info is not None:
            result['GroupInfo'] = self.group_info

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminList') is not None:
            self.admin_list = m.get('AdminList')

        if m.get('Createtime') is not None:
            self.createtime = m.get('Createtime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupInfo') is not None:
            self.group_info = m.get('GroupInfo')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

