# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAirflowLoginTokenRequest(DaraModel):
    def __init__(
        self,
        airflow_id: str = None,
    ):
        # The ID of the Airflow instance. You can view the instance ID on the [Airflow Instances](https://help.aliyun.com/document_detail/2881043.html) page.
        # 
        # This parameter is required.
        self.airflow_id = airflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airflow_id is not None:
            result['AirflowId'] = self.airflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')

        return self

