# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListInstancesRequest(DaraModel):
    def __init__(
        self,
        cross_region_replication: str = None,
        edition: str = None,
        instance_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.cross_region_replication = cross_region_replication
        # The edition of the license. Valid values:
        # - free: Free edition.
        # - trial: Trial edition.
        # - scalability: Scalability edition.
        # - standard: Standard edition.
        # - enterprise: Enterprise edition.
        self.edition = edition
        # Instance ID list.
        self.instance_ids = instance_ids
        # Page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Instance status. Valid values:
        # - creating: Being created.
        # - running: Running.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_region_replication is not None:
            result['CrossRegionReplication'] = self.cross_region_replication

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossRegionReplication') is not None:
            self.cross_region_replication = m.get('CrossRegionReplication')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

