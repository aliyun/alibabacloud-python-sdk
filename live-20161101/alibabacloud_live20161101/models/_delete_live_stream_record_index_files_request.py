# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteLiveStreamRecordIndexFilesRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        owner_id: int = None,
        record_id: List[str] = None,
        region_id: str = None,
        remove_file: str = None,
        stream_name: str = None,
    ):
        # The AppName of the live stream.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The array of index file IDs.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The region ID.
        self.region_id = region_id
        # Specifies whether to delete the associated OSS objects at the same time. Valid values:
        # 
        # - **true**: Deletes.
        # 
        # - **false**: Does not delete.
        # 
        # This parameter is required.
        self.remove_file = remove_file
        # The stream name.
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

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remove_file is not None:
            result['RemoveFile'] = self.remove_file

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoveFile') is not None:
            self.remove_file = m.get('RemoveFile')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

