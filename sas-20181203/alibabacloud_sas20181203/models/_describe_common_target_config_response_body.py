# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCommonTargetConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        target_list: List[main_models.DescribeCommonTargetConfigResponseBodyTargetList] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the details of the configuration items.
        self.target_list = target_list

    def validate(self):
        if self.target_list:
            for v1 in self.target_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TargetList'] = []
        if self.target_list is not None:
            for k1 in self.target_list:
                result['TargetList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.target_list = []
        if m.get('TargetList') is not None:
            for k1 in m.get('TargetList'):
                temp_model = main_models.DescribeCommonTargetConfigResponseBodyTargetList()
                self.target_list.append(temp_model.from_map(k1))

        return self

class DescribeCommonTargetConfigResponseBodyTargetList(DaraModel):
    def __init__(
        self,
        flag: str = None,
        target: str = None,
        target_type: str = None,
    ):
        # The mode in which the configuration takes effect. Valid values:
        # 
        # *   **add**: In this mode, the configuration takes effect on the assets.
        # *   **del**: In this mode, the configuration does not take effect on the assets.
        self.flag = flag
        # The ID of the asset on which the configuration takes effect.
        # 
        # > 
        # 
        # *   When you set the **TargetType** parameter to **uuid**, the value of this parameter indicates the UUID of an asset.
        # 
        # *   When you set the **TargetType** parameter to **Cluster**, the value of this parameter indicates the ID of a cluster.
        # 
        # *   When you set the **TargetType** parameter to **image_repo**, the value of this parameter indicates the ID of an image repository.
        self.target = target
        # The dimension from on which the feature was configured. Valid values:
        # 
        # *   **uuid**: the UUID of the asset
        # *   **Cluster**: the ID of the cluster
        # *   **image_repo**: the ID of the image repository
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flag is not None:
            result['Flag'] = self.flag

        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

