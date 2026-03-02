# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class SubmitSqlPreviewRequest(DaraModel):
    def __init__(
        self,
        body: main_models.SqlStatementWithContext = None,
        session_cluster_name: str = None,
    ):
        self.body = body
        # This parameter is required.
        self.session_cluster_name = session_cluster_name

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.session_cluster_name is not None:
            result['sessionClusterName'] = self.session_cluster_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.SqlStatementWithContext()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('sessionClusterName') is not None:
            self.session_cluster_name = m.get('sessionClusterName')

        return self

