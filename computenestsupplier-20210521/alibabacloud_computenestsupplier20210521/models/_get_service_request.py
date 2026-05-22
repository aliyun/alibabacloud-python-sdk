# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetServiceRequest(DaraModel):
    def __init__(
        self,
        filter_ali_uid: bool = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_name: str = None,
        service_version: str = None,
        shared_account_type: str = None,
        show_detail: List[str] = None,
    ):
        # Specifies whether to filter information based on Alibaba Cloud account IDs.
        self.filter_ali_uid = filter_ali_uid
        # The region ID.
        self.region_id = region_id
        # The service ID.
        self.service_id = service_id
        # The Service Instance Id.
        self.service_instance_id = service_instance_id
        # The Service Name.
        self.service_name = service_name
        # The service version.
        self.service_version = service_version
        # The share type of the service. Default value: SharedAccount. Valid values:
        # 
        # *   SharedAccount: The service is shared by multiple accounts.
        # *   Resell: The service is distributed.
        self.shared_account_type = shared_account_type
        # The information that you want to query.
        self.show_detail = show_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_ali_uid is not None:
            result['FilterAliUid'] = self.filter_ali_uid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.shared_account_type is not None:
            result['SharedAccountType'] = self.shared_account_type

        if self.show_detail is not None:
            result['ShowDetail'] = self.show_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterAliUid') is not None:
            self.filter_ali_uid = m.get('FilterAliUid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('SharedAccountType') is not None:
            self.shared_account_type = m.get('SharedAccountType')

        if m.get('ShowDetail') is not None:
            self.show_detail = m.get('ShowDetail')

        return self

