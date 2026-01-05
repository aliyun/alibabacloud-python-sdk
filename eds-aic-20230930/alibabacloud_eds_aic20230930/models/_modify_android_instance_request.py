# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyAndroidInstanceRequest(DaraModel):
    def __init__(
        self,
        android_instance_id: str = None,
        down_bandwidth_limit: int = None,
        instance_ids: List[str] = None,
        new_android_instance_name: str = None,
        up_bandwidth_limit: int = None,
    ):
        # The ID of the cloud phone instance.
        self.android_instance_id = android_instance_id
        self.down_bandwidth_limit = down_bandwidth_limit
        self.instance_ids = instance_ids
        # The new name of the cloud phone instance.
        # 
        # >  The name can be up to 30 characters in length. It can contain letters, digits, colons (:), underscores (_), periods (.), or hyphens (-). It must start with letters but cannot start with http:// or https://.
        self.new_android_instance_name = new_android_instance_name
        self.up_bandwidth_limit = up_bandwidth_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id

        if self.down_bandwidth_limit is not None:
            result['DownBandwidthLimit'] = self.down_bandwidth_limit

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.new_android_instance_name is not None:
            result['NewAndroidInstanceName'] = self.new_android_instance_name

        if self.up_bandwidth_limit is not None:
            result['UpBandwidthLimit'] = self.up_bandwidth_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')

        if m.get('DownBandwidthLimit') is not None:
            self.down_bandwidth_limit = m.get('DownBandwidthLimit')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('NewAndroidInstanceName') is not None:
            self.new_android_instance_name = m.get('NewAndroidInstanceName')

        if m.get('UpBandwidthLimit') is not None:
            self.up_bandwidth_limit = m.get('UpBandwidthLimit')

        return self

