# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveStreamBlockRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        block_type: str = None,
        domain_name: str = None,
        location_list: str = None,
        owner_id: int = None,
        region_id: str = None,
        release_time: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs. You can view the application name on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page of the ApsaraVideo Live console.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The blocking type. Valid values: blacklist and whitelist.
        # 
        # This parameter is required.
        self.block_type = block_type
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The blocked region. If you specify multiple regions, such as CN and AS, separate them with commas (,).
        # 
        # This parameter is required.
        self.location_list = location_list
        self.owner_id = owner_id
        self.region_id = region_id
        # The time when the blocking ends. The time must be in UTC. If you do not specify this parameter, the blocking is valid for 7 days by default.
        self.release_time = release_time
        # The name of the live stream. You can view the stream name on the [Stream Management](https://help.aliyun.com/document_detail/197397.html) page of the ApsaraVideo Live console.
        # 
        # This parameter is required.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.location_list is not None:
            result['LocationList'] = self.location_list

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('LocationList') is not None:
            self.location_list = m.get('LocationList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

