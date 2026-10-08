# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScaleOutApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        deploy_group: str = None,
        ecu_info: str = None,
    ):
        # The ID of the application that you want to scale out. You can call the ListApplication operation to query the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the instance group where the application you want to scale out is deployed. You can call the QueryApplicationStatus operation to query the group ID. For more information, see [QueryApplicationStatus](https://help.aliyun.com/document_detail/149394.html).
        # 
        # This parameter is required.
        self.deploy_group = deploy_group
        # The ID of the elastic compute unit (ECU) that corresponds to the Elastic Compute Service (ECS) instance to be added to the instance group for scale-out. You can call the ListScaleOutEcu operation to query the ECU ID. For more information, see [ListScaleOutEcu](https://help.aliyun.com/document_detail/149371.html). Separate multiple ECU IDs with commas (,).
        # 
        # This parameter is required.
        self.ecu_info = ecu_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.deploy_group is not None:
            result['DeployGroup'] = self.deploy_group

        if self.ecu_info is not None:
            result['EcuInfo'] = self.ecu_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DeployGroup') is not None:
            self.deploy_group = m.get('DeployGroup')

        if m.get('EcuInfo') is not None:
            self.ecu_info = m.get('EcuInfo')

        return self

