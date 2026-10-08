# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScaleInApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        ecc_info: str = None,
        force_status: bool = None,
    ):
        # The ID of the application. You can call the ListApplication operation to query the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the elastic compute container (ECC) that corresponds to the Elastic Compute Service (ECS) instance to be removed for the application. Separate multiple ECC IDs with commas (,). You can call the QueryApplicationStatus operation to query the ECC ID. For more information, see [QueryApplicationStatus](https://help.aliyun.com/document_detail/149394.html).
        # 
        # This parameter is required.
        self.ecc_info = ecc_info
        # Specifies whether to forcibly unpublish the application from the ECS instance. You need to set this parameter to true only if the ECS instance expires. In normal cases, you do not need to set this parameter to true.
        self.force_status = force_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.ecc_info is not None:
            result['EccInfo'] = self.ecc_info

        if self.force_status is not None:
            result['ForceStatus'] = self.force_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EccInfo') is not None:
            self.ecc_info = m.get('EccInfo')

        if m.get('ForceStatus') is not None:
            self.force_status = m.get('ForceStatus')

        return self

