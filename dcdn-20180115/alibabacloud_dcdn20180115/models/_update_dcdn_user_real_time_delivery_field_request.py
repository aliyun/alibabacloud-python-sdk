# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDcdnUserRealTimeDeliveryFieldRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        fields: str = None,
    ):
        # The type of the collected logs. Default value: cdn_log_access_l1. Valid values:
        # 
        # *   **cdn_log_access_l1**: access logs of L1 Dynamic Route for CDN (DCDN) points of presence (POPs)
        # *   **cdn_log_origin**: back-to-origin logs
        # *   **cdn_log_er**: EdgeRoutine logs
        self.business_type = business_type
        # The list of fields. Separate multiple fields with commas (,). For more information, see [Fields in a real-time log](https://help.aliyun.com/document_detail/324199.html).
        # 
        # This parameter is required.
        self.fields = fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.fields is not None:
            result['Fields'] = self.fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        return self

