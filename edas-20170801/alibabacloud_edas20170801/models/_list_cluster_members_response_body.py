# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListClusterMembersResponseBody(DaraModel):
    def __init__(
        self,
        cluster_member_page: main_models.ListClusterMembersResponseBodyClusterMemberPage = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The information about the ECS instances in the cluster.
        self.cluster_member_page = cluster_member_page
        # The HTTP status code that is returned.
        self.code = code
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cluster_member_page:
            self.cluster_member_page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_member_page is not None:
            result['ClusterMemberPage'] = self.cluster_member_page.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterMemberPage') is not None:
            temp_model = main_models.ListClusterMembersResponseBodyClusterMemberPage()
            self.cluster_member_page = temp_model.from_map(m.get('ClusterMemberPage'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClusterMembersResponseBodyClusterMemberPage(DaraModel):
    def __init__(
        self,
        cluster_member_list: main_models.ListClusterMembersResponseBodyClusterMemberPageClusterMemberList = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.cluster_member_list = cluster_member_list
        # The page number of the returned page. If this parameter is not returned, the first page is returned.
        self.current_page = current_page
        # The number of ECS instances returned per page.
        self.page_size = page_size
        # The total number of pages returned when all ECS instances are returned based on the specified PageSize parameter.
        self.total_size = total_size

    def validate(self):
        if self.cluster_member_list:
            self.cluster_member_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_member_list is not None:
            result['ClusterMemberList'] = self.cluster_member_list.to_map()

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterMemberList') is not None:
            temp_model = main_models.ListClusterMembersResponseBodyClusterMemberPageClusterMemberList()
            self.cluster_member_list = temp_model.from_map(m.get('ClusterMemberList'))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListClusterMembersResponseBodyClusterMemberPageClusterMemberList(DaraModel):
    def __init__(
        self,
        cluster_member: List[main_models.ListClusterMembersResponseBodyClusterMemberPageClusterMemberListClusterMember] = None,
    ):
        self.cluster_member = cluster_member

    def validate(self):
        if self.cluster_member:
            for v1 in self.cluster_member:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterMember'] = []
        if self.cluster_member is not None:
            for k1 in self.cluster_member:
                result['ClusterMember'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_member = []
        if m.get('ClusterMember') is not None:
            for k1 in m.get('ClusterMember'):
                temp_model = main_models.ListClusterMembersResponseBodyClusterMemberPageClusterMemberListClusterMember()
                self.cluster_member.append(temp_model.from_map(k1))

        return self

class ListClusterMembersResponseBodyClusterMemberPageClusterMemberListClusterMember(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_member_id: str = None,
        create_time: int = None,
        ecs_id: str = None,
        ecu_id: str = None,
        private_ip: str = None,
        status: int = None,
        update_time: int = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_member_id = cluster_member_id
        self.create_time = create_time
        self.ecs_id = ecs_id
        self.ecu_id = ecu_id
        self.private_ip = private_ip
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_member_id is not None:
            result['ClusterMemberId'] = self.cluster_member_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id

        if self.ecu_id is not None:
            result['EcuId'] = self.ecu_id

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterMemberId') is not None:
            self.cluster_member_id = m.get('ClusterMemberId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')

        if m.get('EcuId') is not None:
            self.ecu_id = m.get('EcuId')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

