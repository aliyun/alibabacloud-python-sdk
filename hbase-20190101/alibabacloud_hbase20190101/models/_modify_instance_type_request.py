# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceTypeRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        core_instance_type: str = None,
        master_instance_type: str = None,
    ):
        # The ID of target instance. You can call [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) to obtain target instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The new node specifications of the core node. You can invoke [DescribeInstanceType](https://help.aliyun.com/document_detail/145796.html) to obtain the available node specifications.
        # 
        # > You must specify either the MasterInstanceType parameter or the CoreInstanceType parameter.
        self.core_instance_type = core_instance_type
        # The new node specifications of the master node. You can invoke [DescribeInstanceType](https://help.aliyun.com/document_detail/145796.html) to obtain the available node specifications.
        # 
        # > You must specify either the MasterInstanceType parameter or the CoreInstanceType parameter.
        self.master_instance_type = master_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type

        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')

        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')

        return self

