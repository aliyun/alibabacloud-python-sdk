# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        ecc_info: str = None,
    ):
        # The ID of the application. You can call the ListApplication operation to query the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the elastic compute container (ECC) that corresponds to the ECS instance on which you want to restart the application. You can call the QueryApplicationStatus operation to query the ECC ID. For more information, see [QueryApplicationStatus](https://help.aliyun.com/document_detail/149394.html).
        # 
        # *   Separate multiple ECC IDs with commas (,).
        # *   If you leave this parameter empty, the application will be restarted on all the ECS instances deployed with the application.
        self.ecc_info = ecc_info

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EccInfo') is not None:
            self.ecc_info = m.get('EccInfo')

        return self

