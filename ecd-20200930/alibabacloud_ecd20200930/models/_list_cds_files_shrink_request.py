# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCdsFilesShrinkRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        end_user_id: str = None,
        file_ids_shrink: str = None,
        group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order_type: str = None,
        parent_file_id: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The ID of the enterprise drive.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The ID of the user to which the network disk is assigned.
        self.end_user_id = end_user_id
        # The IDs of the files to be queried.
        self.file_ids_shrink = file_ids_shrink
        # The ID of the team space.
        self.group_id = group_id
        # The number of entries to return on each page. Default value: 100.
        self.max_results = max_results
        # The query token. Set the value to the value of the `NextToken` parameter returned in the last call to the operation. You do not need to set this parameter when you call the operation for the first time.
        self.next_token = next_token
        # The sorting method of the files.
        # 
        # Valid values:
        # 
        # *   CreateTimeDesc: sorts the by creation time in descending order.
        # *   ModifiedTimeAsc: sort the by modification time in ascending order.
        # *   NameDesc: sorts the by file name in descending order.
        # *   SizeAsc: sorts by file size in ascending order.
        # *   ModifiedTimeDesc: sort the by modification time in descending order.
        # *   CreateTimeAsc: sorts the by creation time in ascending order.
        # *   SizeDesc: sorts by file size in descending order.
        # *   NameAsc: sorts by file name in ascending order.
        self.order_type = order_type
        # The parent folder ID. You can obtain the value by using the response parameter `FileId` of this operation.
        self.parent_file_id = parent_file_id
        # The ID of the logon region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to obtain the list of regions supported by cloud computers.
        self.region_id = region_id
        # The file status.
        # 
        # Valid values:
        # 
        # *   available: returns only normal file.
        # *   uploading: returns only the of objects that are being uploaded.
        self.status = status

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

        if self.file_ids_shrink is not None:
            result['FileIds'] = self.file_ids_shrink

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.parent_file_id is not None:
            result['ParentFileId'] = self.parent_file_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('FileIds') is not None:
            self.file_ids_shrink = m.get('FileIds')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ParentFileId') is not None:
            self.parent_file_id = m.get('ParentFileId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

