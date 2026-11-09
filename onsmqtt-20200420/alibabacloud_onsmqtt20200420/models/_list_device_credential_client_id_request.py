# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeviceCredentialClientIdRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        next_token: str = None,
        page_no: str = None,
        page_size: str = None,
    ):
        # Group ID of the MQTT version of the micro message queue.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the Cloud Message Queue MQTT version instance, which must match the actual instance ID used by the client. You can obtain this ID from the **Instance Details** page in the console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Token for starting the next page query.
        self.next_token = next_token
        # Indicates the page number of the returned results. The starting page is counted from 1.
        self.page_no = page_no
        # The maximum number of query records to display per page.
        # Value range: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

