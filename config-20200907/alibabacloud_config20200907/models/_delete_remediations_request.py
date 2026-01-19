# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRemediationsRequest(DaraModel):
    def __init__(
        self,
        remediation_ids: str = None,
    ):
        # The ID of the remediation template. Separate multiple remediation template IDs with commas (,).
        # 
        # For more information about how to obtain the ID of a remediation template, see [ListRemediations](https://help.aliyun.com/document_detail/270772.html).
        # 
        # This parameter is required.
        self.remediation_ids = remediation_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remediation_ids is not None:
            result['RemediationIds'] = self.remediation_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationIds') is not None:
            self.remediation_ids = m.get('RemediationIds')

        return self

