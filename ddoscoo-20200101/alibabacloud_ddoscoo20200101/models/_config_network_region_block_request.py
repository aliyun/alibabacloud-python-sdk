# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigNetworkRegionBlockRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        instance_id: str = None,
    ):
        # The configuration of the location blacklist, expressed as a JSON string with the following structure:
        # - **RegionBlockSwitch**: String type. Required. The switch status of the location blacklist. Valid values:
        #     - **on**: enabled
        #     - **off**: disabled
        # - **Countries**: Array type. Optional. The list of international region codes to block.
        #     > For more information about international region codes, see [Parameters for China and international regions](https://help.aliyun.com/document_detail/167926.html).
        # 
        # 
        # - **Provinces**: Array type. Optional. The list of China region codes to block.
        # 
        #     > For more information about China region codes, see [Parameters for China and international regions](https://help.aliyun.com/document_detail/167926.html).
        # 
        #     For example, `[11,12]` indicates Beijing and Tianjin.
        # 
        # This parameter is required.
        self.config = config
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # > You can call [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) to query the IDs of all Anti-DDoS Pro or Anti-DDoS Premium instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

