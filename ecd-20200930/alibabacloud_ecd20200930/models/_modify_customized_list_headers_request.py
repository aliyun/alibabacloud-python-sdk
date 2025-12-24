# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ModifyCustomizedListHeadersRequest(DaraModel):
    def __init__(
        self,
        headers: List[main_models.ModifyCustomizedListHeadersRequestHeaders] = None,
        list_type: str = None,
        region_id: str = None,
    ):
        # The headers.
        self.headers = headers
        # The type of the list.
        # 
        # Valid values:
        # 
        # *   desktop: cloud computer
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.list_type = list_type
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.headers:
            for v1 in self.headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Headers'] = []
        if self.headers is not None:
            for k1 in self.headers:
                result['Headers'].append(k1.to_map() if k1 else None)

        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('Headers') is not None:
            for k1 in m.get('Headers'):
                temp_model = main_models.ModifyCustomizedListHeadersRequestHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyCustomizedListHeadersRequestHeaders(DaraModel):
    def __init__(
        self,
        display_type: str = None,
        header_key: str = None,
    ):
        # The display type of the header.
        # 
        # > For the desktop_id_name and office_site_id_name head keys, set the value of this parameter to required. For other header keys, set the value of this parameter to display or hide based on your requirements.
        self.display_type = display_type
        # The key of the header.
        # 
        # > All header keys of the list must be specified.
        # 
        # Valid values:
        # 
        # *   desktop_id_name: the IDs and names of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   system_data_disk: the system disks and data disks of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   office_site_type: the office network types of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   create_time: the time when the cloud computers are created.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ip: the IP addresses of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   spec_system_protocol: the instance types, OSs, and protocol types of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   monitor: the monitoring information of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   assigned_users: the number of end users that are assigned to the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   encryption: indicates whether the cloud computers are encrypted.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   office_site_id_name: the IDs and names of the office networks.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   pay_type: the billing methods of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   tag: the tags that are attached to the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   hostname: the hostnames of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   status: the statuses of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   current_user: the current end users of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.header_key = header_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_type is not None:
            result['DisplayType'] = self.display_type

        if self.header_key is not None:
            result['HeaderKey'] = self.header_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayType') is not None:
            self.display_type = m.get('DisplayType')

        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')

        return self

