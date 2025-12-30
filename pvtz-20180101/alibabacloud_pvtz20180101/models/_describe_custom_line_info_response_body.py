# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCustomLineInfoResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        creator: str = None,
        creator_sub_type: str = None,
        creator_type: str = None,
        dnscategory: str = None,
        ipv_4s: List[str] = None,
        line_id: str = None,
        name: str = None,
        request_id: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The time when the custom line was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the custom line was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The creator of the custom line.
        self.creator = creator
        # The type of the creator. Valid values:
        # 
        # *   CUSTOM: Alibaba Cloud account
        # *   SUB: RAM user
        # *   STS: assumed role that obtains the Security Token Service (STS) token of a RAM role
        # *   OTHER: other roles
        self.creator_sub_type = creator_sub_type
        # The role of the creator. Valid values:
        # 
        # *   USER: user
        # *   SYSTEM: system
        self.creator_type = creator_type
        self.dnscategory = dnscategory
        # The IPv4 CIDR blocks.
        self.ipv_4s = ipv_4s
        # The unique ID of the custom line.
        self.line_id = line_id
        # The name of the custom line.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The time when the custom line was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the custom line was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type

        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type

        if self.dnscategory is not None:
            result['Dnscategory'] = self.dnscategory

        if self.ipv_4s is not None:
            result['Ipv4s'] = self.ipv_4s

        if self.line_id is not None:
            result['LineId'] = self.line_id

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')

        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')

        if m.get('Dnscategory') is not None:
            self.dnscategory = m.get('Dnscategory')

        if m.get('Ipv4s') is not None:
            self.ipv_4s = m.get('Ipv4s')

        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

