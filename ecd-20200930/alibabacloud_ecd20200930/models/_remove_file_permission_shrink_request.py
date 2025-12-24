# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveFilePermissionShrinkRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        end_user_id: str = None,
        file_id: str = None,
        group_id: str = None,
        member_list_shrink: str = None,
        region_id: str = None,
    ):
        # The ID of the enterprise drive.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The ID of the end user.
        self.end_user_id = end_user_id
        # The file ID. You can call the [ListCdsFiles](https://help.aliyun.com/document_detail/2247622.html) operation to query the ID of the file.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the team space.
        self.group_id = group_id
        # The users that you want to authorize to use the cloud disk.
        # 
        # This parameter is required.
        self.member_list_shrink = member_list_shrink
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.member_list_shrink is not None:
            result['MemberList'] = self.member_list_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MemberList') is not None:
            self.member_list_shrink = m.get('MemberList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

