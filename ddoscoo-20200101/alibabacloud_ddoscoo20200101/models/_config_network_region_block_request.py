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
        # The details of the configurations of blocked locations. This parameter is a JSON string. The value consists of the following fields:
        # 
        # *   **RegionBlockSwitch**: the status of the location blacklist feature. This field is required and must be of the string type. Valid values:
        # 
        #     *   **on**
        #     *   **off**
        # 
        # *   **Countries**: the codes of the countries and areas from which you want to block requests. This field is optional and must be of the array type.
        # 
        #     **
        # 
        #     **Note** For more information about the codes of countries and areas, see [Location parameters](https://help.aliyun.com/document_detail/167926.html).
        # 
        # *   **Provinces**: the codes of the administrative regions in China from which you want to block requests. This field is optional and must be of the array type.
        # 
        #     **
        # 
        #     **Note** For more information about the codes of administrative regions in China, see [Location parameters](https://help.aliyun.com/document_detail/167926.html).
        # 
        #     For example, `[11,12]` specifies Beijing and Tianjin.
        # 
        # This parameter is required.
        self.config = config
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
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

